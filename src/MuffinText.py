# -*- encoding: utf-8 -*-
'''
Created on 15/01/2011

@author: erunamo
'''
import wx
import os#, sys

import threading, time


class MuffinText(wx.TextCtrl):
    '''
    classdocs: Clase encargada del area de texto
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        #Si solo se ha abierto y no se a guardado, permanece falso
        self.esta_guardado=False
        self.path=None
        self.__parent=parent
        
        texto_inicial="""
Actor 1: Well do I understand your speech, yet few strangers do so.
         Why then do you not speak in the Common Tongue,
         as is the custom in the West, if you wish to be answered?
         # TL check: The above seems to be a quote from the lord of the rings, look it up later
Actor 2: What are you babbling about?

NOTA: Use la tecla 'ESC' para pausar y despausar el video.
      Puede usar las teclas F1 y F2 para ir 5 segundos atras o adelante en el video.
      MuffinTranslator ahora tiene sistema de auto-guardado cada 30seg, después de guardar la primer vez.
      #NO OLVIDES REPORTAR LOS ERRORES"""
                
        wx.TextCtrl.__init__(self, self.__parent, -1, texto_inicial, style=wx.TE_MULTILINE|wx.HSCROLL)
        

    def __abrir_texto(self,_path):
        file=open(_path,"rU")
        texto = file.read()
        file.close()
        #self.Create(self.__parent,value=texto, style=wx.TE_MULTILINE|wx.HSCROLL)#NO
        self.SetValue(texto)
        if self.esta_guardado:
            self.hiloGuardado.kill()
            self.hiloGuardado, self.path=None,None
            self.esta_guardado=False
           
        
    def __guardar_texto(self,_doc_path):
        self.path=_doc_path
        self.SaveFile(self.path)#soluciona problema con unicode
        self.SaveFile(self.path+'~')#guarda también un backup
        print (u"»» Archivo guardado correctamente + backup")
        if not self.esta_guardado:
            self.esta_guardado=True
            self.hiloGuardado=AutoGuardado(self)
            self.hiloGuardado.start()
            
        
        
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
                
    #Evento para guardar Archivos
    def onSaveFile(self,event):
            dlg = wx.FileDialog(None, message="Seleccione un archivo de texto",
                                defaultDir=os.getcwd(), defaultFile=".txt",
                                style=wx.SAVE | wx.CHANGE_DIR )
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                self.__guardar_texto( unicode( path.replace('\\','/')  )  )
                dlg.Destroy()
                
    
    
###############################################
########   AUTO-GUARDADO, MULTIHILO   #########
class AutoGuardado(threading.Thread):
    def __init__(self, _wxText):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.__wxText=_wxText
        self.seguir_guardando=self.__wxText.esta_guardado
        
    def run(self):
        
        while True : #si ya se ha guardado
            time.sleep(30)
            if self.seguir_guardando:
                self.__wxText.SaveFile(self.__wxText.path)
                print (u"» Guardado Automatico...(30seg) "+self.getName() )
            else:
                print (self.getName()+" is dead X.x")
                break
    
    def kill(self):
        self.seguir_guardando=False
        print (self.getName()+" pronto... morirá u.u")
        #self.join()

