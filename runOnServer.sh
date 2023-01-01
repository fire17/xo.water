#!/bin/bash
# @reboot . /home/magic/wholesomegarden/xo.water/runOnServer.sh

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