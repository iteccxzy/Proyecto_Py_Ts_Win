import wx
from connect import *


class Edit_ts(wx.Dialog):
    def __init__(self, parent, title):
        super(Edit_ts, self).__init__(parent, title=title, size=(600, 400))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel2 = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        # insertar fecha------------------------------------------------

        self.fecha2 = wx.StaticText(panel2, wx.ID_ANY, "ingrese la fecha")
        hbox1.Add(self.fecha2, 0, wx.LEFT, 20)

        self.text_fecha = wx.TextCtrl(panel2, wx.ID_ANY, "fecha de la tutoria")

        hbox1.AddStretchSpacer(1)
        hbox1.Add(self.text_fecha, 0, wx.RIGHT, 20)

        vbox.Add(hbox1, 1, wx.ALL | wx.EXPAND)

        # botones cancelar------------------------------------------------

        self.botonCancel = wx.Button(panel2, -1, 'Cancelar')

        hbox2.Add(self.botonCancel, 0, wx.LEFT, 30)

        self.botonCancel.Bind(wx.EVT_BUTTON, self.onClose)

        self.botonBuscar = wx.Button(panel2, -1, 'Buscar')

        hbox2.AddStretchSpacer(1)
        hbox2.Add(self.botonBuscar, 0, wx.RIGHT, 30)

        self.botonBuscar.Bind(wx.EVT_BUTTON, self.onClick)

        vbox.Add(hbox2, 1, wx.ALL | wx.EXPAND)

        # buscar y eliminar--------------------------------------

        self.id_ = wx.StaticText(
            panel2, wx.ID_ANY, "ingrese nuevos datos")
        hbox3.Add(self.id_, 0, wx.LEFT, 5)

        self.text_Fe = wx.TextCtrl(panel2, wx.ID_ANY, "nueva fecha ")

        hbox3.Add(self.text_Fe, 0, wx.LEFT, 5)

        self.text_Ho = wx.TextCtrl(panel2, wx.ID_ANY, "nueva hora")

        hbox3.Add(self.text_Ho, 0, wx.RIGHT, 5)

        self.text_T_id = wx.TextCtrl(panel2, wx.ID_ANY, "nueva Id")

        hbox3.Add(self.text_T_id, 0, wx.RIGHT, 5)

        self.botonGuardar = wx.Button(panel2, -1, 'Guardar')

        hbox3.Add(self.botonGuardar, 0, wx.RIGHT, 5)

        self.botonGuardar.Bind(wx.EVT_BUTTON, self.onClickGuardar)

        vbox.Add(hbox3, 1, wx.ALL | wx.EXPAND)

        # grilla

        self.planilla = wx.grid.Grid(panel2, -1)

        self.planilla.CreateGrid(10, 8)

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

        panel2.SetSizer(vbox)

        # metodos

    def onClose(self, event):
        self.Close()

    def ShowMessage(self):
        wx.MessageBox('los datos se guardaron correctamente', 'Info',
                      wx.OK | wx.ICON_INFORMATION)

    def onClick(self, event):
        # self.planilla.Show(True)

        m = self.text_fecha.GetValue()

        result = consulta_busqueda_ts(m)

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

            # self.planilla.EnableEditing(True)

    def onClickGuardar(self, event):

        a = self.text_Fe.GetValue()
        b = self.text_Ho.GetValue()
        c = self.text_T_id.GetValue()

        consulta_edit(a, b, c)

        wx.CallLater(300, self.ShowMessage)

        self.Close()
