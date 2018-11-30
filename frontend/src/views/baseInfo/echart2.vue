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
            <div>
                <div>
                    <div v-for="item in colItem">{{item}}</div>
                </div>
            </div>
            <div class="box" v-for="item in seriesData">
                <div class="btnContain">
                    <el-button @click="chartCheck(item.index)" type="success" size="mini" icon="el-icon-edit" circle></el-button>
                    <el-button @click="chartCheck(item.index)" type="danger" icon="el-icon-delete" size="mini" circle></el-button>
                    <el-button @click="chartCheck(item.index)" icon="el-icon-search" size="mini" circle></el-button>
                </div>
                <div v-bind:style="styleObj" :ref="item.name"></div>
            </div>
        </el-main>
    </el-container>
</template>
<script>
    import echarts from 'echarts'
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
            data: [],
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

    let option2 = {
        title: {
            text: '困人误报率',
            show: false
        },
        tooltip: {
            show: true,
            trigger: 'axis',
            formatter: '{b}: {c}%'
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
            data: [],
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
        },
        data () {
            return {
                barChart: {},
                barChartList: [],
                // barOption: option1,
                tableNames: [],
                value: '',
                colItem: [],
                chartList: [],
                styleObj: {
                    width: '100%',
                    height: '90%'
                },
                seriesData: {}
            }
        },
        watch: {
        },
        mounted () {
            // this.initChart()
            // this.renderChart()
            window.onresize = () => {
                // this.barChart.resize()
                // this.lineChart.resize()
            }
            this.getTableList()
        },
        methods: {
            change () {
                let chartData = [{ name: 'chart1', option: option1, index: 0 }, { name: 'chart2', option: option2, index: 1 },]
                // let seriesData = [];
                // chartData.forEach(function (item) {
                //     let outObj = {};
                //     let valueKey = Object.keys(item);
                //     outObj.name = item[valueKey[0]];
                //     outObj.value = item[valueKey[1]];
                //     outObj.index = item[valueKey[2]];
                //     seriesData.push(outObj);
                //     // this.renderChart(item)
                // });
                this.seriesData = chartData
                // console.log(this.seriesData)

                this.$nextTick(() => {
                    this.initChart(this.seriesData)
                    this.renderChart(this.seriesData)
                })
            },
            initChart (arr) {
                arr.forEach(item => {
                    let name = item.name
                    // console.log(this.$refs[name][0])
                    this.barChartList[item.index] = echarts.init(this.$refs[name][0])
                })
            },
            renderChart (val) {
                val.forEach(item => {
                    this.barChartList[item.index].setOption(item.option)
                })
            },
            chartCheck (value) {
                console.log('you choice: ' + value)
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
            },
            // add() {
            //     let that = this;
            //     $(function () {
            //         $(document).mousemove(function (e) {
            //             if (!!this.move) {
            //                 var posix = !document.move_target ? { 'x': 0, 'y': 0 } : document.move_target.posix,
            //                     callback = document.call_down || function () {
            //                         $(this.move_target).css({
            //                             'top': e.pageY - posix.y,
            //                             'left': e.pageX - posix.x
            //                         });
            //                     };

            //                 callback.call(this, e, posix);
            //             }
            //         }).mouseup(function (e) {
            //             if (!!this.move) {
            //                 var callback = document.call_up || function () { };
            //                 callback.call(this, e);
            //                 $.extend(this, {
            //                     'move': false,
            //                     'move_target': null,
            //                     'call_down': false,
            //                     'call_up': false
            //                 });
            //             }
            //         });
            //         var $box = $('#box').mousedown(function (e) {
            //             var offset = $(this).offset();

            //             this.posix = { 'x': e.pageX - offset.left, 'y': e.pageY - offset.top };
            //             $.extend(document, { 'move': true, 'move_target': this });
            //         }).on('mousedown', '#coor', function (e) {
            //             var posix = {
            //                 'w': $box.width(),
            //                 'h': $box.height(),
            //                 'x': e.pageX,
            //                 'y': e.pageY
            //             };
            //             that.a = posix.w + 'px'
            //             console.log(posix)
            //             console.log(that.a)

            //             $.extend(document, {
            //                 'move': true, 'call_down': function (e) {
            //                     $box.css({
            //                         'width': Math.max(30, e.pageX - posix.x + posix.w),
            //                         'height': Math.max(30, e.pageY - posix.y + posix.h)
            //                     });
            //                 }
            //             });
            //             return false;
            //         });
            //     });
            // },
        }
    }
</script>
<style lang="scss" scoped>
    .main {
        width: 100%;
        padding: 0 !important;
        margin: 0 !important;
        position: relative;
    }

    .box {
        display: inline-block;
        margin-left: 10px;
        width: 45%;
        height: 400px;
        cursor: move;
        position: relative;
        top: 30px;
        background-color: #FFF;
        border: 1px solid #CCCCCC;
        -webkit-box-shadow: 10px 10px 25px #ccc;
        -moz-box-shadow: 10px 10px 25px #ccc;
        box-shadow: 10px 10px 25px #ccc;
        overflow: hidden;
        border-radius: 15px;

        .btnContain {
            text-align: right;
            padding-right:10px;
            padding-top:10px;
        }
    }

    /* #coor {
        width: 10px;
        height: 10px;
        overflow: hidden;
        cursor: se-resize;
        position: absolute;
        right: 0;
        bottom: 0;
        background-color: #09C;
    } */

    .page-topic {
        height: 70px !important;
        background-color: #fff;
        box-shadow: 0 -1px 0 0 #EAEBF0 inset;
        text-align: left;
        line-height: 70px;
    }
</style>