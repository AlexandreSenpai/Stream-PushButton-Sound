import winsound
from playsound import playsound
import keyboard
import json

def read_json():
  with open('sound_directory.json') as _dir:
    data = json.load(_dir)
  return data

def play_sound(key, id):
  sounds = read_json()
  if keyboard.is_pressed(key):
    winsound.PlaySound(sounds['tracks'][id]['dir'], winsound.SND_ASYNC)

  if keyboard.is_pressed('g'):
    winsound.PlaySound(None, winsound.SND_ASYNC)

def play_effects(key, id):
  sounds = read_json()
  if keyboard.is_pressed(key):
    playsound(sounds['effects'][id]['dir'])
    
if __name__ == '__main__':
  while True:
    play_effects('1', 0)
    play_sound('d', 0)
