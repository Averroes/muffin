# Introduction #

Muffin lo estoy desarrollando en debian, por lo que describiré aquí como instalar los requisitos necesarios para su ejecución.


## Debian/Ubuntu ##

Muffin necesita para funcionar:
  * Python 2.6+
  * wxPython 2.8
  * mplayer
  * MplayerCtrl
  * simplejson

el comando para instalar estas dependencias es:

```
$ sudo aptitude python-setuptools python-wxgtk2.8 mplayer && sudo easy_install mplayerctrl simplejson
```

## Fedora ##
En Fedora, debería servir el siguiente comando (cualquier error, por favor reportarlo):
```
$ su-
# yum install wxpython-2.8 python-setuptools mplayer && easy_install mplayerctrl simplejson
```

## Arch ##
En ArchLinux, debería servir el siguiente comando (cualquier error, por favor reportarlo):
```
$ su-
# pacman -S wxpython python2-distribute mplayer && easy_install-2.7 mplayerctrl simplejson
```
**¡¡Atención!!:** debes ejecutar el muffin con _python2_, ya que wxPython no funciona aun con python3.

**NOTA:** Gracias a Eddotan por hacer [un paquete en \*AUR\*](https://aur.archlinux.org/packages.php?ID=46544) ;D

# Descargar código #
Para eso necesitas "Mercurial", debes descargarlo desde los repositorios de tu distribución.
Una vez con ello, usa en un shell:
```
hg clone https://muffin.googlecode.com/hg/ muffin 
```

## Actualizar codigo ##
Si ya tienes una copia del repositorio, y quieres actualizar a los últimos cambios, ejecuta los siguiente en la carpeta 'muffin':
```
hg pull
hg update
```
Esto descarga los datos del repositorio, y luego actualiza la copia local.


# Ejecutar programa #
El programa se inicia desde MuffinMain.py