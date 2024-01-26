#!/bin/bash
# @reboot . /home/magic/wholesomegarden/xo.water/runOnServer.sh

# MAKE SURE YOU ARE USING NODE 16
# nvm use 16

# Make sure pm2 is installed
# npm install pm2 -g

# use pm2 to run the script (remember to setup secrets.json)
# pm2 start npx --name "wa-automate" -e /home/magic/wholesomegarden/xo.water/secrets.json -- @open-wa/wa-automate --socket -p 8085 -k "$WA_KEY" --license-key "$WA_KEY" --message-preprocessor 'AUTO_DECRYPT_SAVE'

# Save this run time to a file
time=$(date)
# Append the line number and current time to the file "ranOnServer.txt"
awk 'END{print NR+1, "'"$time"'"}' ./ranOnServer.txt >> ./ranOnServer.txt


. ./secrets.sh

echo WA_KEY = $WA_KEY

# Start redis server
redis-server &
# Start the openwa server
# npx @open-wa/wa-automate --socket -p 8085 -k "$WA_KEY" --license-key "$WA_KEY" --message-preprocessor 'AUTO_DECRYPT_SAVE' &
# /home/magic/.nvm/versions/node/v16.19.0/bin/npx @open-wa/wa-automate --socket -p 8085 -k "$WA_KEY" --license-key "$WA_KEY" --message-preprocessor 'AUTO_DECRYPT_SAVE' &
# Wait for login
sleep 30
# Run water
python3 water.py &

echo " ::: Running on server ::: "


# Save this run time to a file
time=$(date)
# Append the line number and current time to the file "ranOnServer.txt"
awk 'END{print NR+1, "'"$time"'"}' ./ranOnServerOK.txt >> ./ranOnServerOK.txt
