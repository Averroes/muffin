# -*- encoding: utf-8 -*-
'''
Created on 6/12/2010

@author: erunamo
'''
import wx
import VideoMplayer


class MuffinFrame(wx.Frame):
    '''
    classdocs
    '''
    def __init__(self, *args, **kwds):
        '''
        Constructor
        '''
        # begin wxGlade: MuffinFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panelTexto = wx.Panel(self, -1)
        self.panelDiccionarios = wx.Panel(self, -1)
        self.pestanaDiccionarios = wx.Notebook(self.panelDiccionarios, -1, style=0)
        self.panelVideo = wx.Panel(self, -1)
        self.ContVolumen_staticbox = wx.StaticBox(self.panelVideo, -1, "Volumen")
        
        # Menu Bar
        self.Muffin_menubar = wx.MenuBar()
        
        wxglade_tmp_menu = wx.Menu()
        wxAbrir=wxglade_tmp_menu.Append(wx.NewId(), "Abrir", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VideoMplayer.onLoadFile, wxAbrir)
        self.Muffin_menubar.Append(wxglade_tmp_menu, "Archivo")
        
        wxglade_tmp_menu = wx.Menu()
        wxSubtitulo=wxglade_tmp_menu.Append(wx.NewId(), "Cargar Sub del video(MKV)", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, VideoMplayer.onLoadSub, wxSubtitulo)
        self.Muffin_menubar.Append(wxglade_tmp_menu, "Opciones de video")
        
        self.SetMenuBar(self.Muffin_menubar)
        # Menu Bar end
        
        self.VideoMplayer = VideoMplayer.initVideo(self.panelVideo) #wx.Panel(self.panelVideo, -1)
        self.PosicionVideo = wx.Slider(self.panelVideo, -1, 0, 0, 99)
        self.botonPlay = wx.BitmapButton(self.panelVideo, -1, wx.Bitmap("play.png", wx.BITMAP_TYPE_ANY))
        self.botonStop = wx.BitmapButton(self.panelVideo, -1, wx.Bitmap("stop.png", wx.BITMAP_TYPE_ANY))
        self.botonAtras = wx.BitmapButton(self.panelVideo, -1, wx.Bitmap("atras.png", wx.BITMAP_TYPE_ANY))
        self.botonAdelante = wx.BitmapButton(self.panelVideo, -1, wx.Bitmap("adelante.png", wx.BITMAP_TYPE_ANY))
        self.volumen = wx.Slider(self.panelVideo, -1, 0, 0, 100)
        self.panelDiccionario1 = wx.Panel(self.pestanaDiccionarios, -1)
        self.texto = wx.TextCtrl(self.panelTexto, -1, """Actor 1:    Well do I understand your speech, yet few strangers do so.\n        Why then do you not speak in the Common Tongue,\n        as        is the custom in the West, if you wish to be answered?\n# TL check: The above seems to be a        quote from the lord of the rings, look it up later\nActor 2:What are you babbling about?""", style=wx.TE_MULTILINE|wx.HSCROLL)

        self.__set_properties()
        self.__do_layout()
        self.__controlEventos()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MuffinFrame.__set_properties
        self.SetTitle("Muffin Translator - PreAlpha version")
        self.SetSize((800, 600))
        self.SetMinSize((800, 600))
        self.botonPlay.SetSize(self.botonPlay.GetBestSize())
        self.botonStop.SetSize(self.botonStop.GetBestSize())
        self.botonAtras.SetSize(self.botonAtras.GetBestSize())
        self.botonAdelante.SetSize(self.botonAdelante.GetBestSize())
        self.volumen.SetMinSize((160, 21))
        # end wxGlade

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
        ContVolumen = wx.StaticBoxSizer(self.ContVolumen_staticbox, wx.VERTICAL)
        ContenedorMplayer.Add(self.VideoMplayer, 4, wx.EXPAND, 0)#
        ContenedorControles.Add(self.PosicionVideo, 0, wx.EXPAND, 0)
        Controles.Add(self.botonPlay, 0, 0, 0)
        Controles.Add(self.botonStop, 0, 0, 0)
        Controles.Add(self.botonAtras, 0, 0, 0)
        Controles.Add(self.botonAdelante, 0, 0, 0)
        ContVolumen.Add(self.volumen, 0, wx.EXPAND, 0)
        Controles.Add(ContVolumen, 1, wx.EXPAND, 0)
        ContenedorControles.Add(Controles, 1, 0, 0)
        ContenedorMplayer.Add(ContenedorControles, 1, wx.EXPAND, 0)
        self.panelVideo.SetSizer(ContenedorMplayer)
        Contenedor1.Add(self.panelVideo, 2, wx.EXPAND, 2)
        self.pestanaDiccionarios.AddPage(self.panelDiccionario1, "tab1")
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
        self.botonPlay.Bind(wx.EVT_BUTTON, VideoMplayer.onPlayVideo)
        self.botonStop.Bind(wx.EVT_BUTTON, VideoMplayer.onStopVideo)
        self.botonAdelante.Bind(wx.EVT_BUTTON, VideoMplayer.onAdvanceVideo)
        self.botonAtras.Bind(wx.EVT_BUTTON, VideoMplayer.onBackVideo)
        
        #self.texto.Bind(wx.KeyEvent.GetKeyCode()==wx.k, VideoMplayer.onKeyPuase)

# end of class MuffinFrame

