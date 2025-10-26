import os
import platform

def clear():
  os_name = platform.system()
  if os_name == "Windows":
    os.system("cls")
  else:
    os.system("clear")
