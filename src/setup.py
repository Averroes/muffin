# -*- encoding: utf-8 -*-
'''
Created on 16/01/2011

@author: erunamo
Este Setup está hecho para usarse con py2exe
'''
from distutils.core import setup 
import py2exe #CAUTION

setup(name="Muffin Translator",
      version="0.1",
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