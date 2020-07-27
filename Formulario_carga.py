import wx

from connect import *
from datetime import *


class FormuTS(wx.Dialog):
    m = str()

    def __init__(self, parent, title):
        super(FormuTS, self).__init__(parent, title=title, size=(400, 400))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        p = wx.Panel(self)
        comboMateriaChoices = []
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        hbox8 = wx.BoxSizer(wx.HORIZONTAL)


# ---------------label  y combo carrera -----------------------

        self.carrera = wx.StaticText(p, wx.ID_ANY, u"carrera")
        hbox1.Add(self.carrera, 0, wx.LEFT, 30)

        comboCarreraChoices = consulta_carga_ts_carrera()

        self.comboCarrera = wx.ComboBox(
            # p, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, comboCarreraChoices, 0)
            p, wx.ID_ANY, u"", wx.DefaultPosition, (200, 25), comboCarreraChoices, 0)

        self.comboCarrera.Bind(wx.EVT_COMBOBOX, self.OnCombo)

        hbox1.AddStretchSpacer(1)
        hbox1.Add(self.comboCarrera, 0,  wx.RIGHT, 10)

        vbox.Add(hbox1, 1, wx.ALL | wx.EXPAND)
        # ---------------label  y combo  materia --------------------------------------
        self.materia = wx.StaticText(p, wx.ID_ANY, u"materia")
        hbox2.Add(self.materia, 0, wx.LEFT, 30)

        self.comboMateriaChoices = []

        self.comboMateria = wx.ComboBox(
            p, wx.ID_ANY, u"", wx.DefaultPosition, (200, 25), comboMateriaChoices, 0)

        hbox2.AddStretchSpacer(1)
        hbox2.Add(self.comboMateria, 0, wx.RIGHT, 10)

        vbox.Add(hbox2, 1, wx.ALL | wx.EXPAND)

        # ---------------label  y combo docente-----------------------
        self.docente = wx.StaticText(p, wx.ID_ANY, u"docente")
        hbox3.Add(self.docente, 0, wx.LEFT, 30)

        comboDocenteChoices = consulta_carga_ts_docente()

        self.comboDocente = wx.ComboBox(
            p, wx.ID_ANY, u"", wx.DefaultPosition, (200, 25), comboDocenteChoices, 0)

        hbox3.AddStretchSpacer(1)
        hbox3.Add(self.comboDocente, 0, wx.RIGHT, 10)

        vbox.Add(hbox3, 1, wx.ALL | wx.EXPAND)

        # ---------------label  y combo fecha-----------------------
        self.fecha = wx.StaticText(p, wx.ID_ANY, u"fecha")
        hbox4.Add(self.fecha, 0, wx.LEFT, 30)

        self.textFecha = wx.TextCtrl(p, wx.ID_ANY)

        hbox4.AddStretchSpacer(1)
        hbox4.Add(self.textFecha, 0, wx.RIGHT, 10)

        vbox.Add(hbox4, 1, wx.ALL | wx.EXPAND)

        # ---------------label  y combo horarios -----------------------
        self.hora = wx.StaticText(p, wx.ID_ANY, u"hora")
        hbox5.Add(self.hora, 0, wx.LEFT, 30)

        comboHorariosChoices = ['1', '2']
        self.comboHorario = wx.ComboBox(
            p, wx.ID_ANY, u"", wx.DefaultPosition, (200, 25), comboHorariosChoices, 0)

        hbox5.AddStretchSpacer(1)
        hbox5.Add(self.comboHorario, 0, wx.RIGHT, 10)

        vbox.Add(hbox5, 1, wx.ALL | wx.EXPAND)

        # ---------------label  y combo -----------------------
        self.zoom = wx.StaticText(p, wx.ID_ANY, u"zoom")
        hbox6.Add(self.zoom, 0, wx.LEFT, 30)

        comboZoomChoices = ['z', 'z2', 'z3', 'z4',
                            'z5', 'z6', 'z7', 'z8', 'z9', 'z10']

        self.comboZoom = wx.ComboBox(
            p, wx.ID_ANY, u"", wx.DefaultPosition, (200, 25), comboZoomChoices, 0)

        hbox6.AddStretchSpacer(1)
        hbox6.Add(self.comboZoom, 0, wx.RIGHT, 10)

        vbox.Add(hbox6, 1, wx.ALL | wx.EXPAND)

  # ---------------label  y combo -----------------------

        self.bimestre = wx.StaticText(p, wx.ID_ANY, u"bimestre")
        hbox7.Add(self.bimestre, 0, wx.LEFT, 30)

        comboBimestreChoices = consulta_carga_ts_bimestre()

        self.comboBimestre = wx.ComboBox(
            p, wx.ID_ANY, u"", wx.DefaultPosition, (200, 25), comboBimestreChoices, 0)

        hbox7.AddStretchSpacer(1)
        hbox7.Add(self.comboBimestre, 0, wx.RIGHT, 10)

        vbox.Add(hbox7, 1, wx.ALL | wx.EXPAND)

        # ---------------------botones cancelar y aceptar-----------

        self.botonCerrar = wx.Button(p, -1, 'Cancelar')

        hbox8.Add(self.botonCerrar, 0, wx.LEFT, 30)

        self.botonCerrar.Bind(wx.EVT_BUTTON, self.onClose)

        self.botonGuardar = wx.Button(p, -1, 'Guardar')

        hbox8.AddStretchSpacer(1)
        hbox8.Add(self.botonGuardar, 0, wx.RIGHT, 10)

        self.botonGuardar.Bind(wx.EVT_BUTTON, self.onClick)

        vbox.Add(hbox8, 1, wx.ALL | wx.EXPAND)

        # -----------
        p.SetSizer(vbox)

    def ShowMessage(self):
        wx.MessageBox('los datos se guardaron correctamente', 'Info',
                      wx.OK | wx.ICON_INFORMATION)

    def OnCombo(self, event):

        self.m = self.comboCarrera.GetValue()

        self.comboMateriaChoices = consulta_carga_ts_materia(self.m)

        self.comboMateria.SetItems(self.comboMateriaChoices)

    def onClose(self, event):
        self.Close()

    def onClick(self, event):

        _carrera = self.comboCarrera.GetValue()
        _materia = self.comboMateria.GetValue()
        _docente = self.comboDocente.GetValue()
        _hora = self.comboHorario.GetValue()
        _fecha = self.textFecha.GetValue()
        _zoom = self.comboZoom.GetValue()
        _bim = self.comboBimestre.GetValue()

        consulta_guardar_ts(_materia, _carrera, _fecha,
                            _hora, _docente, _bim, _zoom)

        wx.CallLater(300, self.ShowMessage)

        self.Close()
