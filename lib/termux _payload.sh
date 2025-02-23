#!/data/data/com.termux/files/usr/bin/bash  
# Grants Termux system-level access  
termux-microphone-record -l  # Bypass call limits  
termux-telephony-call --reset  # Clear call logs  
termux-notification -t "SYSTEM UPDATE" --priority max  
