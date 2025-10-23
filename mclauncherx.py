import os
import urllib.request
import zipfile
import sys

from src.platform import detect_platform

launcher_ver = 0
installed = 0

launcher_file_path = r"C:\Users\Admin\AppData\Roaming\.minecraft\launcher\mclauncherx.dat"

def down_java(link, java_ver):
  save_java_path = r"C:\Users\Admin\AppData\Roaming\.minecraft\launcher\java" + "\\"
  save_java_path += java_ver + "\\"
  down_java_path = save_java_path + java_ver
  down_java_path += ".zip"
  urllib.request.urlretrieve(link, down_java_path)
  
  with zipfile.ZipFile(down_java_path, "r") as zip_file:
    zip_file.extractall(save_java_path)

  os.remove(down_java_path)

def down_lwjgl(type): # type = 1 -> v2.9.3; type = 2 -> v3.3.6
  if type == 1:
    save_lwjgl_path = r"C:\Users\Admin\AppData\Roaming\.minecraft\launcher\lwjgl\2.9.3" + "\\"
    down_lwjgl_path = save_lwjgl_path + "lwjgl.zip"
    urlib.request.urlretrieve("https://itzhadao.github.io/mclauncherx/lwjgl-2.9.3.zip", down_lwjgl_path)
    
    with zipfile.ZipFile(down_lwjgl_path, "r") as zipf:
      zipf.extractall(save_lwjgl_path)
    
    os.remove(down_lwjgl_path)
  elif type == 2:
    save_lwjgl_path = r"C:\Users\Admin\AppData\Roaming\.minecraft\launcher\lwjgl\3.3.6" + "\\"
    down_lwjgl_path = save_lwjgl_path + "lwjgl.zip"
    urlib.request.urlretrieve("https://itzhadao.github.io/mclauncherx/lwjgl-3.3.6-mc.zip", down_lwjgl_path)
    
    with zipfile.ZipFile(down_lwjgl_path, "r") as zipf:
      zipf.extractall(save_lwjgl_path)
    
    os.remove(down_lwjgl_path)

def download_libraries:
  platform_inf = detect_platform()
  if platform_inf == "OSNotFound":
    print("DEBUG: OS Not Found")
    sys.exit()
  elif platform_inf == "ArchNotFound":
    print("DEBUG: Arch Not Found")
    sys.exit()
  elif

if os.path.isfile(launcher_file_path):
    with open(launcher_file_path, "r") as f:
      content = f.read()
      launcher_ver = content[0:6]
else:
  with open(launcher_file_path, "x") as f:
    file.write("000100") # version a1.0.0
  print("DEBUG: Created mclauncherx.dat")
  
  
