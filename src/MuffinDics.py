# -*- encoding: utf-8 -*-
'''
Created on 22/01/2011

@author: erunamo
'''
import wx

from urllib2 import urlopen
from urllib import urlencode
import sys
try:
    import json
except ImportError:
    print('You need to install the python-json package')


class DiccionariosTab(wx.Notebook):
    '''
    DiccionariosTab construye las pestañas de consulta de diccionarios on-line,
    también se encarga de gestionar los eventos consernientes a ellas.
    '''
    def __init__(self, padre):
        '''
        Constructor. Solo resibe al padre de wx.Notebook().
        '''
        wx.Notebook.__init__(self, padre, -1, style=0)
        self.faq=u"""
 Muffin es un ayudante para la 
 traducción de subtítulos, 
 pensado para los traductores 
 de anime. Muestra en una misma 
 ventana: el video, el área para 
 escribir texto, y la consulta 
 de diccionarios on-line. Esto 
 ahorra valioso tiempo a la hora 
 de traducir, ya que se evita 
 la tediosa tarea de pasar entre
 ventanas por cada línea de 
 traducción, etc."""
        self.__servicios()
        
    def __servicios(self):
        self.home=wx.StaticText(self, -1, self.faq, name='Home')
        self.AddPage(self.home, self.home.Name) 
        self.google=DiccGenerico(self, "Google", GoogleTranslator)#, nombre metodo de envio y respuesta)
        self.AddPage(self.google, self.google.Name) 
        
        
#------------------
class DiccGenerico(wx.Panel):
    '''
    DiccGenerico es un wx.Panel, que crea un conjunto de widgets generico,
    su intención es la de funcionar para cualquier tipo de consulta online.
    '''
    def __init__(self, _padre, _nombre="servicio?", f_consulta=None):
        '''
        _padre=padre de wx.Panel; _nombre=nombre del servici; 
        f_consulta= función que hará la consulta en internet.
        '''
        wx.Panel.__init__(self, _padre, -1, name=_nombre)
        
        self.nombre_servicio = wx.StaticText(self, -1, _nombre)
        self.pregunta = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER|wx.TE_CENTRE)
        self.button_enviar = wx.Button(self, -1, "OK")
        self.respuesta = wx.StaticText(self, -1, u"Aquí saldrá la respuesta a su consulta")
        self.conexion = wx.StaticText(self, -1, u"Información de conexión...")
        self.func_consulta=f_consulta#función que consulta la palabra en internet
        
        self.__do_layout()
        self.__eventos()

        
    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.nombre_servicio, 0, 0, 0)
        sizer_1.Add(self.pregunta, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5)
        sizer_1.Add(self.button_enviar, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(self.respuesta, 2, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 10)
        sizer_1.Add(self.conexion, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_RIGHT, 2)
        self.SetSizer(sizer_1)
        
    def __eventos(self):
        self.button_enviar.Bind(wx.EVT_BUTTON, self.consultor)#
        self.pregunta.Bind(wx.EVT_TEXT_ENTER, self.consultor)
        
    def consultor(self, event):
        '''
        Consultor es un warper para llamar a la función 
        encargada de la consulta en internet.
        '''
        self.func_consulta(self)#warper
        
        
#------- Funciones consulta de cada servicio.
def GoogleTranslator(objeto):
    ''' 
    El parametro "objeto", se refiere a un objeto tipo 
    DiccGenerico(), con eso se tiene acceso a las partes 
    internas de este, para tomar y modificar los 
    resultados en pantalla. 
    '''
    #print ("clic")# prueba xD
    #objeto.respuesta.SetLabel(objeto.pregunta.GetValue())
    #######Copy/paste de algun blog xD
    lang1='en'
    lang2='es'
    langpair='%s|%s'%(lang1,lang2)
    text=objeto.pregunta.GetValue() #' '.join()
    base_url='http://ajax.googleapis.com/ajax/services/language/translate?'
    params=urlencode( (('v',1.0),
                       ('q',text),
                       ('langpair',langpair),) )
    url=base_url+params
    content=urlopen(url).read()
    try:
        trans_dict=json.loads(content)
    except AttributeError:
        #trans_dict=json.read(content)
        print(">> Falló <<")
    #print(trans_dict['responseData']['translatedText'])
    objeto.respuesta.SetLabel(trans_dict['responseData']['translatedText'])
    
    

def WordReference():
    pass

def RAE():
    pass