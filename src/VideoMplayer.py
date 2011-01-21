# -*- encoding: utf-8 -*-
'''
Created on 6/12/2010

@author: erunamo
'''
import wx
import os, sys
import MplayerCtrl as mpc

#----Variables globales----
if os.name == 'nt':
    mplayer_path="mplayer.exe"
else:
    mplayer_path="mplayer"
    mpc.VO_DRIVER="gl,"+mpc.VO_DRIVER


def initVideo(parent):
    global video_mplayer_panel
    global padre
    padre=parent
    video_mplayer_panel=mpc.MplayerCtrl(padre, -1, mplayer_path)
    return video_mplayer_panel


def __openVideo(video_path2):
    global video_path
    video_path=video_path2
    print video_path
    try:
        video_mplayer_panel.Start(video_path)#, ("-cache-min 20",) )
        video_mplayer_panel.Loadfile(video_path)
        #video_mplayer_panel.FrameDrop(0)
    except UnicodeDecodeError:
        #Gestiona el error del unicode2ascii (not in range(128) )
        onStopVideo(wx.EVT_ACTIVATE)
        onPlayVideo(wx.EVT_ACTIVATE)
        
    return


#============Manejo de eventos==============
#---Eventos de carga---

def onLoadFile(event):
    dlg = wx.FileDialog(None, message=u"Seleccione un archivo de video",
                        defaultDir=os.getcwd(), defaultFile="",
                        style=wx.OPEN | wx.CHANGE_DIR )
    if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
        path = path.replace('\\','/')
        path = path.encode(sys.getfilesystemencoding())
        __openVideo(path)
        dlg.Destroy()
        

def onLoadSub(event):
    print u"cargando sub?"
    onStopVideo(event)
    video_mplayer_panel.Start(video_path, ("-ass",) )
    #video_mplayer_panel.SubSource('2')
    print mpc.VO_DRIVER
    if video_mplayer_panel.GetSubVisibility():
        print u"Activado"
    else:
        print u"No activado"
        
        

#---Eventos de reproduccion del video---

def onPlayVideo(event):
    if not video_mplayer_panel.process_alive :
        print u"¡¡no hay proceso de Mplayer!!"
        print video_path
        video_mplayer_panel.Start(video_path)    
    else:
        print u">>pausa/play normal"
        video_mplayer_panel.Pause()#despausa
        

def onStopVideo(event):
    #playing=video_mplayer_panel.playing
    #if video_mplayer_panel.playing :
        #video_mplayer_panel.Stop()
        while not video_mplayer_panel.Quit():
            pass
        print u"#Video Detenido"
        

def onAdvanceVideo(event, time=5):
    video_mplayer_panel.Seek(str(time))

def onBackVideo(event, time=-5):
    video_mplayer_panel.Seek(str(time))
    
    
def onKeyPuase(event):
    #print event.GetKeyCode()
    if event.GetKeyCode() == 27:#tecla ESC
        print u"**Pausa, tecla ESC desapretada...**"
        onPlayVideo(event)
    elif event.GetKeyCode() == 340:#tecla F1
        onBackVideo(event)
    elif event.GetKeyCode() == 341:#tecla F2
        onAdvanceVideo(event)
    else:
        event.Skip()
