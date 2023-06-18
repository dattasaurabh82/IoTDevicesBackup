import os
from datetime import date

today = date.today()
print(today)

os.system('git add .')
os.system('git commit -m \"latest comtmit\"')
os.system('git status')
os.system('git push -u origin main')

# test
