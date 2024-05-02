from tkinter import *

window = Tk()
window.wm_attributes('-alpha', 0.93)
root = Tk()


window.title("Создание документов для квестов")
window.geometry('1080x730')
window.resizable(width=False, height=False)

root.title("Календарь")
root.geometry('1080x720')

root_frame = Frame(root)
root_frame.place(relwidth=2,relheight=2)

frame = Frame(window)
frame.place(relwidth=1, relheight=1)
