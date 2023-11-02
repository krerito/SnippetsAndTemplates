@echo off

:: Definir la ruta de la carpeta a copiar y la unidad de red
set carpeta_origen="\\192.168.1.60\Public\QN APPLICATION\Release"
set unidad_destino=C:\Release

:: Copiar la carpeta de origen a la carpeta de destino
xcopy %carpeta_origen% %unidad_destino% /E /I /Y

@echo off
set ShortcutName=QN Application.lnk
set ShortcutTarget=C:\Release\QN Application.exe
set ShortcutLocation=%USERPROFILE%\Desktop
set Shortcut=%ShortcutLocation%\%ShortcutName%
set ShortcutScript="%TEMP%\ShortcutScript.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") > %ShortcutScript%
echo sLinkFile = "%Shortcut%" >> %ShortcutScript%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %ShortcutScript%
echo oLink.TargetPath = "%ShortcutTarget%" >> %ShortcutScript%
echo oLink.Save >> %ShortcutScript%
cscript /nologo %ShortcutScript%
del %ShortcutScript%
