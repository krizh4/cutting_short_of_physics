import wx

class K_Dialog(wx.Dialog):
    def __init__(self, parent, id=-1, title=('KineticEnergy; Enter values')):
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

class P_Dialog(wx.Dialog):
    def __init__(self, parent, id=-1, title=('PotentialEnergy; Enter values')):
        wx.Dialog.__init__(self, parent, id, title, size=(-1, -1))

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.lable = wx.StaticText(self, label="Enter Mass:")
        self.field = wx.TextCtrl(self, value="", size=(100, 20))
        self.mainSizer.Add(self.lable, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.field, 0, wx.ALL, 8 )

        self.label_h = wx.StaticText(self, label="Enter height:")
        self.field_h = wx.TextCtrl(self, value="", size=(100, 20))
        self.mainSizer.Add(self.label_h, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.field_h, 0, wx.ALL, 8 )

        self.label_g = wx.StaticText(self, label="Enter gravity:")
        self.field_g = wx.TextCtrl(self, value="", size=(100, 20))
        self.mainSizer.Add(self.label_g, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.field_g, 0, wx.ALL, 8 )

        self.okbutton = wx.Button(self, label="OK", id=wx.ID_OK)
        self.buttonSizer.Add(self.okbutton, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.buttonSizer, 0, wx.ALL, 0)
        self.Bind(wx.EVT_BUTTON, self.onOK, id=wx.ID_OK)
        self.Bind(wx.EVT_TEXT_ENTER, self.onOK)

        self.SetSizer(self.mainSizer)

    def onOK(self, event):
        try:
            self.mass = self.field.GetValue()
            self.height = self.field_h.GetValue()
            self.gravity = self.field_g.GetValue()
            z = float(self.mass) * float(self.height) * float(self.gravity)
            self.result = (f"{z} J")
            self.Destroy()
        except ValueError:
            self.Destroy()
            

    def onCancel(self, event):
        self.result = None
        self.Destroy()
        
class frm(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(-1, -1))
        self.panel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        #Kinetic  Button
        self.btn = wx.Button(self.panel, -1, "kinetic energy")
        self.Bind(wx.EVT_BUTTON, self.GetAns, self.btn)
        self.txt =wx.TextCtrl(self.panel, -1, size=(140, -1))
        self.txt.SetValue('Ans Goes Here')
        #Potential Energy Button
        self.btnP = wx.Button(self.panel, -1, "potential energy")
        self.Bind(wx.EVT_BUTTON, self.GetAnsP, self.btnP)
        self.txtP = wx.TextCtrl(self.panel, -1, size=(140, -1))
        self.txtP.SetValue('Ans Goes Here')
        #mass pressure button
        self.btnM = wx.Button(self.panel, -1, "mass pressure")
        self.Bind(wx.EVT_BUTTON, self.GetAnsM, self.btnM)
        self.txtM = wx.TextCtrl(self.panel, -1, size=(140, -1))
        self.txtM.SetValue('Ans Goes Here')

        self.btn.SetPosition((5, 5))
        self.txt.SetPosition((5, 30))
        self.btnP.SetPosition((200, 5))
        self.txtP.SetPosition((200, 30))
        self.btnM.SetPosition((5, 60))
        self.txtM.SetPosition((5, 85))
        
        #added menu bar
        self.makeMenuBar()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.btn)
        sizer.Add(self.txt)
        
        self.panel.SetSizer(sizer)
        self.Show()
    
    #functions for menubar
    def makeMenuBar(self):
        typesMenu = wx.Menu()
        kineticEnergyItem = typesMenu.Append(-1, "&Kinetic_Energy...\tCtrl-K", "Help string shown in status bar for this menu item")
        potentialEnergyItem = typesMenu.Append(-1, "&Potential_Energy...\tCtrl-P", "Help string shown in status bar for this menu item")
        massPressureItem = typesMenu.Append(-1, "&Mass_Pressure...\tCtrl-M", "Help string shown in status bar for this menu item")
        exitItem = typesMenu.Append(wx.ID_EXIT)

        menuBar = wx.MenuBar()
        menuBar.Append(typesMenu, "&type")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnKinetic, kineticEnergyItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnPotential, potentialEnergyItem)
        self.Bind(wx.EVT_MENU, self.OnMass, massPressureItem)

    def OnExit(self, event):
        self.Close(True)

    def OnKinetic(self, event):
        self.GetAnsK(True)
    
    def OnPotential(self, event):
        self.GetAnsP(True)

    def OnMass(self, event):
        self.GetAnsM(True)
        
    def GetAns(self, e):
        dlg = K_Dialog(self)
        dlg.ShowModal()
        try:
            self.txt.SetValue(dlg.result)
        except AttributeError:
            print("Error: Please Add Values Correctly")

    def GetAnsP(self, e):
        dlgp = P_Dialog(self)
        dlgp.ShowModal()
        try:
            self.txtP.SetValue(dlgp.result)
        except AttributeError:
            print("Error: Please Add Values Correctly")

    def GetAnsM(self, e):
        wx.MessageBox("Hello, Working on Mass Pressure")
        #commented cuz Working on
        '''dlgm = M_Dialog(self)
        dlgm.ShowModal()
        try:
            self.txtM.SetValue(dlgb.result)
        except: AttributeError:
            print("Error: Please Add Values Correctly")'''

    def OnCloseWindow(self, e):
        self.Destroy()
        
app = wx.App()
frame = frm(None, title='phy6 Calc')
app.MainLoop()
