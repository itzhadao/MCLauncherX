import keyboard
import os
import urllib.request

from clear import clear

def down_mc(link, ver, jarf_name):
  save = r"C:\Users\Admin\AppData\Roaming\.minecraft\versions" + "\\"
  save += ver + "\\"
  save += jarf_name + ".jar"
  urllib.request.urlretrieve(link, save)

def file_exists(path):
  return os.path.exists(path)

def run_mc(ver):
  if ver == "rd-132211":
    if not file_exists(r"C:\Users\Admin\AppData\Roaming\.minecraft\versions\rd-132211\rd-132211-launcher.jar"):
      down_mc("https://piston-data.mojang.com/v1/objects/393e8d4b4d708587e2accd7c5221db65365e1075/client.jar", "rd-132211", "rd-132211-launcher.jar")
    os.system(r'C:\Users\Admin\AppData\Roaming\.minecraft\launcher\java\8\bin\java.exe -cp ""')

def main(jdk_vers):
  clear()
  havejdk8 = False
  havejdk17 = False
  havejdk21 = False
  if str(jdk_vers)[0] == 1:
    havejdk8 = True
  if str(jdk_vers)[1] == 1:
    havejdk17 = True
  if str(jdk_vers)[2] == 1:
    havejdk21 = True
  
  current_slot = 0
  running = True
  choices = ["rd-132211", "rd-132328", "rd-160052", "rd-161348"]
  length = len(choices)
  while running:
    for i in range(length):
      if current_slot == i:
        print(">" + choices[current_slot] + "<")
      else:
        print(choices[current_slot])
    clear()
    if keyboard.is_pressed('up'):
      current_slot -= 1
      current_slot = current_slot%length
    if keyboard.is_pressed('down'):
      current_slot += 1
      current_slot = current_slot%length
    if keyboard.is_pressed('enter'):
      run_mc(choices[current_slot])
