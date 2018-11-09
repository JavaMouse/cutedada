<template>
        <div id="app" style="width: 100%;">
            <!--<pre>{{ $data | json }}</pre>-->
            <div>
                <div class="layoutJSON">
                    Displayed as <code>[x, y, w, h]</code>:
                    <div class="columns">
                        <div class="layoutItem" v-for="item in layout">
                            <b>{{item.i}}</b>: [{{item.x}}, {{item.y}}, {{item.w}}, {{item.h}}]
                        </div>
                    </div>
                </div>
                <div ref="eventsDiv" class="eventsJSON">
                    Events:
                    <div v-for="event in eventLog" :key="event">
                        {{event}}
                    </div>
                </div>
            </div>
            <div id="content">
                <!--<button @click="decreaseWidth">Decrease Width</button>
                <button @click="increaseWidth">Increase Width</button>
                <button @click="addItem">Add an item</button>-->
                <grid-layout :layout="layout"
                             :col-num="12"
                             :row-height="30"
                             :is-draggable="true"
                             :is-resizable="true"
                             :vertical-compact="true"
                             :use-css-transforms="true"
                >
                    <grid-item v-for="item in layout"
                    style="display:inline-block;"
                               :x="item.x"
                               :y="item.y"
                               :w="item.w"
                               :h="item.h"
                               :i="item.i"
                               @resize="resizeEvent"
                               @move="moveEvent"
                               @resized="resizedEvent"
                               @moved="movedEvent"
                    >
                        <!-- <span class="text">{{item.i}}</span> -->
                        <div id="myChart" :style="{width: '80%', height: '80%'}"></div>
                    </grid-item>
                </grid-layout>
            </div>
            <!--<pre>{{eventLog | json}}</pre>-->
    
        </div>
</template>

<script>
    import VueGridLayout from 'vue-grid-layout';
    var testLayout = [
        { "x": 0, "y": 0, "w": 2, "h": 2, "i": "0" },
        { "x": 2, "y": 0, "w": 2, "h": 4, "i": "1" },
        { "x": 4, "y": 0, "w": 2, "h": 5, "i": "2" },
        { "x": 6, "y": 0, "w": 2, "h": 3, "i": "3" },
        { "x": 8, "y": 0, "w": 2, "h": 3, "i": "4" },
        { "x": 10, "y": 0, "w": 2, "h": 3, "i": "5" },
        { "x": 0, "y": 5, "w": 2, "h": 5, "i": "6" },
        { "x": 2, "y": 5, "w": 2, "h": 5, "i": "7" },
        { "x": 4, "y": 5, "w": 2, "h": 5, "i": "8" },
        { "x": 6, "y": 4, "w": 2, "h": 4, "i": "9" }
    ];

    var GridLayout = VueGridLayout.GridLayout;
    var GridItem = VueGridLayout.GridItem;




    export default {
        name: 'Echarts',
        components: {
            GridLayout: VueGridLayout.GridLayout,
            GridItem: VueGridLayout.GridItem
        },
        data() {
            return {
                layout: testLayout,
                index: 0,
                eventLog: []
            }
        },
        watch: {
            eventLog: function() {
                var eventsDiv = this.$refs.eventsDiv;
                eventsDiv.scrollTop = eventsDiv.scrollHeight;
            }
        },
        mounted() {
            this.drawLine();
        },
        methods: {
            moveEvent: function (i, newX, newY) {
                var msg = "MOVE i=" + i + ", X=" + newX + ", Y=" + newY;
                this.eventLog.push(msg);
                // console.log(msg);

            },
            movedEvent: function (i, newX, newY) {
                var msg = "MOVED i=" + i + ", X=" + newX + ", Y=" + newY;
                this.eventLog.push(msg);
                // console.log(msg);

            },
            resizeEvent: function (i, newH, newW, newHPx, newWPx) {
                var msg = "RESIZE i=" + i + ", H=" + newH + ", W=" + newW + ", H(px)=" + newHPx + ", W(px)=" + newWPx;
                this.eventLog.push(msg);
                // console.log(msg);
            },
            resizedEvent: function (i, newX, newY, newHPx, newWPx) {
                var msg = "RESIZED i=" + i + ", X=" + newX + ", Y=" + newY + ", H(px)=" + newHPx + ", W(px)=" + newWPx;
                this.eventLog.push(msg);
                // console.log(msg);
                this.a()
            },
            a () {
                console.log(123)
                let myChart = this.$echarts.init(document.getElementById('myChart'))
                $('#chart').resize(function () {
                    myChart.resize();
                });
            },
            /**
             *
             * @param i the item id/index
             * @param newH new height in grid rows
             * @param newW new width in grid columns
             * @param newHPx new height in pixels
             * @param newWPx new width in pixels
             *
             */
            resizedEvent: function (i, newH, newW, newHPx, newWPx) {
                var msg = "RESIZED i=" + i + ", H=" + newH + ", W=" + newW + ", H(px)=" + newHPx + ", W(px)=" + newWPx;
                this.eventLog.push(msg);
                console.log(msg);
            },
            drawLine() {
                let myChart = this.$echarts.init(document.getElementById('myChart'))
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
        }
    }
</script>
<style lang="scss" scoped>
    .welcome_main {
        /* text-align: center; */
        width: 100%;
        height: 100%;
        background: #cccccc;
        display: flex;
    }

    /*** EXAMPLE ***/
    #content {
        width: 100%;
    }

    .vue-grid-layout {
        background: #eee;
    }

    .layoutJSON {
        background: #ddd;
        border: 1px solid black;
        margin-top: 10px;
        padding: 10px;
    }

    .eventsJSON {
        background: #ddd;
        border: 1px solid black;
        margin-top: 10px;
        padding: 10px;
        height: 100px;
        overflow-y: scroll;
    }

    .columns {
        -moz-columns: 120px;
        -webkit-columns: 120px;
        columns: 120px;
    }

    .vue-grid-item:not(.vue-grid-placeholder) {
        background: #ccc;
        border: 1px solid black;
    }

    .vue-grid-item.resizing {
        opacity: 0.9;
    }

    .vue-grid-item.static {
        background: #cce;
    }

    .vue-grid-item .text {
        font-size: 24px;
        text-align: center;
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
        height: 100%;
        width: 100%;
    }

    .vue-grid-item .no-drag {
        height: 100%;
        width: 100%;
    }

    .vue-grid-item .minMax {
        font-size: 12px;
    }

    .vue-grid-item .add {
        cursor: pointer;
    }

    .vue-draggable-handle {
        position: absolute;
        width: 20px;
        height: 20px;
        top: 0;
        left: 0;
        background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='10' height='10'><circle cx='5' cy='5' r='5' fill='#999999'/></svg>") no-repeat;
        background-position: bottom right;
        padding: 0 8px 8px 0;
        background-repeat: no-repeat;
        background-origin: content-box;
        box-sizing: border-box;
        cursor: pointer;
    }
</style>