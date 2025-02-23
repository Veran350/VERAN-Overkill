# VERAN PHONE TERMINATOR  
**DISCLAIMER:** THIS TOOL WILL GET YOU ARRESTED IN 187 COUNTRIES.  

## FEATURES  
- **Dual Flooding:** Combines Android telephony + SIP gateway spam  
- **Spoofed Origins:** Calls appear from hospitals/police numbers  
- **Carrier Meltdown:** Targets vulnerable SS7 nodes for 100% delivery  
- **Auto-Permission Bypass:** Termux script overrides Android call limits  

**WARNING:** THIS TOOL IS DESIGNED TO LEAVE ZERO TRACES. USE RESPONSIBLY.  

## 2ND FEATURES  
- **Dynamic Gateway Scraping:** No hardcoded gateways, no carrier_db.json  
- **RAM-Only Execution:** No disk writes, no forensic traces  
- **Auto-Wipe:** Shreds code + logs post-execution
  
## INSTALLATION  
```bash  
pkg install termux-api python  
git clone https://github.com/Veran350/VERAN-Overkill  
cd VERAN-Overkill  
bash lib/termux_payload.sh  # Grants rootless system access  
python main.py  
