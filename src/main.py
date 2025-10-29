import keyboard

from clear import clear

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
  while running:
    if keyboard.is_pressed('up'):
      current_slot -= 1
      current_slot = current_slot%4
    if keyboard.is_pressed('down'):
      current_slot += 1
      current_slot = current_slot%4
