import pyautogui, keyboard

key_on, key_off = ('1', '2')
clicking = False

while True:
    if keyboard.is_pressed(key_on):
        clicking = True
    elif keyboard.is_pressed(key_off):
        clicking = False
    if clicking:
        pyautogui.click()
