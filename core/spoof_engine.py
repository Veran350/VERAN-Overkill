# core/spoof_engine.py  
import random  

class GhostSpoof:  
    def __init__(self):  
        self.priority_prefixes = [  
            "911", "112", "999", "000",  # Emergency spoofs  
            "800", "888", "877", "866",  # Toll-free masks  
            "311", "511", "611"          # Govt service clones  
        ]  
        self.country_codes = [  
            "1", "44", "33", "49", "86", "81", "91"  # Global coverage  
        ]  

    def generate(self):  
        country = random.choice(self.country_codes)  
        prefix = random.choice(self.priority_prefixes)  
        # Generates hybrid numbers like +1-911-XXX-XXXX  
        return f"+{country}{prefix}{random.randint(1000,9999)}{random.randint(100,999)}"  

    def override_imei(self):  
        # Generates fake 15-digit IMEI for carrier bypass  
        imei = [random.randint(0,9) for _ in range(15)]  
        imei[14] = (sum(imei[::2]) % 10  # Luhn validation spoof  
        return ''.join(map(str, imei))  
