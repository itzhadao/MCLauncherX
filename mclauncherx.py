import os
import urllib.request

# https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25%2B36/OpenJDK25U-jdk_x64_windows_hotspot_25_36.zip

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
    save_java_path = r"C:\Users\Admin\

if os.path.isfile(launcher_file_path):
    with open(launcher_file_path, "r") as f:
      content = f.read()
      launcher_ver = content[0:6]
else:
  with open(launcher_file_path, "x") as f:
    file.write("000100") # version a1.0.0
  print("DEBUG: Created mclauncherx.dat")
  
  
