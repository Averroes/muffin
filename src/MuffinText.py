# -*- encoding: utf-8 -*-
'''
Created on 15/01/2011

@author: erunamo
'''
import wx
import os#, sys

class MuffinText(wx.TextCtrl):
    '''
    classdocs: Clase encargada del area de texto
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        #es nuevo,si se abre otro, cambia a falso 
        self.tipo_nuevo=True 
        #Si no se a guardado, permanece falso
        self.esta_guardado=False
        
        texto_inicial="""
Actor 1: Well do I understand your speech, yet few strangers do so.
         Why then do you not speak in the Common Tongue,
         as is the custom in the West, if you wish to be answered?
         # TL check: The above seems to be a quote from the lord of the rings, look it up later
Actor 2: What are you babbling about?

NOTA: Use la tecla 'ESC' para pausar y despausar el video.
      Puede usar las teclas F1 y F2 para ir 5 segundos atras o adelante en el video
      #NO OLVIDES REPORTAR LOS ERRORES"""
        self.__parent=parent
        
        wx.TextCtrl.__init__(self, parent, -1, texto_inicial, style=wx.TE_MULTILINE|wx.HSCROLL)
        

    def __abrir_texto(self,_path):
        file=open(_path,"rU")
        texto = file.read()
        #self.Create(self.__parent,value=texto, style=wx.TE_MULTILINE|wx.HSCROLL)#NO
        self.SetValue(texto)
        file.close()
           
        
    def __guardar_texto(self,_doc_path):
        #file=open(_doc_path,"w")#sobre-escribe
        #texto=unicode(self.GetString(0, -1))#de 0 a infinito
        #file.write(texto)
        self.SaveFile(_doc_path)#soluciona problema con unicode
        #file.close()
        print u"»» Archivo guardado correctamente"
        
        
    #Evento para abrir Archivos
    def onLoadFile(self, event):
        #if self.tipo_nuevo:
            dlg = wx.FileDialog(None, message=u"Seleccione un archivo de texto",
                                defaultDir=os.getcwd(), defaultFile=".txt",
                                style=wx.OPEN | wx.CHANGE_DIR )
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                path = path.replace('\\','/')
                path = unicode(path)#path.encode(sys.getfilesystemencoding())
                self.__abrir_texto(path)
                dlg.Destroy()
                
    #Evento para guardar Archivos
    def onSaveFile(self,event):
            dlg = wx.FileDialog(None, message=u"Seleccione un archivo de texto",
                                defaultDir=os.getcwd(), defaultFile=".txt",
                                style=wx.SAVE | wx.CHANGE_DIR )
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                path = path.replace('\\','/')
                path = unicode(path)#path.encode(sys.getfilesystemencoding())
                self.__guardar_texto(path)
                dlg.Destroy()
                
    
    
    
    
