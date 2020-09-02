import pyautogui
import keyboard
import msvcrt

def get_pos():
    pos = input('point the fusion button and press enter')
    return pyautogui.position()

def select():
    pyautogui.keyDown('ctrl')
    pyautogui.doubleClick()
    pyautogui.keyUp('ctrl')
    
def fusion(button):
    pyautogui.click(button)

def activate(ex):
    if ex == 0:
        print('off')
        return 2
    elif ex == 2:
        print('on')
        return 0

def bind():
    print('press the select key\n')
    k_1 = keyboard.read_hotkey()
    print(k_1)
    print('press the fusion key\n')
    k_2 = keyboard.read_hotkey()
    print(k_2[2])
    return k_1, k_2[2]

class pos():
    x = 0
    y = 0

if __name__ == "__main__":
    button = pos()
    button = get_pos()
    k_1 = '1'
    k_2 = '2'
    k_3 = '3'
    k_4 = '4'
    print('\npress 1 to select\npress 2 to fusion\npress 3 to activate/desactivate\npress 4 to bind\npress esc to quit')
    ex = 0
    while ex != 1:
        if ex != 2:
            if keyboard.is_pressed(k_1) == True:
                select()
                while keyboard.is_pressed(k_1) == True:
                    ex = ex
            if keyboard.is_pressed(k_2) == True:
                fusion(button)
                while keyboard.is_pressed(k_2) == True:
                    ex = ex
        if keyboard.is_pressed(k_3) == True:
            ex = activate(ex)
            while keyboard.is_pressed(k_3) == True:
                ex = ex
        if keyboard.is_pressed(k_4) == True:
            while keyboard.is_pressed(k_4) == True:
                ex = ex
            k_1, k_2 = bind()
        if keyboard.is_pressed('escape') == True:
            print('exiting...')
            ex = 1