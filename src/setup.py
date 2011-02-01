# -*- encoding: utf-8 -*-
'''
Created on 16/01/2011

@author: erunamo
Este Setup está hecho para usarse con py2exe
'''
from distutils.core import setup 
import os

num_version="0.1.7"

if os.name == 'nt':
    import py2exe #CAUTION
    from glob import glob
    
    data_files = [("Microsoft.VC90.CRT", glob(r'C:\Users\Admi-Siul\Documents\Aegisub portable\Microsoft.VC90.CRT\*.*'))]
    
    setup(data_files=data_files,
          name="Muffin Translator",
          version=num_version,
          description="Sistema unificado de apoyo para la traducción de anime",
          author="C. Daniel Sanchez R. (ErunamoJAZZ)",
          author_email="anonimato1990@gmail.com",
          url="",
          license="GPLv3",
          scripts=["MuffinMain.py"],
          py_modules=["MuffinGUI","MuffinText","VideoMplayer","wx","MplayerCtrl"],
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
          url="",
          license="GPLv3",
          scripts=["MuffinMain.py"],
          py_modules=["MuffinGUI","MuffinText","VideoMplayer","wx","MplayerCtrl"],
          console=["MuffinMain.py"], 
          zipfile=None
    )
