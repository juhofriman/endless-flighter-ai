#!/usr/bin/env python3


from pynput import keyboard

a_pressed = 0
s_pressed = 0

def on_press(key):
    global a_pressed, s_pressed
    if(key.char == 'a'):
        a_pressed = 1
    if(key.char == 's'):
        s_pressed = 1


def on_release(key):
    global a_pressed, s_pressed
    if(key.char == 'a'):
        a_pressed = 0
    if(key.char == 's'):
        s_pressed = 0

def kb_state():
    return [a_pressed, s_pressed]

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
