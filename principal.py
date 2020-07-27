import wx
import psycopg2
import wx.lib.intctrl
import wx.grid


from connect import *
from Formulario_carga import *
from Edit_ts import *
from Del_ts import *


# Creación de clases para conexión


class VentanaPrincipal(wx.Frame):

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent=parent, title=title, size=(800, 700))

        # Conifgurando  el menu.-------------------------------------------------------------------------------
        
        filemenu = wx.Menu()


        menuAgregar = filemenu.Append(-1, "&Agregar",  " Information about this program")

        menuModificar = filemenu.Append(-1, "Modificar", " Information about this program")

        menuEliminar = filemenu.Append(-1, "Eliminar"," Information about this program")

        filemenu.AppendSeparator()

        menuSalir = filemenu.Append(  -1, "E&xit", " Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&Archivo")
        self.SetMenuBar(menuBar)

        # eventos
        
        self.Bind(wx.EVT_MENU, self.onClick, menuAgregar)
        self.Bind(wx.EVT_MENU, self.onClickDel, menuEliminar)
        self.Bind(wx.EVT_MENU, self.onClickEdit, menuModificar)
        self.Bind(wx.EVT_MENU, self.onClose, menuSalir)



        # conectamos con la base de datos-------------------------------------------
        # -------------------------

        result = consulta_principal()

        # Definimos el panel principal---------------------------------------------------

        panel = wx.Panel(self, -1)

        # Añadimos el la planilla*-

        planilla = wx.grid.Grid(panel, -1)

        # creamos las filas y columnas

        planilla.CreateGrid(len(result), 7)

        planilla.SetColLabelValue(0, 'carrera')

        planilla.SetColLabelValue(1, 'materia')

        planilla.SetColLabelValue(2, 'nombre')

        planilla.SetColLabelValue(3, 'apellido')

        planilla.SetColLabelValue(4, 'fecha')

        planilla.SetColLabelValue(5, 'hora')

        

        planilla.SetColLabelValue(6, 'zoom')

       

        # definimos los tamaños

       # colocar SetRowLabelSize(0) elimina el encabezado de la fila

        planilla.SetRowLabelSize(0)

        planilla.SetColSize(0, 100)

        planilla.SetColSize(1, 150)

        planilla.SetColSize(2, 100)

        planilla.SetColSize(3, 100)

        planilla.SetColSize(4, 100)

        planilla.SetColSize(5, 60)

        planilla.SetColSize(6, 50)

       

    #     attr = wx.grid.GridCellAttr()
    #    attr.SetReadOnly(True)
     #   for i in range(0, len(result)):
      #      planilla.SetRowAttr(i, attr)
        planilla.EnableEditing(False)

        for i in range(0, len(result)):

            # añadimos la primera columna

            planilla.SetCellValue(i, 0, "%s" % result[i][0])

            planilla.SetCellValue(i, 1, "%s" % result[i][1])

            planilla.SetCellValue(i, 2, "%s" % result[i][2])

            planilla.SetCellValue(i, 3, "%s" % result[i][3])

            planilla.SetCellValue(i, 4, "%s" % result[i][4])

            planilla.SetCellValue(i, 5, "%s" % result[i][5])

            planilla.SetCellValue(i, 6, "%s" % result[i][6])

            # planilla.SetCellValue(i, 7, "%s" % result[i][7])

            # planilla.SetCellValue(i, 8, "%s" % result[i][8])

        # Add buttons

        botonCerrar = wx.Button(panel, -1, 'Cerrar')
        botonCerrar.Bind(wx.EVT_BUTTON, self.onClose)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(planilla, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        vbox.Add(botonCerrar, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        panel.SetSizer(vbox)
        self.Centre(True)
        self.Show(True)

       # -----------------------------metodos---------------------------------

    def onClose(self, event):
        self.Close()

    def onClick(self, event):
        self.ventana = FormuTS(self, "Formulario nueva TS")
        self.ventana.ShowModal()
        self.ventana.Destroy()

    def onClickDel (self, event):
        self.ventana_busqueda= Del_ts(self, "buscar ts")
        self.ventana_busqueda.ShowModal()
        self.ventana_busqueda.Destroy()

    def onClickEdit(self, event):
        self.ventana_edit= Edit_ts(self, "edit ts")
        self.ventana_edit.ShowModal()
        self.ventana_edit.Destroy()




app = wx.App()

VentanaPrincipal(None, "mis tutorias")

app.MainLoop()
