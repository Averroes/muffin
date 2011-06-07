# -*- encoding: utf-8 -*-
'''
Created on 16/01/2011

@author: erunamo
Este Setup está hecho para usarse con py2exe
'''
from distutils.core import setup 
import os

num_version=u"0.2"

if os.name == 'nt':
    try:
        import py2exe #CAUTION
    except ImportError:
        print(">>> Falta py2exe <<<")
        os.sys.exit(1)
    from glob import glob
    
    data_files = [("Microsoft.VC90.CRT", glob(r'C:\Users\Admi-Siul\Documents\Aegisub portable\Microsoft.VC90.CRT\*.*'))]
    
    setup(data_files=data_files,
          name=u"Muffin Translator",
          version=num_version,
          description=u"Muffin Translator. Sistema unificado de apoyo para la traducción de anime.",
          author=u"C. Daniel Sanchez R. (ErunamoJAZZ)",
          author_email=u"anonimato1990@gmail.com",
          url=u"http://code.google.com/p/muffin/",
          license=u"GPLv3",
          scripts=["MuffinMain.py"],
          py_modules=["MuffinGUI","MuffinText","VideoMplayer","wx","MplayerCtrl","MuffinDics"],
          console=[{"script":"MuffinMain.py", "icon_resources": [(0, "img/muffin.ico")]  }],
          zipfile=None,
          options={"py2exe": {"bundle_files": 1}}
          )
else:
    setup(data_files=data_files,
          name=u"Muffin Translator",
          version=num_version,
          description=u"Muffin Translator. Sistema unificado de apoyo para la traducción de anime.",
          author=u"C. Daniel Sanchez R. (ErunamoJAZZ)",
          author_email=u"anonimato1990@gmail.com",
          url=u"http://code.google.com/p/muffin/",
          license=u"GPLv3",
          scripts=["MuffinMain.py"],
          py_modules=["MuffinGUI","MuffinText","VideoMplayer","wx","MplayerCtrl","MuffinDics"],
          console=["MuffinMain.py"], 
          zipfile=None
          )
