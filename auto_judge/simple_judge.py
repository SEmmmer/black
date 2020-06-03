import wx


class UserFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(UserFrame, self).__init__(*args, **kwargs)

        panel = wx.Panel(self)

        welcome_text = wx.StaticText(panel, label="直播弹幕管理")
        font = welcome_text.GetFont()
        font.PointSize += 5
        font = font.Bold()
        welcome_text.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(welcome_text, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        panel.SetSizer(sizer)

        self.menu_bar()
        self.CreateStatusBar()
        self.SetStatusText("")
        self.danmaku_field()

    def menu_bar(self):
        file_menu = wx.Menu()
        cookies_item = file_menu.Append(-1,
                                        "加载Cookies",
                                        "加载浏览器保存的Cookies")
        danmaku_load_item = file_menu.Append(-1,
                                             "载入弹幕",
                                             "加载某次直播的弹幕")
        danmaku_save_item = file_menu.Append(-1,
                                             "抓取弹幕",
                                             "从现在开始捕捉某个房间的弹幕")
        file_menu.AppendSeparator()
        exit_item = file_menu.Append(wx.ID_EXIT)

        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT)

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(help_menu, "&Help")
        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self.exit, exit_item)
        self.Bind(wx.EVT_MENU, self.about, about_item)

    def danmaku_field(self):
        confirm = wx.Button(self, label="&鲨了他ud5tdi76r7i6uyhfi\tCtrl-K")
        confirm_pt = wx.Point(150, 150)
        confirm.SetPosition(confirm_pt)
        confirm.Show()

    def using(self, event):
        wx.MessageBox("")

    def exit(self, event):
        self.Close(True)

    def about(self, event):
        wx.MessageBox("作者：Shirakami Emmmer",
                      "直播弹幕管理机",
                      wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
    application = wx.App()
    frame = UserFrame(None, title="Hello")
    frame.Show()
    application.MainLoop()
