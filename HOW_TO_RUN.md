'''
# HOW TO RUN (each in different terminal)

1 - nvm use 20.11 && npx @open-wa/wa-automate --help --socket -p 8085 -k "$WA_KEY" --license-key "$WA_KEY" --message-preprocessor 'AUTO_DECRYPT_SAVE' --debug 
2 - redis-server & python3.8 app.py
3 - ssh -R xowater.serveo.net:80:localhost:5050 serveo.net
4 - python3.8 water.py

'''

'''
# HOW TO RESTART if started with wrong nvm 
# 1. try restarting linux: wsl --shutdown
# 2. if not working, remove the folowwing
mv ~/.cache/puppeteer ~/.cache/puppeteer_x
mv ~/.npm/_npx ~/.npm/_npx_x
mv session.data.json session.data.json_xxx
'''