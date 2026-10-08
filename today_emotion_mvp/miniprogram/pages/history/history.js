const { request } = require('../../utils/api')

Page({
  data: {
    streak: 0,
    total: 0,
    records: []
  },

  onShow() {
    this.load()
  },

  async load() {
    try {
      const data = await request('/api/emotions/history')
      this.setData(data)
    } catch (err) {
      wx.showToast({ title: err.message || '加载失败', icon: 'none' })
    }
  }
})
