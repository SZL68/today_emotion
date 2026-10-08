Page({
  data: {
    report: null
  },

  onLoad() {
    const report = wx.getStorageSync('latestReport')
    this.setData({ report })
  },

  backHome() {
    wx.navigateBack({ delta: 1 })
  },

  goHistory() {
    wx.redirectTo({ url: '/pages/history/history' })
  }
})
