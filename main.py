from docxtpl import DocxTemplate
from tkinter import *


def clicked():
    doc = DocxTemplate("file.docx")
    context = {
        'company': str(company_btn.get()),
        'dictionary': str(btn_dicta.get()),
        'quantity': str(btn_quan.get()),
        'time': str(btn_time.get()),
        'place': str(btn_place.get()),
        'money': str(btn_mon.get()),
        'hz': str(btn_inf.get()),
        'name': str(btn_director.get())
    }

    doc.render(context)

    doc.save("save.docx")


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('1920x1080')

company = Label(window, text='Введите наименование вашего учреждения \n (Пример: Муниципальное автономное общеобразовательное учреждение города Набережные Челны "Средняя общеобразовательная школа №50 с углубленным изучением отдельных предметов", в лице директора Ахметзянова Рамиля Рустамовича))')
company.grid(column=0, row=0)
company_btn = Entry(window, width=50)
company_btn.grid(column=0, row=1)

dicta = Label(window, text='Введите название вашей услуги \n (Пример: проведение научно-технического квеста)')
dicta.grid(column=0, row=2)
btn_dicta = Entry(window, width=25)
btn_dicta.grid(column=0, row=3)

quan = Label(window, text='Введите количество человек сначала число, а потом в скобках словами \n (Пример: 100 (Сто))')
quan.grid(column=0, row=4)
btn_quan = Entry(window, width=25)
btn_quan.grid(column=0, row=5)

time = Label(window, text='Введите дату \n (Пример: "15"  июня 2023)')
time.grid(column=0, row=6)
btn_time = Entry(window, width=25)
btn_time.grid(column=0, row=7)

place = Label(window, text='Введите адрес и время \n (Пример: г. Набережные Челны, ул. Шамиля Усманова, д.19. Время проведения: с 09:30) ')
place.grid(column=0, row=8)
btn_place = Entry(window, width=50)
btn_place.grid(column=0, row=9)

mon = Label(window, text='Введите цену \n (Пример: 17 000 (Семнадцать тысяч))')
mon.grid(column=0, row=10)
btn_mon = Entry(window, width=25)
btn_mon.grid(column=0, row=11)

inf = Label(window, text='Введите информация о заказчике')
inf.grid(column=0, row=12)
btn_inf = Entry(window, width=125)
btn_inf.grid(column=0, row=13)

director = Label(window, text='Введите имя директора \n (Пример: Р.Р. Ахметзянов)')
director.grid(column=0, row=14)
btn_director = Entry(window, width=25)
btn_director.grid(column=0, row=15)





btn_company = Button(window, text="Нажмите, когда все ввели", command=clicked)
btn_company.grid(column=0, row=16)
window.mainloop()

