from tkinter import *
import pyautogui
import keyboard
import pyperclip

root = Tk()

def rgb_to_hex(rgb):
    return '%02X%02X%02X' % rgb

def btn_click():
    z = True
    while z:
        xy = pyautogui.position() 
        s = str(list(xy)[0]) + ', ' + str(list(xy)[1])      
        if keyboard.is_pressed('ESC') == True:
            pyperclip.copy(s)
            z = False
            colorD = '#' + rgb_to_hex(pyautogui.pixel(list(xy)[0], list(xy)[1])) #Получение цвета пикселя

    Label(text=s, font=30, height=2, width=17)\
        .grid(row=3, column=1) 
    Label(text=colorD, font=30, height=2, width=17)\
        .grid(row=4, column=1)

root['bg'] = '#1E1E1E' # цвет фона
root.title('Координаты мыши') # название программы
root.wm_attributes('-alpha', 0.9) # прозрачность окна
root.attributes("-topmost", True) # поверх всех окон
root.geometry('320x220') # размеры окна
root.resizable(width=False, height=False) # можно ли изменять размеры окна

Label(text='Нажмите "ESC" для остановки программы', bg='#1E1E1E', fg='white', font=70, height=2)\
    .grid(row=0, column=0, columnspan=5)

Button(text="Click!", command=btn_click, font=250, height=3, width=35).grid(row=1, column=0, columnspan=5)

Label(text="", bg='#1E1E1E')\
    .grid(row=2, column=0) #пустое место

Label(text='Координаты', bg='#1E1E1E', fg='white', font=40, height=2, width=17)\
    .grid(row=3, column=0)

Label(text='вывод', font=30, height=2, width=17)\
        .grid(row=3, column=1)

Label(text='Цвет пикселя', bg='#1E1E1E', fg='white', font=40, height=2, width=17)\
    .grid(row=4, column=0)

Label(text='вывод', font=30, height=2, width=17)\
        .grid(row=4, column=1)

def Quit():
    pass
root.protocol("WM_DELETE_WINDOW", Quit)
root.mainloop()



