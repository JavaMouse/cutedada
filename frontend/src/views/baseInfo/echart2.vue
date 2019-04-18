<template>
    <el-container>
        <el-header class="page-topic">
            <p>展示页面</p>
        </el-header>
        <el-main class="main">
            <div class="box" v-for="(item,index) in seriesData" :key="index">
                <fullscreen ref="fullscreen" :fullscreen.sync="fullscreen" @change="fullscreenChange" style="width:100%;height:100%;background-color:#fff;">
                <div class="btnContain">
                    <el-button @click="chartCheck(item.index)" type="success" size="mini" icon="el-icon-edit" circle></el-button>
                    <el-button @click="deleteChart(item)" type="danger" icon="el-icon-delete" size="mini" circle></el-button>
                    <el-button @click="toggle(item.index)" icon="el-icon-search" size="mini" circle></el-button>
                </div>
                <div v-bind:style="styleObj" :ref="item.name"></div>
                <span class="descSpan" v-if="item.option">备注:  {{item.option.desc || '无'}}</span>
            </fullscreen>
            </div>
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
                value: '',
                chartList: [],
                styleObj: {
                    width: '100%',
                    height: '80%'
                },
                seriesData: {},
                option: [],
                chartmenber: [],
                creator: ''
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
            this.getCookieVal()
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
                        this.option[index].desc = res.desc
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
                            item2.type = 'line',
                            item2.smooth = true
                        })
                    } else if(res.chart_type === 2) {
                        this.option[index]={}
                        this.option[index].title = { 
                            text: res.title,
                            x: 'center'
                        }
                        this.option[index].desc = res.desc
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
                            item2.type = 'bar',
                            item2.smooth = true
                        })
                    } else {
                        this.option[index]={}
                        this.option[index].desc = res.desc
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
                    this.change(item)  
            },
            async getChart () {
                let response = await this.$axios.get('chart/get_chartId_list/'+'1')
                this.chartmenber = response.data.chartList || []
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
            change (val) {
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
                    this.delete(value)
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
            },
            async delete (value) {
                console.log("dele_id"+this.chartmenber[value.index])
                let res = await this.$axios.post('chart/delete_chart', {chart_id: this.chartmenber[value.index]})
                let data = {
                    chart_title: value.option.title.text || '',
                    creator: this.creator,
                    operate_type: 2,
                    chart_id: this.chartmenber[value.index]
                }
                let response2 = await this.$axios.post('chart/add_operate', data)
                if(res.code === 0 && response2.code === 0) {
                    this.$message.success('删除成功！')
                    this.getChart()
                } else {
                    this.$message.success('删除失败请重试！')
                }
            },
            getCookie(cookie_name) {
                var allcookies = document.cookie;
                var cookie_pos = allcookies.indexOf(cookie_name);
                if (cookie_pos != -1) {
                    // 把cookie_pos放在值的开始，只要给值加1即可
                    cookie_pos = cookie_pos + cookie_name.length + 1; 
                    //计算取cookie值得结束索引
                    var cookie_end = allcookies.indexOf(";", cookie_pos);
                    if (cookie_end == -1) {
                        cookie_end = allcookies.length;
                    }
                    //得到想要的cookie的值
                    var value = unescape(allcookies.substring(cookie_pos, cookie_end)); 
                }
                return value;
            },
            getCookieVal () {
                let cookie_name = 'username'
                let cookie_value = this.getCookie(cookie_name)
                this.creator = cookie_value
            },
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
        height: 430px;
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
        background-color: #fff;
        box-shadow: 0 -1px 0 0 #EAEBF0 inset;
        text-align: left;
        p {
            font-size: 16px;
            font-weight: bold;
        }
    }
    .descSpan {
        width: 100%;
        font-size: 14px;
        display: inline-block;
        margin-top: 8px;
        text-align: center;
    }
</style>