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
#import threading, time

#----Variables globales----
if os.name == 'nt':
    mplayer_path=u"mplayer.exe"
else:
    mplayer_path=u"mplayer"
    mpc.AO_DRIVER="oss,"+mpc.AO_DRIVER


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
        self.__valorOSD=2
        self.pausado=True#comienza pausado
        mpc.MplayerCtrl.__init__(self, self.padre, -1, mplayer_path)#, mplayer_args=("-ass"," -osdlevel 3 ",) )
        #self.sDaem=sliderDaemon(self.sliderVideo, self)#BUGGG!!
        
        
    def __openVideo(self, video_path2):
        '''
        Abre el video cargado, y lo manda a reproducir.
        '''
        if self.process_alive :
            self.onStopVideo(wx.Event)
        self.video_path=video_path2
        
        try:
            self.__start()
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
    
        #self.pausado, self.sDaem.pausa=False, False
        self.Start(self.video_path, _argumentos )
        print (u"& Abriendo: "+ self.video_path)
        self.sliderVideo.SetValue(0)
        self.__volumen=100
        self.Osd( self.__valorOSD )#2 por defecto
        
        
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
            #path = path.encode(sys.getfilesystemencoding())#MplayerCtrl0.3.0 no lo necesita
            self.__openVideo( path.replace(u'\\',u'/')  )  
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
            self.setSlider()
            #self.pausado, self.sDaem.pausa = not self.pausado, not self.pausado
            self.Pause()#despausa
            #print ('pausa')
            
    
    def onStopVideo(self, event):
        while not self.Quit():
            pass
        print (u"# Video Detenido")
            
    
    def onAdvanceVideo(self, event, time=5):
        self.Seek(unicode(time))
        self.setSlider()
    
    def onBackVideo(self, event, time=-5):
        self.Seek(unicode(time))
        self.setSlider()
        
        
    def onKeyPuase(self, event):
        '''
        Manejo de reproducción del video desde el teclado.
        '''
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
        '''
        Cambia la posición del video cuando se selecciona el slider.
        '''
        try:
            self.Seek(self.sliderVideo.GetValue(), 1)#1=porcentaje
        except:
            pass
    
    def setOSD(self, event):
        '''
        sirve para quitar el tiempo en el video.
        '''
        self.__valorOSD = 1 if(self.__valorOSD==2)else 2
        self.Osd( self.__valorOSD )
        
    def setSlider(self):
        self.sliderVideo.SetValue( int( self.GetPercentPos() ) )
        
        
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
            
         
"""
#OJO, ESTO LO DEJO COMO HISTORIA, PERO YA NO LO ESTOY USANDO

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
        self.pausa=True
        self.start()        
        
    def run(self):
        '''
        Inicia es con self.start(), si el video
        está pausado, no hace nada [Fix "saltitos"]. 
        '''
        while True :
            try:
                time.sleep(1)
                if not self.pausa:#salta si está pausado.
                    try:
                        self.__slider.SetValue( int( self.__video.GetPercentPos() ) )                    
                    except TypeError:
                        self.__slider.SetValue( 0 )
                    except:
                        pass
            except:
                pass
                
"""