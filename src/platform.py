import platform
import sys

def detect_platform():
  system = platform.system().lower()
  machine = platform.machine().lower()
  
  if "linux" in system:
    os_name = "linux"
  elif "windows" in system:
    os_name = "windows"
  elif "darwin" in system or "mac" in system:
    os_name = "mac"
  elif "aix" in system:
    os_name = "aix"
  elif "sunos" in system or "solaris" in system:
    os_name = "solaris"
  else:
    return "OSNotFound"
  
  if machine in ("x86_64", "amd64"):
    arch = "x64"
  elif machine in ("aarch64", "arm64"):
    arch = "aarch64"
  elif machine in ("armv7l", "armv8l"):
    arch = "arm"
  elif machine == "ppc64le":
    arch = "ppc64le"
  elif machine == "ppc64":
    arch = "ppc64"
  elif machine == "riscv64":
    arch = "riscv64"
  elif machine == "s390x":
    arch = "s390x"
  elif machine == "i386" or machine == "i686":
    arch = "x32"
  elif machine == "sparcv9":
    arch = "sparcv9"
  else:
    return "ArchNotFound"
  
  return f"{os_name}-{arch}"
