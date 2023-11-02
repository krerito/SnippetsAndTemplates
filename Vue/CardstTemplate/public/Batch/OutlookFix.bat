@echo off
setlocal enabledelayedexpansion

echo ---------------------------------------------------
echo ATENCIÓN: Este script cerrará las aplicaciones de
echo Office 365 y OneDrive. También desactivará el inicio 
echo automático de OneDrive y, finalmente, abrirá Outlook en modo seguro.
echo ---------------------------------------------------
echo.
echo Por favor, cierra tus documentos y guarda tu trabajo.
echo.
echo Si estás de acuerdo, escribe "SI" y presiona Enter.
echo De lo contrario, solo cierra esta ventana.
echo.

set /p userInput=Confirmación: 

if /i "%userInput%" NEQ "SI" (
    echo Operación cancelada por el usuario.
    exit /b
)

:: Matar procesos relacionados con OneDrive y Office 365
echo Cerrando OneDrive...
taskkill /f /im OneDrive.exe
if ERRORLEVEL 1 (
    if ERRORLEVEL 128 (
        echo OneDrive no estaba en ejecución.
    ) else (
        echo Ocurrió un error al cerrar OneDrive: !ERRORLEVEL!
        echo Por favor, manda esta información a IT. Se requiere atención personal.
        pause
        exit /b
    )
)
pause

echo Cerrando Word...
taskkill /f /im WINWORD.EXE
if ERRORLEVEL 1 (
    if ERRORLEVEL 128 (
        echo Word no estaba en ejecución.
    ) else (
        echo Ocurrió un error al cerrar Word: !ERRORLEVEL!
        echo Por favor, manda esta información a IT. Se requiere atención personal.
        pause
        exit /b
    )
)
pause

echo Cerrando Excel...
taskkill /f /im EXCEL.EXE
if ERRORLEVEL 1 (
    if ERRORLEVEL 128 (
        echo Excel no estaba en ejecución.
    ) else (
        echo Ocurrió un error al cerrar Excel: !ERRORLEVEL!
        echo Por favor, manda esta información a IT. Se requiere atención personal.
        pause
        exit /b
    )
)
pause

echo Cerrando PowerPoint...
taskkill /f /im POWERPNT.EXE
if ERRORLEVEL 1 (
    if ERRORLEVEL 128 (
        echo PowerPoint no estaba en ejecución.
    ) else (
        echo Ocurrió un error al cerrar PowerPoint: !ERRORLEVEL!
        echo Por favor, manda esta información a IT. Se requiere atención personal.
        pause
        exit /b
    )
)
pause

echo Cerrando Outlook...
taskkill /f /im OUTLOOK.EXE
if ERRORLEVEL 1 (
    if ERRORLEVEL 128 (
        echo Outlook no estaba en ejecución.
    ) else (
        echo Ocurrió un error al cerrar Outlook: !ERRORLEVEL!
        echo Por favor, manda esta información a IT. Se requiere atención personal.
        pause
        exit /b
    )
)
pause

:: Desactivar el inicio automático de OneDrive
echo Desactivando el inicio automático de OneDrive...
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "OneDrive" /t REG_SZ /d "" /f
if ERRORLEVEL 1 (
    echo Ocurrió un error al desactivar el inicio automático de OneDrive: !ERRORLEVEL!
    echo Por favor, manda esta información a IT. Se requiere atención personal.
    pause
    exit /b
)
pause

:: Iniciar Outlook en modo seguro
echo Iniciando Outlook en modo seguro...
start outlook.exe /safe
if ERRORLEVEL 1 (
    echo Ocurrió un error al iniciar Outlook en modo seguro: !ERRORLEVEL!
    echo Por favor, manda esta información a IT. Se requiere atención personal.
    pause
    exit /b
)
pause

echo Proceso completado con éxito.
endlocal
