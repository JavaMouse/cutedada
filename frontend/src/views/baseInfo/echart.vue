<template>
    <!-- <div class="welcome_main">
        <div id="myChart" :style="{width: '80%', height: '60%'}"></div>
    </div> -->
    <grid-layout
            :layout="layout"
            :col-num="12"
            :row-height="30"
            :is-draggable="true"
            :is-resizable="true"
            :vertical-compact="true"
            :margin="[10, 10]"
            :use-css-transforms="true"
    >

        <grid-item v-for="item in layout"
        style="border:1px solid red;"
                   :x="item.x"
                   :y="item.y"
                   :w="item.w"
                   :h="item.h"
                   :i="item.i">
            {{item.i}}
        </grid-item>
    </grid-layout>
</template>

<script>
    import VueGridLayout from 'vue-grid-layout';
    var testLayout = [
	    {"x":0,"y":0,"w":2,"h":2,"i":"0"},
	    {"x":2,"y":0,"w":2,"h":4,"i":"1"},
	    {"x":4,"y":0,"w":2,"h":5,"i":"2"},
	    {"x":6,"y":0,"w":2,"h":3,"i":"3"},
	    {"x":8,"y":0,"w":2,"h":3,"i":"4"},
	    {"x":10,"y":0,"w":2,"h":3,"i":"5"},
	    {"x":0,"y":5,"w":2,"h":5,"i":"6"},
	    {"x":2,"y":5,"w":2,"h":5,"i":"7"},
	    {"x":4,"y":5,"w":2,"h":5,"i":"8"},
	    {"x":6,"y":4,"w":2,"h":4,"i":"9"}
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
                layout: testLayout
            }
        },
        mounted() {
            this.drawLine();
        },
        methods: {
            drawLine() {
               
                // 基于准备好的dom，初始化echarts实例
                // let myChart = this.$echarts.init(document.getElementById('myChart'))
                // 绘制图表
                // myChart.setOption({
                //     title: { text: 'echarts' },
                //     tooltip: {},
                //     xAxis: {
                //         data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
                //     },
                //     yAxis: {},
                //     series: [{
                //         name: '销量',
                //         type: 'bar',
                //         data: [5, 20, 36, 10, 10, 20]
                //     }]
                // });
            }
        }
    }
</script>
<style lang="scss" scoped>
    .welcome_main {
        text-align: center;
        background: #FFF;
        display: flex;
    }
</style>