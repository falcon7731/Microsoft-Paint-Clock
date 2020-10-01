import pyautogui
from datetime import datetime
import keyboard
from time import sleep
import sys


screenWidth, screenHeight = pyautogui.size()
running = True
is_drawing = False
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05
def draw_num(num,length , start,time):
    if num == 0:
        for l in 'abcdef':
            draw_line(l,length, start , time)
    if num == 1:
        for l in 'de':
            draw_line(l,length, start , time)
    if num == 2:
        for l in 'fegbc':
            draw_line(l,length, start , time)
    if num == 3:
        for l in 'fegdc':
            draw_line(l,length, start , time)
    if num == 4:
        for l in 'aged':
            draw_line(l,length, start , time)
    if num == 5:
        for l in 'fagdc':
            draw_line(l,length, start , time)
    if num == 6:
        for l in 'fabcdg':
            draw_line(l,length, start , time)
    if num == 7:
        for l in 'fed':
            draw_line(l,length, start , time)
    if num == 8:
        for l in 'abcdefg':
            draw_line(l,length, start , time)
    if num == 9:
        for l in 'gafedc':
            draw_line(l,length, start , time)

class pos:
    
    def __init__(self,start):
        self.x = start.x
        self.y = start.y
        self.init_x = start.x
        self.init_y = start.y

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

def draw_line(line,lenghth , start , time):
    pyautogui.moveTo(start.x , start.y)
    if line == 'a':
        pyautogui.drag(0, lenghth, duration=time)
    if line == 'b':
        pyautogui.move(0, lenghth)
        pyautogui.drag(0, lenghth, duration=time)
    if line == 'c':
        pyautogui.move(0, 2*lenghth)
        pyautogui.drag(lenghth, 0, duration=time)
    if line == 'd':
        pyautogui.move(lenghth, 2*lenghth)
        pyautogui.drag(0, -lenghth, duration=time)
    if line == 'e':
        pyautogui.move(lenghth, lenghth)
        pyautogui.drag(0, -lenghth, duration=time)
    if line == 'f':
        pyautogui.move(lenghth, 0)
        pyautogui.drag(-lenghth, 0, duration=time)
    if line == 'g':
        pyautogui.move(lenghth, lenghth)
        pyautogui.drag(-lenghth, 0, duration=time)
    if line == ':':
        pyautogui.click(422, 62)
        pyautogui.moveTo(start.x , start.y)
        pyautogui.move(lenghth/2-4, lenghth/2-4)
        pyautogui.drag(8, 8, duration=time)
        pyautogui.move(0, lenghth)
        pyautogui.drag(8, 8, duration=time)
        pyautogui.click(336, 74)

def clear():
    sleep(1)
    keyboard.press_and_release('ctrl+a')
    keyboard.press_and_release('delete')
    sleep(0.1)
    keyboard.press_and_release('alt')
    sleep(0.1)
    keyboard.press_and_release('h')
    sleep(0.1)
    keyboard.press_and_release('b')
    sleep(0.1)
    keyboard.press_and_release('enter')


def startt():
    global is_drawing
    is_drawing = True


keyboard.add_hotkey('ctrl+shift+p', lambda: startt())

print('Ready')
while running:
    get_pos = pyautogui.position()
    start = pos(get_pos)
    if is_drawing:
        t = datetime.now().time()
        h = format(t.hour,'02d')
        m = format(t.minute,'02d')
        s = format(t.second , '02d')
        print(t)
        for l in h:
            draw_num(int(l),60, start , 0.3)
            print(start)
            start.x += 80
        draw_line(':',60, start , 0.2)
        start.x += 80
        for l in m:
            draw_num(int(l),60, start , 0.25)
            start.x += 80
        draw_line(':',60, start , 0.15)
        start.x += 80
        for l in s:
            draw_num(int(l),60, start , 0.15)
            start.x += 80
        start.x = start.init_x
        pyautogui.moveTo(start.x , start.y)
        clear()
        if keyboard.is_pressed('q'):
            sys.exit()




