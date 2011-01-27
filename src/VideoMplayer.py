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


def initVideo(parent, _sliderVideo=None):
    '''
    Recibe al padre para contruir el wx.Panel, y 
    el Slider de la posición del video.
    '''
    global video_mplayer_panel
    global padre, sliderVideo
    padre, sliderVideo = parent, _sliderVideo
    video_mplayer_panel=mpc.MplayerCtrl(padre, -1, mplayer_path, mplayer_args=("-ass"," -osdlevel 3 ",) )
    #video_mplayer_panel.Osd('2')
    return video_mplayer_panel


def __openVideo(video_path2):
    if video_mplayer_panel.process_alive :
        onStopVideo(wx.Event)
    global video_path
    video_path=video_path2
    print ("& Abriendo: "+ video_path)
    try:
        __start()
        #video_mplayer_panel.Start(video_path)#, ("-cache-min 20",) )
        #video_mplayer_panel.Loadfile(video_path)
    except UnicodeDecodeError:
        print ('error de Unicode (en teoría, no debería pasar)')
    except mpc.BuildProcessError:
        print ("¡¡¡ERROR FATAL, Mplayer NO ENCONTRADO, no puede mostrarse el video!!!")

    return

def __start():
    video_mplayer_panel.Start(video_path)
    print ("& Abriendo: "+ video_path)
    video_mplayer_panel.Osd(2)
    #video_mplayer_panel.SetProperty('osdlevel', 2)
    sliderVideo.SetValue(0)
    
    
#============Manejo de eventos==============
#---Eventos de carga---

def onLoadFile(event):
    dlg = wx.FileDialog(None, message="Seleccione un archivo de video",
                        defaultDir=os.getcwd(), defaultFile="",
                        style=wx.OPEN | wx.CHANGE_DIR )
    if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
        path = path.replace('\\','/')
        #path = path.encode(sys.getfilesystemencoding())#MplayerCtrl0.3.0 no lo necesita
        __openVideo(path)
        dlg.Destroy()
        

def onLoadSub(event):
    onStopVideo(event)
    video_mplayer_panel.Start(video_path, (u"-ass",) )
    #print (mpc.VO_DRIVER)
    print ("→Subtitulo activado (si lo hay)←")
    video_mplayer_panel.Osd(2)


#---Eventos de reproduccion del video---

def onPlayVideo(event):
    if not video_mplayer_panel.process_alive :
        print ("¡¡no hay proceso de Mplayer!!")
        
        #video_mplayer_panel.Start(video_path)
        __start()    
    else:
        print (">> pausa/play normal")
        video_mplayer_panel.Pause()#despausa
        

def onStopVideo(event):
    #playing=video_mplayer_panel.playing
    #if video_mplayer_panel.playing :
        #video_mplayer_panel.Stop()
        while not video_mplayer_panel.Quit():
            pass
        print ("# Video Detenido")
        

def onAdvanceVideo(event, time=5):
    video_mplayer_panel.Seek(str(time))

def onBackVideo(event, time=-5):
    video_mplayer_panel.Seek(str(time))
    
    
def onKeyPuase(event):
    #print event.GetKeyCode()
    if event.GetKeyCode() == 27:#tecla ESC
        print ("**Pausa, tecla ESC desapretada...**")
        onPlayVideo(event)
    elif event.GetKeyCode() == 340:#tecla F1
        onBackVideo(event)
    elif event.GetKeyCode() == 341:#tecla F2
        onAdvanceVideo(event)
    else:
        event.Skip()
        
#-----Eventos Slider-----
def setPos(event):
    video_mplayer_panel.Seek(sliderVideo.GetValue(), 1)#1=porcentaje

def getPos(event):
    #sliderVideo.SetValue( int(video_mplayer_panel.GetProperty('percent_pos') ) )
    pass
