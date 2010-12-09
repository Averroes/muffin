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
    video_mplayer_panel=mpc.MplayerCtrl(parent, -1, mplayer_path)
    #video_mplayer_panel.SetDimensions(0,0,320,180)
    return video_mplayer_panel

def __openVideo(video_path2):
    global video_path
    video_path=video_path2
    print video_path
    video_mplayer_panel.Loadfile(video_path)
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

def onLoadSub(event):#Bugea epicamente
    print "cargando sub?"
    
    #video_mplayer_panel.SubDemux('0')
    video_mplayer_panel.Start(video_path, "-ass")
    video_mplayer_panel.SubSource('2')
    #video_mplayer_panel.SetProperty("sub", "0")
    if video_mplayer_panel.GetSubVisibility():
        print "Activado"
    else:
        print "no activado"
        
        

#---Eventos de reproduccion del video---

def onPlayVideo(event):
    proceso=video_mplayer_panel.process_alive
    pausa=video_mplayer_panel.keep_pause
    if proceso == False :
        print "no hay proceso"
        print video_path
        video_mplayer_panel.Start(video_path)
    
    elif pausa == True :
        print "pausa/play normal"
        video_mplayer_panel.Pause()#despausa

def onStopVideo(event):
    playing=video_mplayer_panel.playing
    if playing == True :
        print "Video Parado"
        video_mplayer_panel.Stop()
        video_mplayer_panel.Quit()

def onAdvanceVideo(event):
    video_mplayer_panel.Seek('5')

def onBackVideo(event):
    video_mplayer_panel.Seek('-5')
    
def onKeyPuase(event):
    print "tecla apretada..."
    
    

    
    
    
    
    