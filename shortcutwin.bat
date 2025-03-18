del "%AppData%\Microsoft\Windows\Start Menu\Programs\tab-for-a-cause-selenium.lnk" || rem
powershell -command "$s=(New-Object -COM WScript.Shell).CreateShortcut('%AppData%\Microsoft\Windows\Start Menu\Programs\tab-for-a-cause-selenium.lnk');$s.TargetPath='%~dp0tab-for-a-cause-selenium.py';$s.IconLocation='%~dp0icon.ico';$s.Save()"
