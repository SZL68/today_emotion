const { request } = require('../../utils/api')

Page({
  data: {
    emotions: [
      { emoji: '😊', text: '很好' },
      { emoji: '🙂', text: '还不错' },
      { emoji: '😐', text: '一般般' },
      { emoji: '😔', text: '有点累' },
      { emoji: '😭', text: '很糟糕' }
    ],
    selected: 2,
    content: '',
    loading: false
  },

  chooseEmotion(e) {
    this.setData({ selected: e.currentTarget.dataset.index })
  },

  onInput(e) {
    this.setData({ content: e.detail.value })
  },

  async submit() {
    if (!this.data.content.trim()) {
      wx.showToast({ title: '写一点今天发生的事吧', icon: 'none' })
      return
    }

    this.setData({ loading: true })
    const item = this.data.emotions[this.data.selected]

    try {
      const result = await request('/api/emotions/analyze', 'POST', {
        emotion: item.emoji,
        content: this.data.content
      })

      wx.setStorageSync('latestReport', result)
      wx.navigateTo({ url: '/pages/report/report' })
      this.setData({ content: '' })
    } catch (err) {
      wx.showToast({ title: err.message || '提交失败', icon: 'none' })
    } finally {
      this.setData({ loading: false })
    }
  },

  goHistory() {
    wx.navigateTo({ url: '/pages/history/history' })
  }
})
