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


def initVideo(parent):
    global video_mplayer_panel
    global padre
    padre=parent
    video_mplayer_panel=mpc.MplayerCtrl(parent, -1, mplayer_path)
    return video_mplayer_panel


def __openVideo(video_path2):
    global video_path
    video_path=video_path2
    print video_path
    video_mplayer_panel.Start(video_path)#, ("-cache-min 20",) )
    video_mplayer_panel.Loadfile(video_path)
    #video_mplayer_panel.FrameDrop(0)
    return


#============Manejo de eventos==============
#---Eventos de carga---

def onLoadFile(event):
    dlg = wx.FileDialog(None, message="Seleccione un archivo de video",
                        defaultDir=os.getcwd(), defaultFile="",
                        style=wx.OPEN | wx.CHANGE_DIR )
    if dlg.ShowModal() == wx.ID_OK:
        path = dlg.GetPath()
        path = path.replace('\\','/')
        path = path.encode(sys.getfilesystemencoding())
        __openVideo(path)
        dlg.Destroy()
        

def onLoadSub(event):
    print "cargando sub?"
    onStopVideo(event)
    video_mplayer_panel.Start(video_path, ("-ass",) )
    #video_mplayer_panel.SubSource('2')
    
    if video_mplayer_panel.GetSubVisibility():
        print "Activado"
    else:
        print "no activado"
        
        

#---Eventos de reproduccion del video---

def onPlayVideo(event):
    if not video_mplayer_panel.process_alive :
        print "no hay proceso"
        print video_path
        video_mplayer_panel.Start(video_path)    
    else:
        print ">>pausa/play normal"
        video_mplayer_panel.Pause()#despausa
        

def onStopVideo(event):
    #playing=video_mplayer_panel.playing
    if video_mplayer_panel.playing :
        #video_mplayer_panel.Stop()
        while not video_mplayer_panel.Quit():
            pass
        print "#Video Detenido"
        

def onAdvanceVideo(event):
    video_mplayer_panel.Seek('5')
    

def onBackVideo(event):
    video_mplayer_panel.Seek('-5')
    
    
def onKeyPuase(event):
    if event.AltDown():
        print "tecla CTRL desapretada..."
        onPlayVideo(event)


        
        
        
    
    

    
    
    
    
    