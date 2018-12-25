<template>
    <el-container>
        <el-header class="page-topic">
            数据表:
            <el-select v-model="value" size="small" placeholder="请选择数据表" @blur="blurChange">
                <el-option v-for="item in tableNames" :key="item" :label="item" :value="item">
                </el-option>
            </el-select>
            <el-button @click="change">刷新</el-button>
        </el-header>
        <el-main class="main">
            <!-- <div>
                <div>
                    <div v-for="item in colItem">{{item}}</div>
                </div>
            </div> -->
            <div class="box" v-for="(item,index) in seriesData" :key="index">
                <fullscreen ref="fullscreen" :fullscreen.sync="fullscreen" @change="fullscreenChange" style="width:100%;height:100%;background-color:#fff;">
                <div class="btnContain">
                    <el-button @click="chartCheck(item.index)" type="success" size="mini" icon="el-icon-edit" circle></el-button>
                    <el-button @click="deleteChart(item.index)" type="danger" icon="el-icon-delete" size="mini" circle></el-button>
                    <el-button @click="toggle(item.index)" icon="el-icon-search" size="mini" circle></el-button>
                </div>
                <div v-bind:style="styleObj" :ref="item.name"></div>
            </fullscreen>
            </div>
       
            <!-- <template>
                    <vue-draggable-resizable class="box2" v-for="item in seriesData" :w="500" :h="400" v-on:dragging="onDrag" v-on:resizing="onResize(item.index)" :parent="true">
                            <div class="btnContain">
                                <el-button @click="chartCheck(item.index)" type="success" size="mini" icon="el-icon-edit" circle></el-button>
                                <el-button @click="chartCheck(item.index)" type="danger" icon="el-icon-delete" size="mini" circle></el-button>
                                <el-button @click="chartCheck(item.index)" icon="el-icon-search" size="mini" circle></el-button>
                            </div>
                            <div v-bind:style="styleObj" :ref="item.name"></div>
                    </vue-draggable-resizable>
            </template> -->
            
        </el-main>
    </el-container>
</template>
<script>
    import echarts from 'echarts'
    import VueDraggableResizable from 'vue-draggable-resizable'

    let option1 = {
        title: {
            text: '误报数量与在线台数环比增长关系',
            show: false
        },
        tooltip: {
            show: true,
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            bottom: 20
        },
        grid: {
            left: 58,
            top: 55,
            right: 20,
            bottom: 84
        },
        xAxis: {
            type: 'category',
            data: ['1月','2月','3月'],
            nameTextStyle: {
                color: '#4B4F58',
                align: 'right'
            },
            nameGap: 20,
            axisLine: {
                lineStyle: {
                    color: '#EAEBF0'
                }
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                color: '#878A92'
            }
        },
        yAxis: {
            type: 'value',
            name: '困人数',
            nameTextStyle: {
                color: '#4B4F58',
                align: 'right',
                padding: [0, 40, 10, 0]
            },
            nameGap: 10,
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                color: '#878A92'
            },
            splitLine: {
                lineStyle: {
                    color: '#EAEBF0'
                }
            }
        },
        color: ['#F5810F', '#3083F2', '#10C79E'],
        series: [{
            name: '误报数量',
            type: 'line',
            barWidth: 6,
            data: ['12', '2', '3']
        }, {
            name: '深度学习误报数',
            type: 'bar',
            barWidth: 6,
            data: ['7', '6', '1']
        }, {
            name: '电梯数量',
            type: 'bar',
            barWidth: 6,
            data: ['2', '2', '1']
        }]
    }
    let option3 = {
    title: {
        text: '柱状图'
    },
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎','百度','谷歌','必应','其他']
    },
    xAxis : 
        {
            type : 'category',
            data : ['周一','周二','周三','周四','周五','周六','周日']
        },
    yAxis : 
        {
            type : 'value'
        },
    series : [
        {
            name:'直接访问',
            type:'bar',
            //折线图：line
            data:[320, 332, 301, 334, 390, 330, 320]
        },
        {
            name:'百度',
            type:'bar',
            data:[620, 732, 701, 734, 1090, 1130, 1120]
        }
    ]
};

    let option2 = {
        title: {
            text: '困人误报率',
            show: false
        },
        tooltip: {
            show: true,
            trigger: 'axis',
            axisPointer:{
                type: 'shadow'
            }
        },
        grid: {
            left: 58,
            top: 55,
            right: 40,
            bottom: 84
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['1','2','3','4','5','6','7'],
            nameTextStyle: {
                color: '#4B4F58',
                align: 'right'
            },
            nameGap: 20,
            axisLine: {
                lineStyle: {
                    color: '#EAEBF0'
                }
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                color: '#878A92'
            }
        },
        yAxis: {
            type: 'value',
            name: '误报率',
            nameTextStyle: {
                color: '#4B4F58',
                align: 'right',
                padding: [0, 40, 10, 0]
            },
            nameGap: 10,
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                color: '#878A92',
                formatter(val) {
                    return val + '%'
                }
            },
            splitLine: {
                lineStyle: {
                    color: '#EAEBF0'
                }
            }
        },
        color: ['#7825FA'],
        series: [{
            name: '误报率',
            type: 'line',
            data: [80, 400, 200, 210, 180, 150, 260],
            areaStyle: {
                color: {
                    type: 'linear',
                    x: 0,
                    y: 0,
                    x2: 0,
                    y2: 1,
                    colorStops: [{
                        offset: 0, color: 'RGBA(120, 37, 250, 1)'
                    }, {
                        offset: 1, color: 'RGBA(120, 37, 250, 0)'
                    }]
                }
            }
        }]
    }
    export default {
        name: 'Echarts2',
        components: {
            'vue-draggable-resizable': VueDraggableResizable
        },
        data () {
            return {
                fullscreen: false,
                width: 0,
                height: 0,
                x: 0,
                y: 0,
                barChart: {},
                barChartList: [],
                tableNames: [],
                value: '',
                colItem: [],
                chartList: [],
                styleObj: {
                    width: '100%',
                    height: '90%'
                },
                seriesData: {},
                option4: {},
                option5: {},
                option: [],
                chartmenber: []
            }
        },
        watch: {
            
        },
        created () {
            this.getChart()
        },
        mounted () {
            window.onresize = () => {
                this.seriesData.forEach(item=>{
                    echarts.init(this.$refs[item.name][0]).resize()
                })
            }
            this.getTableList()
            // this.getChart()
        },
        methods: {
            async getcChartData (item,index) {
                let res = await this.$axios.get('chart/get_chart_info/'+item)
                    if(res.chart_type === 1) {
                        // 柱状图
                        this.option[index]={}
                        this.option[index].title = { 
                            text: res.title,
                            x: 'center'
                        }
                        this.option[index].xAxis = {
                            data: res.x_data,
                            type: 'category'
                        }
                        this.option[index].yAxis = { type: 'value' }
                        this.option[index].legend = {
                            bottom: 'bottom',
                            data: res.legend,
                            type: 'scroll'
                        }
                        this.option[index].tooltip = { trigger: 'axis' }
                        this.option[index].series = res.series
                        this.option[index].series.forEach(item2=>{
                            item2.type = 'line'
                        })
                    } else if(res.chart_type === 3) {
                        this.option[index]={}
                        this.option[index].title = { 
                            text: res.title,
                            x: 'center'
                        }
                        this.option[index].legend = {
                            bottom: 'bottom',
                            data: res.legend,
                            type: 'scroll'
                        }
                        this.option[index].tooltip = { trigger: 'item' }
                        this.option[index].series = res.series
                    }
                    this.change()  
            },
            getChart () {
                this.chartmenber = ['1','3']
                this.chartmenber.forEach((item,index) => {
                    this.getcChartData(item,index)
                });
            },
            toggle (value) {
                this.$refs['fullscreen'][value].toggle() 
            },
            fullscreenChange (fullscreen) {
                this.fullscreen = fullscreen
                this.$nextTick(() => {
                        this.seriesData.forEach(item=>{
                        echarts.init(this.$refs[item.name][0],'light').resize()
                    })
                })
            },
            onResize: function (x, y, width, height) {
                this.x = x
                this.y = y
                this.width = width
                this.height = height
            },
            onDrag: function (x, y) {
                this.x = x
                this.y = y
            },
            change () {
                console.log(this.option)
                let getchartData = []
                this.chartmenber.forEach((item,i)=>{
                    getchartData[i] = {
                        name: 'chart'+[i+1],
                        option: this.option[i],
                        index: i
                    }
                })
                let seriesData = [];
                getchartData.forEach(function (item) {
                    let outObj = {};
                    let valueKey = Object.keys(item);
                    outObj.name = item[valueKey[0]];
                    outObj.value = item[valueKey[1]];
                    outObj.index = item[valueKey[2]];
                    seriesData.push(outObj);
                });
                this.seriesData = getchartData
                this.$nextTick(() => {
                    this.initChart(this.seriesData)
                    this.renderChart(this.seriesData)
                })
            },
            initChart (arr) {
                arr.forEach(item => {
                    let name = item.name
                    this.barChartList[item.index] = echarts.init(this.$refs[name][0])
                })
            },
            renderChart (val) {
                val.forEach(item => {
                    this.barChartList[item.index].setOption(item.option,true)
                })
            },
            chartCheck (value) {
                console.log('you choice: ' + value)
            },
            // 删除
            deleteChart (value) {
                this.$confirm('此操作将永久删除该图表, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning',
                    center: true
                }).then(() => {
                    this.seriesData.splice(value,1)
                    console.log(this.seriesData)
                    this.$nextTick(() => {
                        this.initChart(this.seriesData)
                        this.renderChart(this.seriesData)
                    })
                    this.$message({
                        type: 'success',
                        message: '删除成功!'
                    });
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
            },
            async blurChange () {
                let response = await this.$axios.get('/table/fields/user', { tablename: this.tableNames[0] })
                if (response.code === 0) {
                    this.colItem = response.data.fields
                }
            },
            async getTableList () {
                let response = await this.$axios.get('/table/tableNames')
                if (response.code === 0) {
                    this.tableNames = response.data.tableNames
                    this.blurChange()
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

    .box {
        display: inline-block;
        margin-left: 30px;
        margin-bottom: 20px;
        width: 46%;
        height: 400px;
        cursor: move;
        position: relative;
        top: 30px;
        background-color: #FFF;
        border: 1px solid #CCCCCC;
        -webkit-box-shadow: 10px 10px 25px #ccc;
        -moz-box-shadow: 10px 10px 25px #ccc;
        box-shadow: 10px 10px 25px #ccc;
        border-radius: 15px;
        overflow: hidden;

        .btnContain {
            text-align: right;
            padding-right:10px;
            padding-top:10px;
        }
    }
    .page-topic {
        height: 70px !important;
        background-color: #fff;
        box-shadow: 0 -1px 0 0 #EAEBF0 inset;
        text-align: left;
        line-height: 70px;
    }
</style>