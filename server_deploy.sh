# install redis
curl -fsSL https://gist.github.com/fire17/1b2b3b4b5c6c7d8d9e0a3c4d5e5d6e7f/raw | bash

# install ffmpeg
sudo apt install ffmpeg

# clone repo
git clone git@github.com:fire17/xo.water.git

cd xo.water
# install deps
python3 -m pip install -r requirements.txt --upgrade

# run redis
# redis-server &

# export WA_KEY

# run openwa
npx @open-wa/wa-automate --socket -p 8085 -k "$WA_KEY" &

# wait for login
sleep 60

# run water
python3 water.py &