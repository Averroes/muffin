# -*- encoding: utf-8 -*-
'''
Created on 16/01/2011

@author: erunamo
Este Setup está hecho para usarse con py2exe
'''
from distutils.core import setup 
import os

num_version="0.2 beta"

if os.name == 'nt':
    try:
        import py2exe #CAUTION
    except ImportError:
        print(">>> Falta py2exe <<<")
    from glob import glob
    
    data_files = [("Microsoft.VC90.CRT", glob(r'C:\Users\Admi-Siul\Documents\Aegisub portable\Microsoft.VC90.CRT\*.*'))]
    
    setup(data_files=data_files,
          name="Muffin Translator",
          version=num_version,
          description="Sistema unificado de apoyo para la traducción de anime",
          author="C. Daniel Sanchez R. (ErunamoJAZZ)",
          author_email="anonimato1990@gmail.com",
          url="http://code.google.com/p/muffin/",
          license="GPLv3",
          scripts=["MuffinMain.py"],
          py_modules=["MuffinGUI","MuffinText","VideoMplayer","wx","MplayerCtrl","MuffinDics"],
          console=["MuffinMain.py"], 
          options={"py2exe": {"bundle_files": 1}},
          zipfile=None
    )
else:
        setup(data_files=data_files,
          name="Muffin Translator",
          version=num_version,
          description="Sistema unificado de apoyo para la traducción de anime",
          author="C. Daniel Sanchez R. (ErunamoJAZZ)",
          author_email="anonimato1990@gmail.com",
          url="http://code.google.com/p/muffin/",
          license="GPLv3",
          scripts=["MuffinMain.py"],
          py_modules=["MuffinGUI","MuffinText","VideoMplayer","wx","MplayerCtrl","MuffinDics"],
          console=["MuffinMain.py"], 
          zipfile=None
    )
