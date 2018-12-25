import axios from 'axios'
import { Message } from 'element-ui'
import { CASHOST, UNIFIEDPATH, PARTNER_TOKEN } from './config'

let CancelToken = axios.CancelToken
let developToken = {}
if (process.env.NODE_ENV === 'development') developToken = { token: PARTNER_TOKEN }

axios.interceptors.request.use(config => {
  return config
}, error => {
  return Promise.reject(error)
})

axios.interceptors.response.use(response => {
  /* 检测某种状态进行重定向
  if (response.status === 302) {
    Router.push({
      name: 'home'
    })
  } */
  return response
}, error => {
  return Promise.resolve(error.response)
})

const checkStatus = response => {
  if (response && (response.status === 200 || response.status === 304 || response.status === 400)) {
    return response.data
  }
  return new Error('service status error')
}

function IsInArray (val) {
  // val.replace('/', '')
  let arr = ['/SystemMaintenace', '/ErrorPage']
  return arr.includes(val)
}

// function checkCode (res) {
//   if (res.code === 60001002) { // user not login
//     let pathName = window.location.pathname
//     if (IsInArray(pathName)) pathName = '/logged'
//     let origin = window.location.origin
//     if (window.location.port === '') origin = origin + ':443'
//     let service = encodeURIComponent(origin + '/ywpt/redirect' + pathName)
//     window.location.href = CASHOST + '?service=' + service
//   } else if (res.code !== 0) {
//     if (/[\u4e00-\u9fa5]/.test(res.message) && res.message.length < 100) {
//       Message.error(res.message)
//     } else {
//       Message.error('操作失败，请稍后再试或联系管理员')
//     }
//   }
//   return res
// }

export default {
  post (url, data, herders, cancel) {
    return axios({
      method: 'post',
      baseURL: UNIFIEDPATH,
      url,
      data: data,
      timeout: 60000,
      headers: {
        ...herders,
        ...developToken
      },
      cancelToken: new CancelToken(function (c) {
        if (cancel) {
          cancel(c)
        }
      })
    }).then(
      (response) => {
        return checkStatus(response)
      }
    )
    // .then(
    //   (res) => {
    //     return checkCode(res)
    //   }
    // )
  },
  get (url, params, herders, cancel) {
    return axios({
      method: 'get',
      baseURL: UNIFIEDPATH,
      url,
      params, // get 请求时带的参数
      timeout: 60000,
      headers: {
        ...herders,
        ...developToken
      },
      cancelToken: new CancelToken(function (c) {
        if (cancel) {
          cancel(c)
        }
      })
    }).then(
      (response) => {
        return checkStatus(response)
      }
    )
    // .then(
    //   (res) => {
    //     return checkCode(res)
    //   }
    // )
  },
  put (url, data, herders, cancel) {
    return axios({
      method: 'put',
      baseURL: UNIFIEDPATH,
      url,
      data,
      timeout: 60000,
      headers: {
        ...herders,
        ...developToken
      },
      cancelToken: new CancelToken(function (c) {
        if (cancel) {
          cancel(c)
        }
      })
    }).then(response => {
      return checkStatus(response)
    })
    // .then(res => {
    //   return checkCode(res)
    // })
  },
  delete (url, params, herders, cancel) {
    return axios({
      method: 'delete',
      baseURL: UNIFIEDPATH,
      url,
      params,
      data: params,
      timeout: 60000,
      headers: {
        ...herders,
        ...developToken
      },
      cancelToken: new CancelToken(function (c) {
        if (cancel) {
          cancel(c)
        }
      })
    }).then(
      (response) => {
        return checkStatus(response)
      }
    )
    // .then(
    //   (res) => {
    //     return checkCode(res)
    //   }
    // )
  }
}
