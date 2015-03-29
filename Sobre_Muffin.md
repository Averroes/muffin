# ¿QUÉ ES MUFFIN? #
Muffin es un ayudante para la traducción de subtítulos, pensado para
los traductores de anime. Muestra en una misma ventana: el video, el
área para escribir texto, y la consulta de diccionarios on-line. Esto
ahorra valioso tiempo a la hora de traducir, ya que se evita la
tediosa tarea de pasar entre ventanas por cada línea de
traducción, etc.





## Más sobre Muffin ##

Muffin hace uso de Python, un lenguaje interpretado y multiplataforma
muy fácil de escribir; también usa wxWidgets en su versión para Python
(wxPython), una biblioteca para hacer interfaces graficas
multiplataforma, que se integra perfectamente según el sistema
operativo en que se use (en Windows usa WindowsForms; en Linux usa GTK; en MacOSX usa Cocoa).

Por último, hace uso del reproductor de video Mplayer en su versión para
consola (sin interfaz grafica), mediante MplayerCtrl, un modulo que lo
integra a wxPython. Mplayer permite a Muffin reproducir videos de cualquier
> tipo incluyendo Matroskas con softsubs (subtítulos flotantes, no pegados
al video). Todo esto hace que Muffin sea completamente multiplataforma,
estable, y que su ampliación también sea mucho más sencilla.



# MUFFIN EN WINDOWS #
Muffin para Windows se distribuye en un .7z (7-Zip), en su interior hay:

  * Carpeta img con imágenes del programa,

  * Microsoft.VC90.CRT con datos del Runtime C++ (necesarios para la ejecución),

  * MuffinMain.exe el archivo "todo en uno" para ejecutar Muffin,

  * Mplayer.exe en compilación genérica.



Si se desea usar una versión del Mplayer.exe optimizada para su procesador,

puede dirigirse a la siguiente página para descargar y remplazar el ejecutable:



> http://oss.netfarm.it/mplayer-win32.php






# MUFFIN EN LINUX #
Muffin se sabe que funciona con Python 2.6 o 2.7, es posible que con versiones anteriores aun lo haga, pero no es seguro. Tampoco se ha pensado aun en
compatibilidad para Python3, pero no se descarta en un futuro cercano, cuando wxPython lo soporte.

Es necesario que descargue desde los repositorios de su distribución los
paquetes wxGTK-2.8 o equivalente, y mplayer. Además de esto, debe instalar
el modulo MplayerCtrl, más información en la siguiente página:



> http://packages.python.org/MplayerCtrl/



El programa se inicia desde MuffinMain.py







# LICENCIA #
Muffin está cobijado bajo la licencia libre GPL versión 3.

Se le concede la libertad de distribuir tanto el programa
ejecutable como el código del mismo, y se le exige la
responsabilidad de redistribuir el código modificado bajo
los mismos términos.


La licencia completa se encuentra en:

> http://www.gnu.org/copyleft/gpl.html




> ## Web de Muffin ##

La web sobre la que se mantiene el desarrollo de Muffin
está alojada en Google Code:



> http://code.google.com/p/muffin/








Por ahora, la versión está en desarrollo, usando Eclipse PyDev.