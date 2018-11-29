<template>
    <el-container>
        <el-header class="page-topic">
            数据表:
            <el-select v-model="value" size="small" placeholder="请选择数据表" @blur="blurChange">
                    <el-option v-for="item in tableNames" :key="item" :label="item" :value="item">
                    </el-option>
                </el-select>
        </el-header>
        <el-main class="main">
            <!-- <div>
                <div>
                    <div v-for="item in colItem">{{item}}</div>
                </div>
            </div> -->
            <div id="box">
                <div id="myChart" v-bind:style="styleObj"></div>
                <div id="coor"></div>
            </div>
            <div id="box">
                <div id="myChart2" v-bind:style="styleObj"></div>
                <div id="coor"></div>
            </div>


        </el-main>

    </el-container>

</template>

<script>
    import echarts from 'echarts'
    import VueDraggableResizable from 'vue-draggable-resizable'
    export default {
        name: 'Echarts2',
        components: {
            VueDraggableResizable
        },
        data() {
            return {
                tableNames: [],
                value: '',
                colItem: [],
                a: '',
                isChange: false,
                styleObj: {
                    width: '100%',
                    height: '100%'
                },
                tabNames: [
                    '111',
                    '222',
                    '333'
                ]

            }
        },
        watch: {
            a: function (val, oldVal) {
                console.log('new: %s, old: %s', val, oldVal)
                this.drawLine()
                let myChart = this.$echarts.init(document.getElementById('myChart'))
                myChart.clear();
                myChart.setOption({
                    title: { text: 'echarts' },
                    tooltip: {},
                    xAxis: {
                        data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
                    },
                    yAxis: {},
                    series: [{
                        name: '销量',
                        type: 'bar',
                        data: [5, 20, 36, 10, 10, 20]
                    }]
                });
            }
        },
        mounted() {
            // this.add()
            this.drawLine()
            this.width = $('#box').width()
            this.getTableList()
        },
        methods: {
            async blurChange() {
                let response = await this.$axios.get('/table/fields/user', { tablename: this.tableNames[0] })
                this.colItem = response.data.fields
            },
            async getTableList() {
                let response = await this.$axios.get('/table/tableNames')
                if(response.code === 0){
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
            drawLine() {
                let myChart = this.$echarts.init(document.getElementById('myChart'))
                let myChart2 = this.$echarts.init(document.getElementById('myChart2'))
                myChart.setOption({
                    title: { text: 'echarts' },
                    tooltip: {},
                    xAxis: {
                        data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
                    },
                    yAxis: {},
                    series: [{
                        name: '销量',
                        type: 'bar',
                        data: [5, 20, 36, 10, 10, 20]
                    }]
                });
                myChart2.setOption({
                    title: { text: 'echarts' },
                    tooltip: {},
                    xAxis: {
                        data: ["aaa", "sss", "ddd", "aaa", "sss", "ddd"]
                    },
                    yAxis: {},
                    series: [{
                        name: '销量',
                        type: 'line',
                        data: [5, 20, 36, 10, 10, 20]
                    }]
                });
                window.onresize = myChart.resize;
                // $("#box").resize(function(){  
                //     myChart.resize(); 
                // })
                // window.addEventListener("resize", () => { Echarts2.resize();});
                // window.addEventListener("resize", () => { 
                //     this.myChart.resize();  
                // });

            }

        }
    }
</script>
<style lang="scss" scoped>
    .main {
        width: 100%;
        padding: 0!important;
        margin: 0!important;
        position: relative;
    }
    #box {
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
    }
    #coor {
        width: 10px;
        height: 10px;
        overflow: hidden;
        cursor: se-resize;
        position: absolute;
        right: 0;
        bottom: 0;
        background-color: #09C;
    }

    .page-topic {
        height: 70px !important;
        background-color: #fff;
        box-shadow: 0 -1px 0 0 #EAEBF0 inset;
        text-align: left;
        line-height: 70px;
    }
</style>