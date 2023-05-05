from pynput.keyboard import Key,Controller
import time
import subprocess as sub
keyboard=Controller()
keyboard.press(Key.cmd)
keyboard.press('t')
keyboard.release('t')
keyboard.release(Key.cmd)
time.sleep(1)
keyboard.type("python3 producer.py")
keyboard.press(Key.enter)
keyboard.release(Key.enter)