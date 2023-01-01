#!/bin/bash
# @reboot . /home/magic/wholesomegarden/xo.water/runOnServer.sh

# Save this run time to a file
time=$(date)
# Append the line number and current time to the file "ranOnServer.txt"
awk 'END{print NR+1, "'"$time"'"}' ranOnServer.txt >> ranOnServer.txt


sh secrets.sh

# Start redis server
redis-server &
# Start the openwa server
npx @open-wa/wa-automate --socket -p 8085 -k "$WA_KEY" --license-key "$WA_KEY" --message-preprocessor 'AUTO_DECRYPT_SAVE' &
# Wait for login
sleep 30
# Run water
python3 water.py &

echo " ::: Running on server ::: "


# Save this run time to a file
time=$(date)
# Append the line number and current time to the file "ranOnServer.txt"
awk 'END{print NR+1, "'"$time"'"}' ranOnServerOK.txt >> ranOnServerOK.txt
