@echo off

REM İndirilecek dosyanın URL'si
set "url=https://blog.ipleaders.in/wp-content/uploads/2020/02/Ways-Websites-Are-Hacked-How-to-Prevent-Them-1.png"

REM İndirilecek dosyanın kaydedileceği yol
set "downloaded_file=%USERPROFILE%\Downloads\background_image.png"

REM Masaüstü arka planı olarak kullanılacak dosyanın yolu
set "desktop_file=%USERPROFILE%\Desktop\background_image.png"

REM Resmi indir
powershell -command "(New-Object System.Net.WebClient).DownloadFile('%url%', '%downloaded_file%')"

REM Eğer dosya başarıyla indirilmişse, masaüstü arka planını değiştir
if exist "%downloaded_file%" (
    REM Masaüstü arka planını değiştirme komutları
    REG ADD "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "%desktop_file%" /f
    RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters
) else (
    echo Resim indirilemedi.
)
title HACKED!!!
:a
set /a num=(%Random% %%9)+1
color %num%
echo ooooo   ooooo       .o.         .oooooo.   oooo    oooo oooooooooooo oooooooooo.   
echo `888'   `888'      .888.       d8P'  `Y8b  `888   .8P'  `888'     `8 `888'   `Y8b  
echo  888     888      .8"888.     888           888  d8'     888          888      888 
echo  888ooooo888     .8' `888.    888           88888[       888oooo8     888      888 
echo  888     888    .88ooo8888.   888           888`88b.     888    "     888      888 
echo  888     888   .8'     `888.  `88b    ooo   888  `88b.   888       o  888     d88' 
echo o888o   o888o o88o     o8888o  `Y8bood8P'  o888o  o888o o888ooooood8 o888bood8P'                                                         					                                                                                                             
ping localhost -n 1.5 >nul
goto a
pause