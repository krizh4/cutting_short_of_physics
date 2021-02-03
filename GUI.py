import wx

class K_Dialog(wx.Dialog):
    def __init__(self, parent, id=-1, title=('Enter values')):
        wx.Dialog.__init__(self, parent, id, title, size=(-1, -1))

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.lable = wx.StaticText(self, label="Enter Mass:")
        self.field = wx.TextCtrl(self, value="", size=(100, 20))
        self.mainSizer.Add(self.lable, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.field, 0, wx.ALL, 8 )

        self.label_v = wx.StaticText(self, label="Enter Velocity:")
        self.field_v = wx.TextCtrl(self, value="", size=(100, 20))
        self.mainSizer.Add(self.label_v, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.field_v, 0, wx.ALL, 8 )

        self.okbutton = wx.Button(self, label="OK", id=wx.ID_OK)
        self.buttonSizer.Add(self.okbutton, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.buttonSizer, 0, wx.ALL, 0)
        self.Bind(wx.EVT_BUTTON, self.onOK, id=wx.ID_OK)
        self.Bind(wx.EVT_TEXT_ENTER, self.onOK)

        self.SetSizer(self.mainSizer)

    def onOK(self, event):
        try:
            self.mass = self.field.GetValue()
            self.velocity = self.field_v.GetValue()
            x = 1 / 2 * float(self.mass) * float(self.velocity) ** 2
            self.result = (f"{x} J")
            self.Destroy()
        except:
            self.Destroy()

    def onCancel(self, event):
        self.result = None
        self.Destroy()

    '''def K_ansr(self):
        x = 1 / 2 * float(self.mass) * float(self.velocity) ** 2
        self.result = x
        print(f"{x} J")'''

class frm(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(-1, -1))
        self.panel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.btn = wx.Button(self.panel, -1, "kinetic power")
        self.Bind(wx.EVT_BUTTON, self.GetAns, self.btn)
        self.txt =wx.TextCtrl(self.panel, -1, size=(140, -1))
        self.txt.SetValue('Ans Goes Here')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.btn)
        sizer.Add(self.txt)
        self.panel.SetSizer(sizer)
        self.Show()

    def GetAns(self, e):
        dlg = K_Dialog(self)
        dlg.ShowModal()
        self.txt.SetValue(dlg.result)

    def OnCloseWindow(self, e):
        self.Destroy
        
app = wx.App()
frame = frm(None, 'phy6')
app.MainLoop()
