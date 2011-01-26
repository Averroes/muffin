# -*- encoding: utf-8 -*-
'''
Created on 22/01/2011

@author: erunamo
'''
import wx


class DiccionariosTab(wx.Notebook):
    '''
    classdocs
    '''


    def __init__(self, padre):
        '''
        Constructor
        '''
        wx.Notebook.__init__(self, padre, -1, style=0)
        self.__servicios()
        self.AddPage(self.google, self.google.Name) 
        
        
        
        
    def __servicios(self):
        self.google=DiccGenerico(self, "Google")#, nombre metodo de envio y respuesta)
        
        
#------------------
class DiccGenerico(wx.Panel):
    def __init__(self, _padre, _nombre="servicio?"):
        wx.Panel.__init__(self, _padre, -1, name=_nombre)
        
        self.nombre_servicio = wx.StaticText(self, -1, _nombre)
        self.pregunta = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER|wx.TE_CENTRE)
        self.button_enviar = wx.Button(self, -1, "OK")
        self.respuesta = wx.StaticText(self, -1, u"Aquí saldrá la respuesta a su consulta")
        self.conexion = wx.StaticText(self, -1, u"Información de conexión...")
        
        self.__do_layout()
        
        
        
    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.nombre_servicio, 0, 0, 0)
        sizer_1.Add(self.pregunta, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5)
        sizer_1.Add(self.button_enviar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(self.respuesta, 2, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 10)
        sizer_1.Add(self.conexion, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_RIGHT, 2)
        self.SetSizer(sizer_1)
        
    def __eventos(self):
        pass
        
        
        
#------- Funciones consulta de cada servicio.
def GoogleTranslator():
    pass

def WordReference():
    pass

def RAE():
    pass