module.exports = {
  outputDir: process.env.outputDir,
  assetsDir: 'static',
  devServer: {
    open: false,
    host: '0.0.0.0',
    port: 9000,
    https: false,
    hotOnly: false,
    proxy: 'http://127.0.0.1:5000',
  }
}
