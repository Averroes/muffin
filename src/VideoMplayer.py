# -*- encoding: utf-8 -*-
'''
Created on 6/12/2010

@author: ErunamoJAZZ
@license: GPLv3
@summary: Muffin Translator, ayudante para la traducción de anime.
@web: http://code.google.com/p/muffin/ 
'''
import wx
import os
import MplayerCtrl as mpc
import threading, time

#----Variables globales----
if os.name == 'nt':
    mplayer_path=u"mplayer.exe"
    mpc.AO_DRIVER="dsound,"
else:
    mplayer_path=u"mplayer"
    #mpc.VO_DRIVER="sdl,",mpc.VO_DRIVER,"gl,"
    mpc.AO_DRIVER="oss,"

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
        self.__volumen=100
        mpc.MplayerCtrl.__init__(self, self.padre, -1, mplayer_path)#, mplayer_args=("-ass"," -osdlevel 3 ",) )
        self.sDaem=sliderDaemon(self.sliderVideo, self)
        
        


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
            print (u'error de Unicode (en teoría, no debería pasar)')
        except mpc.BuildProcessError:
            print (u"¡¡¡ERROR FATAL, Mplayer NO ENCONTRADO, no puede mostrarse el video!!!")
    
        return
    
    
    def __start(self, _argumentos=(u"",) ):
        '''
        Empieza a reproducir el último video cargado.
        Puede recibir argumentos como una tupla. 
        ¡¡OJO!!: si el OSD no funciona, revisar si tiene 
        un font asignado (más que todo en windows).
        '''
        try:
            self.Start(self.video_path, _argumentos )
            print (u"& Abriendo: "+ self.video_path)
            self.sliderVideo.SetValue(0)
            self.__volumen=100
            #self.Loadfile(self.video_path)
            self.Osd(2)
            
        except:
            print(u"Error en __start (al comenzar reproducción)")
        
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
            #path = path.replace('\\','/')
            #path = path.encode(sys.getfilesystemencoding())#MplayerCtrl0.3.0 no lo necesita
            self.__openVideo(unicode( path.replace('\\','/')  )  )
            dlg.Destroy()
            
    
    def onLoadSub(self, event):
        '''
        Evento que carga los subtitulos .ass de un video.
        '''
        self.onStopVideo(event)
        self.__start(_argumentos=(u"-ass",) )
        print (u">> Subtítulo .ASS con estilos, activado (si lo hay) <<")
    
    
    #---Eventos de reproduccion del video---
    
    def onPlayVideo(self, event):
        if not self.process_alive :
            print (u"¡¡no hay proceso de Mplayer!!")
            self.__start()    
        else:
            self.Pause()#despausa
            #print ('pausa')
            
    
    def onStopVideo(self, event):
        while not self.Quit():
            pass
        print (u"# Video Detenido")
            
    
    def onAdvanceVideo(self, event, time=5):
        self.Seek(str(time))
    
    def onBackVideo(self, event, time=-5):
        self.Seek(str(time))
        
        
    def onKeyPuase(self, event):
        #print event.GetKeyCode()
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            #print ("**Pausa, tecla ESC desapretada...**")
            self.onPlayVideo(event)
        elif event.GetKeyCode() == wx.WXK_F1:
            self.onBackVideo(event)
        elif event.GetKeyCode() == wx.WXK_F2:#tecla F2
            self.onAdvanceVideo(event)
        else:
            event.Skip()
            
    #-----Eventos Slider-----
    def setPos(self, event):
        try:
            self.Seek(self.sliderVideo.GetValue(), 1)#1=porcentaje
        except:
            pass
      
        
        
    #----Eventos Slider Audio
    def volUp(self, event):
        if self.__volumen < 100:
            self.__volumen= self.__volumen+10
            self.SetProperty('volume', float(self.__volumen))
        else:
            self.OsdShowText('Max vol', 1)
            print ('Max vol')
        
    def volDown(self, event):
        if self.__volumen > 0:
            self.__volumen= self.__volumen-10
            self.SetProperty('volume', float(self.__volumen))
        else:
            self.OsdShowText('Min vol', 1)
            print ('Min vol')
         
         

#---Daemon del slider del video----
class sliderDaemon(threading.Thread):
    '''
    Daemon que actualiza la posición del silider 
    del video todo el tiempo.
    '''
    def __init__(self, _slider, _video):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.__slider=_slider
        self.__video=_video
        self.start()        
        
    def run(self):
        '''
        Inicia es con self.start()
        '''
        while True :
            time.sleep(1)
            try:
                self.__slider.SetValue( int( self.__video.GetPercentPos() ) )
            except TypeError:
                self.__slider.SetValue( 0 )
            except:
                pass
