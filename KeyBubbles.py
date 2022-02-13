from pynput import keyboard
from pynput.keyboard import Key
from tkinter import *
from collections import deque
from threading import Thread
import tkinter as tk

message_queue = deque()
fins = False

def key_map(key):
    key_dict = {
        Key.alt_l: 'alt',
        Key.alt_gr: 'alt',
        Key.backspace: '⌫',
        Key.cmd: '⌘',
        Key.ctrl_l: 'ctrl',
        Key.ctrl_r: 'ctrl',
        Key.delete: 'del',
        Key.end: 'end',
        Key.enter: '⏎',
        Key.esc: '⮹',
        Key.f1: 'f1',
        Key.f10: 'f10',
        Key.f11: 'f11',
        Key.f12: 'f12',
        Key.f13: 'f13',
        Key.f14: 'f14',
        Key.f15: 'f15',
        Key.f16: 'f16',
        Key.f17: 'f17',
        Key.f18: 'f18',
        Key.f19: 'f19',
        Key.f2: 'f2',
        Key.f20: 'f20',
        Key.f3: 'f3',
        Key.f4: 'f4',
        Key.f5: 'f5',
        Key.f6: 'f6',
        Key.f7: 'f7',
        Key.f8: 'f8',
        Key.f9: 'f9',
        Key.home: '⌂',
        Key.insert: 'Insert',
        Key.menu: '≡',
        Key.pause: 'Pause',
        Key.shift: '⇪',
        Key.shift_r: '⇪',
        Key.space: '⌴',
        Key.caps_lock: '⮸',
        Key.tab: '⭾',
        Key.left: '🡄',
        Key.right: '🡆',
        Key.up: '🡅',
        Key.down: '🡇',
        Key.print_screen: '📷',
        Key.page_down: '▲',
        Key.page_up: '▼'
    }

    try:
        if key in key_dict:
            return key_dict[key]
        else:
            if '\\x' in key.char:
               return "" 
            return key.char.replace("'", "")
    except:
        return ""

def listen_keyboard():
    def on_press(key):
        if fins:
            return False        
        message_queue.append(key_map(key))
    listener = keyboard.Listener(
        on_press = on_press
    )

    listener.start()

thread = Thread(target=listen_keyboard)
thread.start()  # "thread" starts running independently.

root = Tk()
# set size of GUI and it appearance possition
win_width = root.winfo_screenwidth()
win_height = root.winfo_screenheight()
GUI_width = 222
GUI_height = 120
string_config = f"{GUI_width}x{GUI_height}+{win_width - GUI_width - 25}+{win_height - GUI_height - 80}"
root.geometry(string_config)
root.configure(bg='black')

label = tk.Label(
    root, 
    text='',
    font=('Arial', 75),
    bg='black',
    fg='white'
)

label.pack()
label.pack(expand=True)

root.attributes('-alpha', 0.6)
root.attributes("-topmost", True)
root.overrideredirect(True)

def consumeText():
    try: label['text'] = message_queue.popleft()
    except IndexError: pass  # Ignore, if no text available.
    # Reschedule call to consumeText.
    root.after(ms=10, func=consumeText)
consumeText()

def on_closing():
    fins = True
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()