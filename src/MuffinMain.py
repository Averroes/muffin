#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Created on 6/12/2010

@author: ErunamoJAZZ
@license: GPLv3
@summary: Muffin Translator, ayudante para la traducción de anime.
@web: http://code.google.com/p/muffin/
'''

from wx import PySimpleApp, InitAllImageHandlers
import MuffinGUI, sys

if __name__ == '__main__':
    '''
    Main de Muffin, aquí se inicializa la ventana.
    '''
    print (u"Iniciando Muffin Translator\n")
    print (u"RECUERDE: puede reportar bugs o sugerencias en la dirección:\n http://code.google.com/p/muffin/issues/list")
    print (u"====================================\n")
    app = PySimpleApp(0)
    InitAllImageHandlers()
    Muffin= MuffinGUI.MuffinFrame (None, -1, "")
    app.SetTopWindow(Muffin)
    Muffin.Show()
    app.MainLoop()
    
    print (u'====================================')
    print (u'Finalizando Muffin Translator')
    
    sys.exit(0)

