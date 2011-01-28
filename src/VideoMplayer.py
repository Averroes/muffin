# -*- encoding: utf-8 -*-
'''
Created on 6/12/2010

@author: erunamo
'''
import wx
import os
import MplayerCtrl as mpc

#----Variables globales----
if os.name == 'nt':
    mplayer_path=u"mplayer.exe"
else:
    mplayer_path=u"mplayer"
    #mpc.VO_DRIVER=mpc.VO_DRIVER,"gl,"

class VideoMplayer(mpc.MplayerCtrl):
    '''
    VideoMplayer es la clase encargada de hacer el wx.Panel que
    lleva el Mplayer. Contiene metodos para interactuar con él.
    '''
    
    def __init__(self,parent, _sliderVideo=None):
        '''
        Recibe al padre para contruir el wx.Panel, y 
        el Slider de la posición del video.
        '''
        self.padre, self.sliderVideo = parent, _sliderVideo
        mpc.MplayerCtrl.__init__(self, self.padre, -1, mplayer_path, mplayer_args=("-ass"," -osdlevel 3 ",) )


    def __openVideo(self, video_path2):
        '''
        Abre el video cargado, y lo manda a reproducir.
        '''
        if self.process_alive :
            self.onStopVideo(wx.Event)
        self.video_path=video_path2
    
        try:
            self.__start()
            #video_mplayer_panel.Loadfile(video_path)
        except UnicodeDecodeError:
            print ('error de Unicode (en teoría, no debería pasar)')
        except mpc.BuildProcessError:
            print ("¡¡¡ERROR FATAL, Mplayer NO ENCONTRADO, no puede mostrarse el video!!!")
    
        return
    
    
    def __start(self):
        '''
        Empieza a reproducir el último video cargado.
        '''
        self.Start(self.video_path, (u"",) )
        print ("& Abriendo: "+ self.video_path)
        self.Osd(2)
        self.sliderVideo.SetValue(0)
        
        
    #============Manejo de eventos==============
    #---Eventos de carga---
    
    def onLoadFile(self, event):
        '''
        Cargador de archivos de video.
        '''
        dlg = wx.FileDialog(None, message="Seleccione un archivo de video",
                            defaultDir=os.getcwd(), defaultFile="",
                            style=wx.OPEN | wx.CHANGE_DIR )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            path = path.replace('\\','/')
            #path = path.encode(sys.getfilesystemencoding())#MplayerCtrl0.3.0 no lo necesita
            self.__openVideo(path)
            dlg.Destroy()
            
    
    def onLoadSub(self, event):
        '''
        Evento que carga los subtitulos .ass de un video.
        '''
        self.onStopVideo(event)
        self.Start(self.video_path, (u"-ass",) )
        print ("→Subtitulo activado (si lo hay)←")
        self.Osd(2)
    
    
    #---Eventos de reproduccion del video---
    
    def onPlayVideo(self, event):
        if not self.process_alive :
            print ("¡¡no hay proceso de Mplayer!!")
            self.__start()    
        else:
            self.Pause()#despausa
            
    
    def onStopVideo(self, event):
        while not self.Quit():
            pass
        print ("# Video Detenido")
            
    
    def onAdvanceVideo(self, event, time=5):
        self.Seek(str(time))
    
    def onBackVideo(self, event, time=-5):
        self.Seek(str(time))
        
        
    def onKeyPuase(self, event):
        #print event.GetKeyCode()
        if event.GetKeyCode() == 27:#tecla ESC
            #print ("**Pausa, tecla ESC desapretada...**")
            self.onPlayVideo(event)
        elif event.GetKeyCode() == 340:#tecla F1
            self.onBackVideo(event)
        elif event.GetKeyCode() == 341:#tecla F2
            self.onAdvanceVideo(event)
        else:
            event.Skip()
            
    #-----Eventos Slider-----
    def setPos(self, event):
        self.Seek(self.sliderVideo.GetValue(), 1)#1=porcentaje
    
    def getPos(self, event):
        #sliderVideo.SetValue( video_mplayer_panel.GetProperty('percent_pos') ) 
        pass
