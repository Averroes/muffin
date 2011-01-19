#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Created on 6/12/2010

@author: erunamo
'''

import wx
import MuffinGUI

if __name__ == '__main__':
    '''
    Main de Muffin, aquí se inicializa la ventana.
    '''
    print "Iniciando Muffin Translator"
    print "RECUERDE: debe tener instalado el mplayer(*nix) desde los repositorios,"
    print "o el mplayer.exe(win) en el mismo directorio del ejecutable."
    print "--------------------------"
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    Muffin= MuffinGUI.MuffinFrame (None, -1, "")
    app.SetTopWindow(Muffin)
    Muffin.Show()
    app.MainLoop()
    print 'Finalizando Muffin Translator'
