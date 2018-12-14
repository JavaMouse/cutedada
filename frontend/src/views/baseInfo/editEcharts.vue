<template>
    <el-container>
        <el-header class="page-topic">
            
        </el-header>
        <div class="content">
            <div class="stepDiv">
                <el-steps :active="activeNum" align-center>
                    <el-step title="步骤1" description="选择数据表"></el-step>
                    <el-step title="步骤2" description="选择x轴、y轴字段"></el-step>
                    <el-step title="步骤3" description="填写过滤器。度量内容"></el-step>
                    <el-step title="步骤4" description="生成图表"></el-step>
                </el-steps>
                <el-button size="mini" style="margin-top: 12px;" @click="next">下一步</el-button>
                <el-button size="mini" style="margin-top: 12px;" @click="pre">上一步</el-button>

            </div>
            <div class="contentDiv" v-if="activeNum===1">
                 请选择数据表:
                <el-select v-model="value" size="mini" placeholder="请选择数据表" @change="blurChange">
                    <el-option v-for="item in tableNames" :key="item" :label="item" :value="item">
                    </el-option>
                </el-select>
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
            </div>
            <div class="contentDiv" v-if="activeNum===3">
                图表类型:
                <el-select v-model="chartName" size="mini" placeholder="请选择数据表" class="dropStyle">
                    <el-option v-for="item in chartTypeList" :key="item" :label="item" :value="item">
                    </el-option>
                </el-select><br>
                x轴过滤器内容:
                <el-input class="dropStyle" size="mini" v-model="input" style="width:160px"></el-input><br>
                x轴度量:
                <el-select class="dropStyle" v-model="xMetric" size="mini" placeholder="请选择x轴度量">
                    <el-option v-for="item in xMetricList" :key="item" :label="item" :value="item">
                    </el-option>
                </el-select><br>
                y轴度量:
                <el-select class="dropStyle" v-model="yMetric" size="mini" placeholder="请选择y轴度量">
                    <el-option v-for="item in yMetricList" :key="item" :label="item" :value="item">
                    </el-option>
                </el-select><br>
            </div>
            <div class="contentDiv" v-if="activeNum===4">
                <el-button size="mini" type="primary" @click="drawChart">生成图表</el-button>
                 <div style="width:100%;height:500px;">
                    <div v-bind:style="styleObj" ref="myChart"></div>
                </div>
            </div>
        </div>
    </el-container>
</template>
<script>
    import echarts from 'echarts'
    import '../../css/kanban.css'
    // import '../../util/kanban1.js'
    // import '../../util/kanban2.js'
    // import '../../util/kanban3.js'
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
                activeNum: 1,
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
                value: '',
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
                    'bar','line'
                ],
                chartName: '',

                stages: ['列名', 'x轴', 'y轴','series'],
                blocks: [
                    {
                    id: 1,
                    status: '列名',
                    title: 'Test',
                    col: ''
                    },
                ],
                xlist: [],
                ylist: [],
                slist: []
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
                    this.activeNum++
                }
            },
            pre() {
                if (this.activeNum > 1) {
                    this.activeNum--
                }
            },
            drawChart () {
                this.initChart()
                this.renderChart()
            },
            initChart () {
                this.myChart = echarts.init(this.$refs.myChart)
            },
            renderChart () {
                this.myChart.setOption(option)
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
                // console.log(blockArr)
            },
            updateBlock(id, status) {
                this.xlist = []
                this.ylist = []
                this.slist = []
                
                this.blocks.find(b => b.id === Number(id)).status = status;
                console.log(id,status)

                this.blocks.forEach(item=>{
                    if(item.status === 'x轴'){
                        this.xlist.push(item.title)
                    }
                    else if(item.status === 'y轴'){
                        this.ylist.push(item.title)
                    }
                    else if(item.status === 'series'){
                        this.slist.push(item.title)
                    }
                })
                console.log('xlist:' + this.xlist)
                console.log('ylist:' + this.ylist)
                console.log('slist:' + this.slist)
            },
            async blurChange () {
                console.log(this.value)
                let response = await this.$axios.get('/table/fields/' + this.value)
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
</style>