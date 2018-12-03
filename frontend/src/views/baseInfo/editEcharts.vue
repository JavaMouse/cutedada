<template>
    <el-container>
        <el-header class="page-topic">
            数据表:
            <el-select v-model="value" size="mini" placeholder="请选择数据表" @change="blurChange">
                <el-option v-for="item in tableNames" :key="item" :label="item" :value="item">
                </el-option>
            </el-select>
             图表类型:
            <el-select v-model="chartName" size="mini" placeholder="请选择数据表">
                <el-option v-for="item in chartTypeList" :key="item" :label="item" :value="item">
                </el-option>
            </el-select>
            <el-button size="mini" type="primary" @click="drawChart">生成图表</el-button>
        </el-header>
        <el-main class="main">
            <!-- <div>
                <div>
                    <div v-for="item in colItem">{{item}}</div>
                </div>
            </div> -->
            <!-- <kanban-board :stages="stages" :blocks="blocks" @update-block="updateBlock"></kanban-board> -->
            <kanban-board :stages="stages" :blocks="blocks" @update-block="updateBlock">
                <div v-for="stage in stages" :slot="stage" class="stageDiv">
                    <h5>{{ stage }}</h5>
                </div>
                <div v-for="block in blocks" :slot="block.id" class="blockDiv">
                    <!-- <div>
                        <strong>id:</strong> {{ block.id }}
                        </div> -->
                        <div>
                        {{ block.title }} ( {{block.col}} )
                    </div>
                </div>
            </kanban-board>

            <div style="width:100%;height:500px;">
                    <div v-bind:style="styleObj" ref="myChart"></div>
            </div>
            
        </el-main>
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
                ]
            }
        },

        watch: {
            
        },
        mounted () {
            this.getTableList()
            this.test()
        },
        methods: {
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
                console.log(blockArr)
            },
            updateBlock(id, status) {
                this.blocks.find(b => b.id === Number(id)).status = status;
                console.log(id,status)
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
            }
            
        }
    }
</script>
<style lang="scss" scoped>
    .main {
        width: 100%;
        padding: 0 !important;
        margin: 0 !important;
        position: relative;
        text-align: left;
    }
    .page-topic {
        height: 70px !important;
        background-color: #fff;
        box-shadow: 0 -1px 0 0 #EAEBF0 inset;
        text-align: left;
        line-height: 70px;
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
        background-color: #fff;
    }
</style>