const app = getApp()

const request = (path, method, data) => {
  return new Promise((resolve, reject) => {
    wx.request({
      url: app.globalData.apiBaseUrl + path,
      method: method || 'GET',
      data: data || {},
      header: { 'content-type': 'application/json' },
      success: (res) => {
        if (res.statusCode >= 200 && res.statusCode < 300) {
          resolve(res.data)
        } else {
          reject(new Error(res.data?.detail || '请求失败'))
        }
      },
      fail: reject
    })
  })
}

module.exports = { request }
