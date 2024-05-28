# Przechwyć Wysokość GUGiK

## PL
Wtyczka QGIS pozwalająca na sprawdzanie wysokości terenu w danym punkcie na obszarze Polski. Działa na podstawie danych z bazy NMT, udostępnianych przez Główny Urząd Geodezji i Kartografii.

### Instrukcja pobrania
* Wtyczkę należy zainstalować w QGIS jako ZIP lub wgrać pliki wtyczki do lokalizacji `C:\Users\User\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`.
* Aby uruchomić wtyczkę, należy kliknąć na ikonę niebieskiego drzewa oznaczonego napisem NMT.
* Jeżeli ikona wtyczki nie jest widoczna w panelu warstw, spróbuj zrestartować QGIS.
* Jeżeli wtyczka nadal nie jest widoczna, należy przejść w QGIS Desktop do Wtyczki -> Zarządzanie wtyczkami -> Zainstalowane -> Przechwyć Wysokość GUGiK -> Odinstalować wtyczkę i zainstalować ponownie.

### Instrukcja użytkowania:
* Po uruchomieniu widżet wtyczki pojawi się w lewej dolnej części interfejsu.
* Aby uzyskać wysokość terenu, należy nacisnąć przycisk "Przechwytuj" i kliknąć w dowolne miejsce na mapie na terenie Polski.
* Współrzędne są w układzie PUWG92.
* Dane o wysokości można skopiować, naciskając przycisk "Kopiuj do schowka". Będą skopiowane według szablonu (współrzędna x, współrzędna y, wysokość).

## EN
A QGIS plugin that allows checking the terrain elevation at a given point in Poland. It operates based on data from the NMT database, provided by the Head Office of Geodesy and Cartography.

### Download Instructions
* The plugin should be installed in QGIS as a ZIP or by uploading the plugin files to the location `C:\Users\User\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`.
* To launch the plugin, click on the blue tree icon labeled NMT.
* If the plugin icon is not visible in the layer panel, try restarting QGIS.
* If the plugin is still not visible, go to QGIS Desktop -> Plugins -> Manage and Install Plugins -> Installed -> Przechwyć Wysokość GUGiK -> Uninstall the plugin and reinstall it.

### Usage Instructions:
* After launching, the plugin widget will appear in the lower left part of the interface.
* To obtain the terrain elevation, press the "Przechwytuj" button and click anywhere on the map within Poland.
* The coordinates are in the PUWG92 system.
* Elevation data can be copied by pressing the "Kopiuj do schowka" button. They will be copied in the format (coordinate x, coordinate y, elevation).
