from tkinter import *

window = Tk()
window.wm_attributes('-alpha', 0.93)

window.title("Создание документов для квестов")
window.geometry('1200x800')
window.resizable(width=False, height=False)

frame = Frame(window)
frame.place(relwidth=1, relheight=1)
