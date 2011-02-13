# -*- encoding: utf-8 -*-
'''
Created on 6/12/2010

@author: ErunamoJAZZ
@license: GPLv3
@summary: Muffin Translator, ayudante para la traducción de anime.
@web: http://code.google.com/p/muffin/
'''
import wx, os.path
import VideoMplayer
import MuffinText, MuffinDics


class MuffinFrame(wx.Frame):
    '''
    MuffinFrame contiene los datos básicos para construir la ventana 
    de MuffinTranslator con sus partes.
    '''
    def __init__(self, *args, **kwds):
        '''
        Constructor por defecto.
        '''
        # begin wxGlade: MuffinFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panelTexto = wx.Panel(self, -1)
        self.panelDiccionarios = wx.Panel(self, -1)
        self.pestanaDiccionarios = MuffinDics.DiccionariosTab(self.panelDiccionarios)#
        self.panelVideo = wx.Panel(self, -1)
        
        self.texto = MuffinText.MuffinText(self.panelTexto)
        dir = '.'
        
        # Parte del Video
        self.PosicionVideo = wx.Slider(self.panelVideo, -1, 0, 0, 99)
        self.VideoMplayer = VideoMplayer.VideoMplayer(self.panelVideo, self.PosicionVideo) #wx.Panel(self.panelVideo, -1)
        self.botonPlay = wx.BitmapButton(self.panelVideo, -1, 
                                         wx.Bitmap(dir+"/img/play.png", wx.BITMAP_TYPE_ANY))
        self.botonStop = wx.BitmapButton(self.panelVideo, -1, 
                                         wx.Bitmap(dir+"/img/stop.png", wx.BITMAP_TYPE_ANY))
        self.botonAtras = wx.BitmapButton(self.panelVideo, -1, 
                                          wx.Bitmap(dir+"/img/atras.png", wx.BITMAP_TYPE_ANY))
        self.botonAdelante = wx.BitmapButton(self.panelVideo, -1, 
                                             wx.Bitmap(dir+"/img/adelante.png", wx.BITMAP_TYPE_ANY))
        self.volumenUp = wx.BitmapButton(self.panelVideo, -1, 
                                             wx.Bitmap(dir+"/img/vol_up.png", wx.BITMAP_TYPE_ANY))
        self.volumenDown = wx.BitmapButton(self.panelVideo, -1, 
                                             wx.Bitmap(dir+"/img/vol_down.png", wx.BITMAP_TYPE_ANY))
        # Fin Parte del Video
        
        # Menu Bar
        self.Muffin_menubar = wx.MenuBar()
        
        wxglade_tmp_menu = wx.Menu()
        wxAbrirVideo=wxglade_tmp_menu.Append(wx.NewId(), "Abrir video", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.VideoMplayer.onLoadFile, wxAbrirVideo)
        wxAbrirTexto=wxglade_tmp_menu.Append(wx.NewId(), "Abrir texto", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.texto.onLoadFile, wxAbrirTexto)
        wxGuardarTexto=wxglade_tmp_menu.Append(wx.NewId(), "Guardar texto", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.texto.onSaveFile, wxGuardarTexto)
        wxGuardarTexto=wxglade_tmp_menu.Append(wx.NewId(), "Guardar texto como...", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.texto.onSaveFileWhit, wxGuardarTexto)
        self.Muffin_menubar.Append(wxglade_tmp_menu, "Archivo")
        
        wxglade_tmp_menu = wx.Menu()
        wxSubtitulo=wxglade_tmp_menu.Append(wx.NewId(), 
                                            "Cargar Sub del video(MKV)", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.VideoMplayer.onLoadSub, wxSubtitulo)
        self.Muffin_menubar.Append(wxglade_tmp_menu, "Opciones de video")

        wxglade_tmp_menu = wx.Menu()
        wxAbout=wxglade_tmp_menu.Append(wx.NewId(), 
                                            "Acerca de...", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.onAbout, wxAbout)
        #self.Muffin_menubar.Append(wxglade_tmp_menu, "Ayuda")
        #OJO, ESTO SE PONE EN LA VERSIÓN 0.2.0!!!!!
        
        self.SetMenuBar(self.Muffin_menubar)
        
        # Menu Bar end
        
        self.__set_properties()
        self.__do_layout()
        self.__controlEventos()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MuffinFrame.__set_properties
        self.SetTitle("Muffin Translator - Alpha version")
        self.SetSize((800, 600))
        self.SetMinSize((800, 600))
        self.botonPlay.SetSize(self.botonPlay.GetBestSize())
        self.botonStop.SetSize(self.botonStop.GetBestSize())
        self.botonAtras.SetSize(self.botonAtras.GetBestSize())
        self.botonAdelante.SetSize(self.botonAdelante.GetBestSize())
        self.volumenUp.SetSize(self.volumenUp.GetBestSize())
        self.volumenDown.SetSize(self.volumenDown.GetBestSize())
        # end wxGlade

        self.PosicionVideo.SetRange(0,100)# en porcentaje
        self.PosicionVideo.SetValue(0)

    def __do_layout(self):
        # begin wxGlade: MuffinFrame.__do_layout
        contenedorTotal = wx.BoxSizer(wx.VERTICAL)
        contenedorPrincipal = wx.BoxSizer(wx.VERTICAL)
        contenedorTexto = wx.BoxSizer(wx.HORIZONTAL)
        Contenedor1 = wx.BoxSizer(wx.HORIZONTAL)
        contenedorDiccionarios = wx.BoxSizer(wx.HORIZONTAL)
        ContenedorMplayer = wx.BoxSizer(wx.VERTICAL)
        ContenedorControles = wx.BoxSizer(wx.VERTICAL)
        Controles = wx.BoxSizer(wx.HORIZONTAL)
        ContenedorMplayer.Add(self.VideoMplayer, 4, wx.EXPAND, 0)#
        ContenedorControles.Add(self.PosicionVideo, 0, wx.EXPAND, 0)
        Controles.Add(self.botonPlay, 0, 0, 0)
        Controles.Add(self.botonStop, 0, 0, 0)
        Controles.Add(self.botonAtras, 0, 0, 0)
        Controles.Add(self.botonAdelante, 0, 0, 0)
        Controles.Add(self.volumenDown, 0, 0, 0)
        Controles.Add(self.volumenUp, 0, 0, 0)
        #Controles.Add(self.volumenImg, 0, 0, 0)
        ContenedorControles.Add(Controles, 1, 0, 0)
        ContenedorMplayer.Add(ContenedorControles, 1, wx.EXPAND, 0)
        self.panelVideo.SetSizer(ContenedorMplayer)
        Contenedor1.Add(self.panelVideo, 2, wx.EXPAND, 2)
        contenedorDiccionarios.Add(self.pestanaDiccionarios, 1, wx.EXPAND, 0)
        self.panelDiccionarios.SetSizer(contenedorDiccionarios)
        Contenedor1.Add(self.panelDiccionarios, 1, wx.EXPAND, 0)
        contenedorPrincipal.Add(Contenedor1, 2, wx.EXPAND, 4)
        contenedorTexto.Add(self.texto, 2, wx.EXPAND, 3)
        self.panelTexto.SetSizer(contenedorTexto)
        contenedorPrincipal.Add(self.panelTexto, 1, wx.EXPAND, 0)
        contenedorTotal.Add(contenedorPrincipal, 1, wx.EXPAND, 0)
        self.SetSizer(contenedorTotal)
        self.Layout()
        self.Centre()
        # end wxGlade
        
        
    def __controlEventos(self):
        '''
        Control de eventos sobre los widgets (todo, menos los menús).
        '''
        self.botonPlay.Bind(wx.EVT_BUTTON, self.VideoMplayer.onPlayVideo)
        self.botonStop.Bind(wx.EVT_BUTTON, self.VideoMplayer.onStopVideo)
        self.botonAdelante.Bind(wx.EVT_BUTTON, self.VideoMplayer.onAdvanceVideo)
        self.botonAtras.Bind(wx.EVT_BUTTON, self.VideoMplayer.onBackVideo)
        self.volumenDown.Bind(wx.EVT_BUTTON, self.VideoMplayer.volDown)
        self.volumenUp.Bind(wx.EVT_BUTTON, self.VideoMplayer.volUp)

        self.texto.Bind(wx.EVT_KEY_UP, self.VideoMplayer.onKeyPuase)
        
        self.PosicionVideo.Bind(wx.EVT_COMMAND_SCROLL, self.VideoMplayer.setPos)

    
    #Muestra el about
    def onAbout(self, event):
        AboutFrame().Show()
        
        
# end of class MuffinFrame


#---About Window
class AboutFrame(wx.Frame):

    title = "About this program"

    def __init__(self):
        wx.Frame.__init__(self, wx.GetApp().TopWindow, title=self.title)
        self.Center()
