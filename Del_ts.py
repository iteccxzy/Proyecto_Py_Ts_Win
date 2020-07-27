import wx
from connect import *




class Del_ts(wx.Dialog):
    def __init__(self, parent, title):
        super(Del_ts, self).__init__(parent, title=title, size=(600, 400))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panelcito = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)


        ############ insertar fecha
        
        self.fecha = wx.StaticText(panelcito, wx.ID_ANY, u"fecha")
        hbox1.Add(self.fecha, 0, wx.LEFT, 30)

        self.text_carera = wx.TextCtrl(panelcito, wx.ID_ANY, "ingrese la fecha")
        
        hbox1.AddStretchSpacer(1)
        hbox1.Add(self.text_carera, 0, wx.RIGHT, 30)

        vbox.Add(hbox1, 1, wx.ALL | wx.EXPAND)

        ##botones cancelar
        self.botonCerrar = wx.Button(panelcito, -1, 'Cancelar')

        hbox2.Add(self.botonCerrar, 0, wx.LEFT, 30)

        self.botonCerrar.Bind(wx.EVT_BUTTON, self.onClose)

       


        self.botonBuscar = wx.Button(panelcito, -1, 'Buscar')

        hbox2.AddStretchSpacer(1)
        hbox2.Add(self.botonBuscar, 0, wx.RIGHT, 30)

        self.botonBuscar.Bind(wx.EVT_BUTTON, self.onClick)

        vbox.Add(hbox2, 1, wx.ALL | wx.EXPAND)

        ##### buscar y eliminar

        self.conf_id = wx.StaticText(panelcito, wx.ID_ANY, u"Id")
        hbox3.Add(self.conf_id, 0, wx.LEFT, 30)

        self.text_id = wx.TextCtrl(panelcito, wx.ID_ANY, "ingrese el id")
        
        hbox3.Add(self.text_id, 0, wx.LEFT, 10)


       
        self.botonDel = wx.Button(panelcito, -1, 'eliminar')

        hbox3.Add(self.botonDel, 0, wx.LEFT, 10)

        self.botonDel.Bind(wx.EVT_BUTTON, self.delete)

        vbox.Add(hbox3, 1, wx.ALL | wx.EXPAND)



        ##grilla

        self.planilla = wx.grid.Grid(panelcito, -1)

        self.planilla.CreateGrid( 10, 8)

        self.planilla.SetColLabelValue(0, 'carrera')

        self.planilla.SetColLabelValue(1, 'materia')

        self.planilla.SetColLabelValue(2, 'nombre')

        self.planilla.SetColLabelValue(3, 'apellido')

        self.planilla.SetColLabelValue(4, 'fecha')

        self.planilla.SetColLabelValue(5, 'hora')
   
        self.planilla.SetColLabelValue(6, 'zoom')

        self.planilla.SetColLabelValue(7, 'id')
      

        # definimos los tamaños

        # colocar SetRowLabelSize(0) elimina el encabezado de la fila

        self.planilla.SetRowLabelSize(0)

        self.planilla.SetColSize(0, 70)

        self.planilla.SetColSize(1, 120)

        self.planilla.SetColSize(2, 80)

        self.planilla.SetColSize(3, 70)

        self.planilla.SetColSize(4, 70)

        self.planilla.SetColSize(5, 60)

        self.planilla.SetColSize(6, 60)

        self.planilla.SetColSize(7, 30)

        self.planilla.EnableEditing(False)

      








        vbox.Add(self.planilla, 0, wx.ALIGN_CENTER | wx.ALL, 2)




        panelcito.SetSizer(vbox)


        ##metodos
    def onClose(self, event):
        self.Close()

    def ShowMessage(self):
        wx.MessageBox('los datos se eliminaron correctamente', 'Info',
                      wx.OK | wx.ICON_INFORMATION)

    def onClick(self, event):
        #self.planilla.Show(True)
        
        m= self.text_carera.GetValue()

        result= consulta_busqueda_ts(m)

        for i in range(0, len(result)):

            # añadimos la primera columna
            
            self.planilla.SetCellValue(i, 0, "%s" % result[i][0])
                 
            self.planilla.SetCellValue(i, 1, "%s" % result[i][1])

            self.planilla.SetCellValue(i, 2, "%s" % result[i][2])

            self.planilla.SetCellValue(i, 3, "%s" % result[i][3])

            self.planilla.SetCellValue(i, 4, "%s" % result[i][4])

            self.planilla.SetCellValue(i, 5, "%s" % result[i][5])

            self.planilla.SetCellValue(i, 6, "%s" % result[i][6])

            self.planilla.SetCellValue(i, 7, "%s" % result[i][7])

    def delete(self, event):
        j = self.text_id.GetValue()
        consulta_del_ts(j)


        wx.CallLater(300, self.ShowMessage)

        self.Close()











