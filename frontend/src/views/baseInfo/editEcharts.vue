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
            <div>
                <div>
                    <div v-for="item in colItem">{{item}}</div>
                </div>
            </div>
            <!-- <kanban-board :stages="stages" :blocks="blocks" @update-block="updateBlock"></kanban-board> -->
            <kanban-board :stages="stages" :blocks="blocks" @update-block="updateBlock">
                <div v-for="stage in stages" :slot="stage" class="stageDiv">
                    <h5>{{ stage }}</h5>
                </div>
                <div v-for="block in blocks" :slot="block.id" class="blockDiv">
                    <div>
                        <strong>id:</strong> {{ block.id }}
                        </div>
                        <div>
                        {{ block.title }}
                    </div>
                </div>
            </kanban-board>
        </el-main>
    </el-container>
</template>
<script>
    import echarts from 'echarts'
    import '../../css/kanban.css';

    export default {
        name: 'editEcharts',
        components: {
        },
        data () {
            return {
                tableNames: [],
                value: '',
                colItem: [],
                stages: ['列名', 'x轴', 'y轴'],
                blocks: [
                    {
                    id: 1,
                    status: '列名',
                    title: 'Test',
                    },
                ]
            }
        },

        watch: {
            
        },
        mounted () {
        },
        methods: {
            updateBlock(id, status) {
                this.blocks.find(b => b.id === Number(id)).status = status;
                console.log(id,status)
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