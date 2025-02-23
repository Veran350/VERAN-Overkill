#!/data/data/com.termux/files/usr/bin/bash  
# Termux trace nuke  
termux-wake-lock  
shred -uzv $PWD/main.py  # Overwrite code  
sqlite3 /data/data/com.android.providers.telephony/databases/mmssms.db "DELETE FROM calls;"  
logcat -c  # Clear Android logs  
rm -rf /data/data/com.termux/files/home/.bash_history  
history -c  
dd if=/dev/urandom of=/dev/log/main bs=1M count=5  
termux-wake-unlock  
