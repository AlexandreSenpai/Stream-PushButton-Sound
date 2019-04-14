import winsound
from time import sleep
from playsound import playsound
import keyboard
import json

def read_json():
  with open('sound_directory.json') as _dir:
    data = json.load(_dir)
  return data

def sound_effect(key, id):
  sounds = read_json()
  if keyboard.is_pressed(key):
    winsound.PlaySound(sounds['tracks'][id]['dir'], winsound.SND_ASYNC)
    sleep(0.09)

  if keyboard.is_pressed('g'):
    winsound.PlaySound(None, winsound.SND_ASYNC)
    
if __name__ == '__main__':
  while True:
    sound_effect('d', 0)