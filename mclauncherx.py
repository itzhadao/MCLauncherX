import os
import urllib.request
import zipfile
import sys

from src.platform import detect_platform

launcher_ver = 0

jdk_vers = []

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

def down_jdk_tar(link, java_ver):
  save_java_path = r"C:\Users\Admin\AppData\Roaming\.minecraft\launcher\java" + "\\"
  save_java_path += java_ver + "\\"
  down_java_path = save_java_path + java_ver
  down_java_path += ".tar.gz"
  
  urllib.request.urlretrieve(link, down_java_path)
  
  with tarfile.open(down_java_path, "r:gz") as tarf:
    tar.extractall(save_java_path)
  
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

def download_lwjgl():
  down_lwjgl(1)
  down_lwjgl(2)
  print("DEBUG: Downloaded LWJGL versions")

def download_libraries:
  global jdk_vers
  platform_inf = detect_platform()
  if platform_inf == "OSNotFound":
    print("DEBUG: OS Not Found")
    sys.exit()
  elif platform_inf == "ArchNotFound":
    print("DEBUG: Arch Not Found")
    sys.exit()
  elif platform_inf == "linux-aarch64":
    down_jdk_tar("https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u462-b08/OpenJDK8U-jdk_aarch64_linux_hotspot_8u462b08.tar.gz", 8)
    down_jdk_tar("https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.16%2B8/OpenJDK17U-jdk_aarch64_linux_hotspot_17.0.16_8.tar.gz", 17)
    down_jdk_tar("https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.8%2B9/OpenJDK21U-jdk_aarch64_linux_hotspot_21.0.8_9.tar.gz", 21)
    jdk_vers = [8, 17, 21]
    print("DEBUG: Downloaded java versions")
    download_lwjgl()

if os.path.isfile(launcher_file_path):
    with open(launcher_file_path, "r") as f:
      content = f.read()
      launcher_ver = content[0:6]
else:
  with open(launcher_file_path, "x") as f:
    file.write("000100") # version a1.0.0
  print("DEBUG: Created mclauncherx.dat")
  
  
