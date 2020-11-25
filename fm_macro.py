from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import pyautogui
import keyboard

def get_pos():
    print('click on the fusion button')
    with MouseListener(on_click=button_pos) as listener:
        listener.join()
    return pyautogui.position()

def fusion(button):
    pyautogui.doubleClick()
    save = pyautogui.position()
    pyautogui.click(button)
    pyautogui.moveTo(save)

def button_pos(x, y, button, pressed):
    if not pressed:
        return False

def on_press(key):
    try:
        if key.name == 'ctrl_l' or 'esc':
            mouse_listener.stop()
            keyboard_listener.stop()
    except AttributeError:
        pass

def on_click(x, y, button, pressed):
    if not pressed:
        keyboard_listener.stop()
        mouse_listener.stop()

class pos():
    x = 0
    y = 0

if __name__ == "__main__":
    f_button = pos()
    f_button = get_pos()
    print('press esc to quit')
    while not keyboard.is_pressed('esc'):
        mouse_listener = MouseListener(on_click=on_click)
        keyboard_listener = KeyboardListener(on_press=on_press)
        mouse_listener.start()
        keyboard_listener.start()
        mouse_listener.join()
        keyboard_listener.join()
        if not keyboard.is_pressed('ctrl') and not keyboard.is_pressed('esc'):
            fusion(f_button)
    print('exit')