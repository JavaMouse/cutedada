module.exports = {
  outputDir: process.env.outputDir,
  assetsDir: 'static',
  css: {
    loaderOptions: {
      sass: {
        data: `@import "@/style/mixin.scss";`
      }
    }
  },
  devServer: {
    open: false,
    host: '0.0.0.0',
    port: 9000,
    https: false,
    hotOnly: false,
    proxy: {
      '/ywpt': {
        target: 'http://10.10.0.10:9090',
        changeOrigin: true
      }
    }
  },
  configureWebpack: {
    externals: {
      'zlplayer': 'zlplayer'
    }
  }
}
