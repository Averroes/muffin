# -*- encoding: utf-8 -*-
'''
Created on 15/01/2011

@author: ErunamoJAZZ
@license: GPLv3
@summary: Muffin Translator, ayudante para la traducción de anime.
@web: http://code.google.com/p/muffin/
'''
import wx
import os
import threading, time
import codecs


class MuffinText(wx.TextCtrl):
    '''
    MuffinText: Clase encargada del area de texto.
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        #Si solo se ha abierto y no se a guardado, permanece falso
        self.esta_guardado=False
        self.path=None
        self.__parent=parent
        
        texto_inicial=u"""#(Modelo para traducir)
Actor 1: Well do I understand your speech, yet few strangers do so.
         Why then do you not speak in the Common Tongue,
         as is the custom in the West, if you wish to be answered?
         # TL check: The above seems to be a quote from the lord of the rings, look it up later
Actor 2: What are you babbling about?

NOTA: Use la tecla 'ESC' para pausar y despausar el video.
      Puede usar las teclas F1 y F2 para ir 5 segundos atras o adelante en el video.
      MuffinTranslator ahora tiene sistema de auto-guardado cada 30seg, después de guardar la primer vez.
      #NO OLVIDES REPORTAR LOS ERRORES EN: http://code.google.com/p/muffin/issues/list"""
                
        wx.TextCtrl.__init__(self, self.__parent, -1, texto_inicial, style=wx.TE_MULTILINE|wx.HSCROLL)
        

    def __abrir_texto(self,_path):
        '''
        Abre un texto intentando primero desde utf-8, y
        luego desde Latin-1 (ANSI). Este ultimo abrirá
        mal textos en otras codificaciones, como unicode. 
        '''
        try:
            file= codecs.open(_path, 'rU', 'utf-8')#OJO
            #file=open(_path,"rU")
            texto = file.read()
            print (u'Texto abierto con codificación utf-8')
        except:
            file.close()
            file= codecs.open(_path, 'rU', 'Latin-1')
            texto = file.read()
            print (u'Texto abierto con codificación Latin-1 (ANSI)')

        file.close()
        
        self.SetValue(texto)
        if self.esta_guardado:
            self.hiloGuardado.kill()
            self.hiloGuardado, self.path=None,None
            self.esta_guardado=False
           
        
    def __guardar_texto(self,_doc_path=None):
        '''
        Guarda el texto en un archivo, y hace un backup del mismo.
        '''
        if not _doc_path is None:
            self.path=_doc_path
        if not self.path is None:
            self.SaveFile(self.path)#soluciona problema con unicode
            self.SaveFile(self.path+'~')#guarda también un backup
            print (u"»» Archivo guardado correctamente + backup")
            if not self.esta_guardado:
                self.esta_guardado=True
                self.hiloGuardado=AutoGuardado(self)
                self.hiloGuardado.start()
        
        else:#si no hay path...
            self.onSaveFileWhit(wx.Event)    
        
        
    #Evento para abrir Archivos
    def onLoadFile(self, event):
        #if self.tipo_nuevo:
            dlg = wx.FileDialog(None, message="Seleccione un archivo de texto",
                                defaultDir=os.getcwd(), defaultFile=".txt",
                                style=wx.OPEN | wx.CHANGE_DIR )
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                self.__abrir_texto( unicode( path.replace('\\','/')  )  )
                dlg.Destroy()
                
    #Evento para "Guardar Archivo como..."
    def onSaveFileWhit(self, event):
            dlg = wx.FileDialog(None, message="Guarde como un archivo de texto",
                                defaultDir=os.getcwd(), defaultFile=".txt",
                                style=wx.SAVE | wx.CHANGE_DIR )
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                self.__guardar_texto( unicode( path.replace('\\','/')  )  )
                dlg.Destroy()
                
    def onSaveFile(self, event):
        self.__guardar_texto()
    
###############################################
########   AUTO-GUARDADO, MULTIHILO   #########
class AutoGuardado(threading.Thread):
    '''
    AutoGuardado: Clase que hereda de Therad, y 
    guarda cada cierto tiempo los datos.
    '''
    def __init__(self, _wxText):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.__wxText=_wxText
        self.seguir_guardando=self.__wxText.esta_guardado
        
    def run(self):
        '''
        Inicia Bucle de auto-guardado. 
        '''
        while True : #si ya se ha guardado
            time.sleep(30)
            if self.seguir_guardando:
                self.__wxText.SaveFile(self.__wxText.path)
                print (u"» Guardado Automatico...(30seg) "+self.getName() )
            else:
                print (self.getName()+" is dead X.x")
                break
    
    def kill(self):
        '''
        Hace que el bucle se termine en la proxima iteración.
        '''
        self.seguir_guardando=False
        print (self.getName()+" pronto... morirá u.u")
        #self.join()

