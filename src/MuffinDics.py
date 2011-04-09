# -*- encoding: utf-8 -*-
'''
Created on 22/01/2011

@author: ErunamoJAZZ
@license: GPLv3
@summary: Muffin Translator, ayudante para la traducción de anime.
@web: http://code.google.com/p/muffin/
'''
import wx
import webbrowser as wb
from urllib2 import urlopen, URLError 
from urllib import urlencode#, quote

try:
    import json
except ImportError:
    print(u'Necesitas instalar el paquete python-json')


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
        self.home=wx.StaticText(self, -1, self.faq, name=u"Home")
        self.AddPage(self.home, self.home.Name)
        self.rae=DiccGenerico(self, u"RAE", RAE )#, nombre metodo de envio y respuesta)
        self.AddPage(self.rae, self.rae.Name)
        self.wr=DiccGenerico(self, u"WR", WordReference )#, nombre metodo de envio y respuesta)
        self.AddPage(self.wr, self.wr.Name)
        self.google=DiccGenerico(self, u"Google", GoogleTranslator)#, nombre metodo de envio y respuesta)
        self.AddPage(self.google, self.google.Name) 
        
#------------------
class DiccGenerico(wx.Panel):
    '''
    DiccGenerico es un wx.Panel, que crea un conjunto de widgets genericos,
    su intención es la de funcionar para cualquier tipo de consulta online.
    '''
    def __init__(self, _padre, _nombre=u"servicio?", f_consulta=None):
        '''
        _padre=padre de wx.Panel; _nombre=nombre del servicio; 
        f_consulta= función que hará la consulta en internet.
        '''
        wx.Panel.__init__(self, _padre, -1, name=_nombre)
        
        self.nombre_servicio = wx.StaticText(self, -1, _nombre)
        self.pregunta = wx.TextCtrl(self, -1, u"", style=wx.TE_PROCESS_ENTER|wx.TE_CENTRE)
        self.button_enviar = wx.Button(self, -1, u"OK")
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
        self.func_consulta(self)#warper   thread.start_new_thread(self.func_consulta, self ) #
        
        
#------- Funciones consulta de cada servicio.
def GoogleTranslator(objeto):
    ''' 
    El parametro "objeto", se refiere a un objeto tipo 
    DiccGenerico(), con eso se tiene acceso a las partes 
    internas de este, para tomar y modificar los 
    resultados en pantalla. 
    De google solo traduce máximo 5 palabras (para evitar
    su uso excesivo por perrys).
    @note: http://code.google.com/intl/es-CO/apis/language/translate/overview.html
    '''
    #######Copy/paste de algun blog xD
    text=objeto.pregunta.GetValue()
    
    if not text == '':#si no está vacío
        t_aux = text.split()
        text = ' '.join(t_aux[:5])#restricción de 5 palabras.
        
        lang1, lang2 ='en', 'es'
        langpair = '%s|%s'%(lang1,lang2)
        base_url = 'http://ajax.googleapis.com/ajax/services/language/translate?'
        params = urlencode( (('v',1.0),
                            ('q',text),
                            ('langpair',langpair),) )
        url=base_url+params
        try:
            objeto.conexion.SetLabel(u"Conectando...")
            
            content=urlopen(url).read()#falla si no hay internet
            trans_dict=json.loads(content)
        except AttributeError:
            objeto.conexion.SetLabel(u"Error de traducción.")
        except URLError:
            objeto.conexion.SetLabel(u"Falló la conexión")
        else:
            objeto.conexion.SetLabel(u"Finalizado.")
            objeto.respuesta.SetLabel(unicode(text+':\n ->'+trans_dict['responseData']['translatedText']))
    else:#Si está vacío
        objeto.respuesta.SetLabel(u"Aquí saldrá la respuesta a su consulta")


def RAE(objeto):
    ''' 
    El parametro "objeto", se refiere a un objeto tipo 
    DiccGenerico(), con eso se tiene acceso a las partes 
    internas de este, para tomar y modificar los 
    resultados en pantalla. 
    @note: http://rae-quel.appspot.com/
    '''
    objeto.conexion.SetLabel(u"Conectando...")
    
    text=objeto.pregunta.GetValue().lower()#minusculas
    base_url=u'http://rae-quel.appspot.com/w/json/'

    url=base_url+unicode(text) 
    try:
        content=urlopen(url).read()#falla si no hay internet
        trans_dict=json.loads(content)
    except AttributeError:
        objeto.conexion.SetLabel(u"Error de traducción.")
    except URLError:
        objeto.conexion.SetLabel(u"Falló la conexión")
    else:
        comp=text+'\n->'+('\n->'.join(trans_dict))
        
        objeto.respuesta.SetLabel( comp )
        objeto.conexion.SetLabel(u"Finalizado.")

def WordReference(objeto):
    ''' 
    El parametro "objeto", se refiere a un objeto tipo 
    DiccGenerico(), con eso se tiene acceso a las partes 
    internas de este, para tomar y modificar los 
    resultados en pantalla. 
    @note: http://www.wordreference.com/
    '''
    objeto.conexion.SetLabel(u"Conectando...")
    
    text=(objeto.pregunta.GetValue().partition(' ') )
    base_url=u'http://mini.wordreference.com/mini/index.aspx?dict=enes&w='
    url=base_url+unicode(text[0])
    
    objeto.respuesta.SetLabel(u"WordReference\n\nMuffin abrirá la respuesta en \nsu navegador por default.")
    
    if wb.open( url ):
        objeto.conexion.SetLabel(u"Finalizado.")
    else:
        objeto.conexion.SetLabel(u"Falló la conexión")
        

