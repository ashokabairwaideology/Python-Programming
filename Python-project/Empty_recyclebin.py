#pip install winshell

import winshell 
try:
     winshell.recycle_bin().empty(confirm=False,show_progress=False, sound=True)
     print("Recycle bin empty now")


except:
     print("Recycle bin already empty")
