<template>
    <el-container>
        <!-- <el-header class="page-topic">
            
        </el-header> -->
        <div class="content">
            <div class="stepDiv">
                <el-steps :active="activeNum" align-center>
                    <el-step title="步骤1" description="选择数据表"></el-step>
                    <el-step title="步骤2" description="选择图表类型"></el-step>
                    <el-step title="步骤3" description="选择维度、度量、过滤器"></el-step>
                    <el-step title="步骤4" description="生成图表"></el-step>
                </el-steps>
                <el-button size="mini" style="margin-top: 12px;" @click="next">下一步</el-button>
                <el-button size="mini" style="margin-top: 12px;" @click="pre">上一步</el-button>

            </div>
            <div class="contentDiv" v-if="activeNum===0">
                 请选择数据表:
                <el-select v-model="editForm.chartName" size="mini" placeholder="请选择数据表" @change="blurChange">
                    <el-option v-for="item in tableNames" :key="item" :label="item" :value="item">
                    </el-option>
                </el-select>
            </div>
            <div class="contentDiv" v-if="activeNum===1">
               图表类型:
                <el-select v-model="editForm.chartType" size="mini" placeholder="请选择图表类型" class="dropStyle">
                    <el-option v-for="item in chartTypeList" :key="item.type" :label="item.name" :value="item.type">
                    </el-option>
                </el-select><br>
                图表标题: <el-input size="mini" v-model="editForm.title" class="inputStyle"></el-input><br>
                图表描述: <el-input size="mini" v-model="editForm.chartDesc" class="inputStyle"></el-input>
            </div>
            <div class="contentDiv" v-if="activeNum===2">
                <kanban-board :stages="stages" :blocks="blocks" @update-block="updateBlock">
                    <div v-for="(stage,index) in stages" :key="index" :slot="stage" class="stageDiv">
                        <h5>{{ stage }}</h5>
                    </div>
                    <div v-for="(block,index) in blocks" :key="index" :slot="block.id" class="blockDiv">
                            <div>
                            {{ block.title }} ( {{block.col}} )
                        </div>
                    </div>
                </kanban-board>
                <el-dialog title="提示" :visible.sync="addColDialog.show" width="30%" center>
                    度量名: <el-input size="mini" v-model="addColDialog.dimenseName" style="width:80%;margin-bottom:20px;"></el-input><br>
                    度量sql:<el-input size="mini" v-model="addColDialog.dimenseSql" style="width:80%;"></el-input>
                    <span slot="footer" class="dialog-footer">
                        <el-button @click="addColDialog.show = false" size="mini">取 消</el-button>
                        <el-button type="primary" @click="submitAddCol" size="mini">确 定</el-button>
                    </span>
                </el-dialog>
                <el-button size="mini" type="primary" @click="addCol">列名增加条件</el-button><br>
                过滤sql: <el-input v-model="editForm.filter" size="mini" class="inputStyle"></el-input>
            </div>
            <div class="contentDiv" v-if="activeNum===3">
                <el-button size="mini" type="primary" @click="drawChart">生成图表</el-button>
                <el-button size="mini" :disabled="chartDisabled" @click="saveChart">保存图表</el-button>
                 <div style="width:100%;height:500px;" v-if="errSQL!==''">
                    <div>当前sql出错，请重试！</div>
                    <div>sql: {{this.errSQL}}</div>
                </div>
                 <div style="width:100%;height:500px;" v-else>
                    <div v-bind:style="styleObj" ref="myChart"></div>
                </div>
            </div>
        </div>
    </el-container>
</template>
<script>
    import echarts from 'echarts'
    import '../../css/kanban.css'

let option = {
    color: ['#3398DB'],
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            data : ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            axisTick: {
                alignWithLabel: true
            }
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'直接访问',
            type:'bar',
            barWidth: '60%',
            data:[10, 52, 200, 334, 390, 330, 220]
        }
    ]
}


    export default {
        name: 'editEcharts',
        components: {
        },
        data () {
            return {
                chartDisabled: false,
                addColDialog: {
                    show: false
                },
                activeNum: 0,
                input: '',
                xMetric: '',
                yMetric: '',
                xMetricList: [
                    'avg','sum','count'
                ],
                yMetricList: [
                    'avg','sum','count'
                ],
                styleObj: {
                    width: '100%',
                    height: '90%'
                },
                myChart: {},
                tableNames: [
                    '用户名','密码','年龄'
                ],
                editForm: {
                    chartName: '',
                    title: '',
                    chartDesc: '',
                    chartType: '',
                    filter: ''
                },
                colItem: [
                { "field": "city", "field_type": "varchar", "id": 1, "memo": "城市" },
                { "field": "province", "field_type": "varchar", "id": 2, "memo": "省份" },
                { "field": "date", "field_type": "date", "id": 3, "memo": "日期" },
                { "field": "weather", "field_type": "varchar", "id": 4, "memo": "天气" },
                { "field": "min_temp", "field_type": "int", "id": 5, "memo": "最低温度" },
                { "field": "max_temp", "field_type": "int", "id": 6, "memo": "最高温度" },
                { "field": "wind", "field_type": "varchar", "id": 7, "memo": "风向" },
                { "field": "wind_speed", "field_type": "varchar", "id": 8, "memo": "风速" },
                { "field": "air_quality", "field_type": "varchar", "id": 9, "memo": "空气质量" },
                { "field": "aqi", "field_type": "int", "id": 10, "memo": "空气质量指数" }],
                chartTypeList: [
                    {
                        type: 1,
                        name: 'line'
                    },
                    {
                        type: 2,
                        name: 'bar'
                    },
                    {
                        type: 3,
                        name: 'pie'
                    }
                ],
                chartName: '',

                stages: ['列名', '主维度', '可选维度','度量','过滤器'],
                blocks: [
                    {
                    id: 1,
                    status: '列名',
                    title: 'Test',
                    col: ''
                    },
                ],
                mainDimense: [],
                optionDimense: [],
                measure: [],
                filter: [],
                mainDimenseSql: '',
                optionDimenseSql: [],
                measureSql: [],
                option: {},
                barChartList: [],
                chartObj: {},
                errSQL: ''
            }
        },

        watch: {
            
        },
        mounted () {
            this.getTableList()
            this.test()
        },
        methods: {
            next() {
                if (this.activeNum < 4) {
                    if(this.activeNum === 2){
                        if(this.measure.length === 0){
                            this.$message.error('度量不能为空！')
                        } else if(this.mainDimense.length === 0){
                            this.$message.error('主维度不能为空！')
                        } else {
                            this.activeNum++
                        }
                    } else {
                        this.activeNum++
                    }
                }
            },
            pre() {
                this.chartDisabled = false
                if (this.activeNum > 0) {
                    this.activeNum--
                }
            },
            addCol () {
                this.addColDialog.show = true
            },
            submitAddCol () {
                this.blocks.push({
                    title: this.addColDialog.dimenseName,
                    col: this.addColDialog.dimenseSql,
                    id: this.blocks.length + 1,
                    status: '列名'
                })
                this.addColDialog.show = false
            },
            async saveChart () {
                this.errSQL = ''
                this.chartDisabled = true
                let response = await this.$axios.post('chart/add_new_chart', this.chartObj)
                console.log(response)
            },
            async drawChart () {
                this.errSQL = ''
                let optionalList = []
                this.optionDimense.forEach((item,index) => {
                    optionalList.push({
                        dimension_name: this.optionDimense[index],
                        dimension_sql: this.optionDimenseSql[index],
                    })
                })
                let measureList = []
                this.measure.forEach((item,index) => {
                    measureList.push({
                        measurement_name: this.measure[index],
                        measurement_sql: this.measureSql[index],
                    })
                })
                let data = {
                    chart_type: this.editForm.chartType || '',
                    dashboard_id: 1,
                    chart_title: this.editForm.title || '',
                    chart_desc: this.editForm.chartDesc || '',
                    creator: 'chennan',
                    chart_table: this.editForm.chartName || '',
                    main_dimension: {
                        dimension_name: this.mainDimense[0],
                        dimension_sql: this.mainDimenseSql
                    },
                    optional_dimension_list: optionalList,
                    filter_list: [{
                        filter_sql: this.editForm.filter
                    }] ,
                    measurement_list: measureList
                }
                if(this.editForm.filter === '' || this.editForm.filter === null){
                    data.filter_list = []
                }
                if(this.mainDimense === '' || this.mainDimense === null){
                    data.main_dimension = {}
                }
                this.chartObj = data
                let res = await this.$axios.post('chart/preview_chart', data)
                console.log(res)
                if(res.success === false){
                    this.errSQL = res.sql
                } else if(res === null) {
                    this.errSQL = 'error！请重试'
                }else {
                    if(res.chart_type === 1) {
                        // 柱状图
                        this.option={}
                        this.option.title = { 
                            text: res.title,
                            x: 'center'
                        }
                        this.option.xAxis = {
                            data: res.x_data,
                            type: 'category'
                        }
                        this.option.yAxis = { type: 'value' }
                        this.option.legend = {
                            bottom: 'bottom',
                            data: res.legend,
                            type: 'scroll'
                        }
                        this.option.tooltip = { trigger: 'axis' }
                        this.option.series = res.series
                        this.option.series.forEach( item2 =>{
                            item2.type = 'line'
                        })
                    } else if(res.chart_type === 2) {
                        this.option={}
                        this.option.title = { 
                            text: res.title,
                            x: 'center'
                        }
                        this.option.xAxis = {
                            data: res.x_data,
                            type: 'category'
                        }
                        this.option.yAxis = { type: 'value' }
                        this.option.legend = {
                            bottom: 'bottom',
                            data: res.legend,
                            type: 'scroll'
                        }
                        this.option.tooltip = { trigger: 'axis' }
                        this.option.series = res.series
                        this.option.series.forEach( item2 =>{
                            item2.type = 'bar'
                        })
                    }else if(res.chart_type === 3) {
                        this.option={}
                        this.option.title = { 
                            text: res.title,
                            x: 'center'
                        }
                        this.option.legend = {
                            bottom: 'bottom',
                            data: res.legend,
                            type: 'scroll'
                        }
                        this.option.tooltip = { trigger: 'item' }
                        this.option.series = res.series
                    }
                    this.$nextTick(() => {
                        this.initChart()
                        this.renderChart()
                    })
                }
            },
            initChart () {
                this.myChart = echarts.init(this.$refs.myChart)
            },
            renderChart () {
                this.myChart.setOption(this.option)
            },
            test () {
                let blockArr = []
                this.colItem.forEach(item => {
                    blockArr.push({
                        id:item.id,
                        title:item.memo,
                        status:'列名',
                        col: item.field
                    })
                });
                this.blocks = blockArr
                console.log(blockArr)
            },
            updateBlock(id, status) {
                this.mainDimense = []
                this.optionDimense = []
                this.measure = []
                this.filter = []
                this.measureSql = []
                this.optionDimenseSql = []
                
                this.blocks.find(b => b.id === Number(id)).status = status;
                console.log(id,status)

                this.blocks.forEach(item=>{
                    if(item.status === '主维度'){
                        this.mainDimense.push(item.title)
                        this.mainDimenseSql = item.col
                    }
                    else if(item.status === '可选维度'){
                        this.optionDimense.push(item.title)
                        this.optionDimenseSql.push(item.col)
                    }
                    else if(item.status === '度量'){
                        this.measure.push(item.title)
                        this.measureSql.push(item.col)
                    }
                    else if(item.status === '过滤器'){
                        this.filter.push(item.title)
                    }
                })
                console.log('主维度:' + this.mainDimense)
                console.log('可选维度:' + this.optionDimense)
                console.log('度量:' + this.measure)
                console.log('过滤器:' + this.filter)
                if (this.mainDimense.length>1) {
                    this.$message.error("主维度只能选择一项！")
                }
            },
            async blurChange () {
                console.log(this.editForm.chartName)
                let response = await this.$axios.get('/table/fields/' + this.editForm.chartName)
                if (response.code === 0) {
                    this.colItem = response.data.fields
                    this.test()
                }
            },
            async getTableList () {
                let response = await this.$axios.get('/table/tableNames')
                if (response.code === 0) {
                    this.tableNames = response.data.tableNames
                }
                let province = '浙江'
                let res = await this.$axios.get('/table/colNames/'+province)
            }
            
        }
    }
</script>
<style lang="scss" scoped>
    .content{
        height: calc(100% - 50px);
        background-image: none;
    }
    .page-topic {
        height: 70px !important;
        background-color: #fff;
        box-shadow: 0 -1px 0 0 #EAEBF0 inset;
        text-align: left;
        line-height: 70px;
        overflow: hidden;
    }
    .stageDiv{
    }
    .blockDiv{
        color: black;
        background: #ccc;
    }
    /deep/ .drag-inner-list{
        list-style-type: none;
        padding: 0;
        background-color: #ddd7d7;
    }
    .stepDiv{
        width: 90%;
        margin: 0 auto;
        padding-top: 40px;
        padding-bottom: 20px;
    }
    .contentDiv{
        // border: 2px solid #c0c4cc;
        width: 90%;
        margin: 10px auto;
    }
    .dropStyle{
        margin-top: 15px;
    }
    .inputStyle{
        width: 175px;
        margin-top: 20px;
    }
</style>