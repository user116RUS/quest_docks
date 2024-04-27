from docxtpl import DocxTemplate
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

from config import frame
from doers_info import doers_info


"""
Actions
"""


def clicked():
    doc = DocxTemplate("file.docx")
    try:
        current_doer = doers_info['Motigullin'] if doer.get() == 'ИП Мотыгуллин' else doers_info['Algarish']

        context = {
            'company': company_enter.get(),
            'doer': current_doer['name'],
            'service': btn_dicta.get(),
            'quantity': btn_quan.get(),
            'time': btn_time.get(),
            'time_delta': btn_time_delta.get(),
            'place': btn_place.get(),
            'money': btn_mon.get(),
            'customer': btn_inf.get(),
            'customer_short': btn_customer_short.get(),
            'doer_full': current_doer['requisites'],
            'name': btn_director.get(),
            'amount': str(btn_mon.get())[:int(btn_mon.get().find(' '))],
            'quantity_number': str(btn_quan.get())[:int(btn_quan.get().find(' '))],
            'doer_fio': current_doer['fio'],
            'cost': str()
        }

        doc.render(context)
        file_name = f"files/{btn_customer_short.get()}.docx"
        doc.save(file_name)
        messagebox.showinfo(title='J-GET', message=f'Успешно создали файл {file_name}')
    except Exception as e:
        messagebox.showerror(title='J-GET', message=f'Не удалось, причина: {e}')


"""
Elements
"""


company = Label(frame, text='Введите наименование учреждения:', font=("Arial", 14), anchor="e")
company.grid(column=0, row=0)
company_enter = Entry(frame, width=50)
company_enter.grid(column=1, row=0)
company_ex = Label(
    frame, text='Пример: Муниципальное автономное общеобразовательное\n'
                ' учреждение города Набережные Челны "Средняя общеобразовательная \nшкола №50 с углубленным изучением'
                'отдельных предметов",\n в лице директора Ахметзянова Рамиля Рустамовича')
company_ex.grid(column=1, row=1)


dicta = Label(frame, text='Введите название вашей услуги:', anchor="e", font=("Arial", 14))
dicta.grid(column=0, row=2)
btn_dicta = Entry(frame, width=50)
btn_dicta.grid(column=1, row=2)
dicta_ex = Label(frame, text='Пример: проведение научно-технического квеста')
dicta_ex.grid(column=1, row=3)


quan = Label(
    frame,
    text='Введите количество человек сначала число, а потом в скобках словами:', justify='right', font=("Arial", 14)
)
quan.grid(column=0, row=4)
btn_quan = Entry(frame, width=50)
btn_quan.grid(column=1, row=4)
quan_ex = Label(frame, text='Пример: 100 (Сто)')
quan_ex.grid(column=1, row=5)


date_time = Label(frame, text='Введите дату:', justify='right', font=("Arial", 14))
date_time.grid(column=0, row=6)
btn_time = Entry(frame, width=50)
btn_time.grid(column=1, row=6)
date_time_ex = Label(frame, text='Пример: "15"  июня 2023')
date_time_ex.grid(column=1, row=7)


place = Label(frame, text='Введите адрес и время:', justify='right', font=("Arial", 14))
place.grid(column=0, row=8)
btn_place = Entry(frame, width=50)
btn_place.grid(column=1, row=8)
place_ex = Label(frame, text='г. Набережные Челны, ул. Шамиля Усманова, д.19. Время проведения: с 09:30')
place_ex.grid(column=1, row=9)


mon = Label(frame, text='Введите стоимость:', justify='right', font=("Arial", 14))
mon.grid(column=0, row=10)
btn_mon = Entry(frame, width=50)
btn_mon.grid(column=1, row=10)
mon_ex = Label(frame, text='Пример: 17000 (Семнадцать тысяч)')
mon_ex.grid(column=1, row=11)


inf = Label(frame, text='Введите информация о заказчике:', justify='right', font=("Arial", 14))
inf.grid(column=0, row=12)
btn_inf = Entry(frame, width=50)
btn_inf.grid(column=1, row=12)
inf_ex = Label(frame, text='Карта партнера')
inf_ex.grid(column=1, row=13)


director = Label(frame, text='Введите имя директора', font=("Arial", 14))
director.grid(column=0, row=14)
btn_director = Entry(frame, width=50)
btn_director.grid(column=1, row=14)
director_ex = Label(frame, text='Пример: Р.Р. Ахметзянов')
director_ex.grid(column=1, row=15)


time_delta = Label(frame, text='Время проведения:', font=("Arial", 14))
time_delta.grid(column=0, row=16)
btn_time_delta = Entry(frame, width=50)
btn_time_delta.grid(column=1, row=16)
time_delta_ex = Label(frame, text='Пример: 09:30-10:30')
time_delta_ex.grid(column=1, row=17)

customer_short = Label(frame, text='Заказчик коротко:', font=("Arial", 14))
customer_short.grid(column=0, row=18)
btn_customer_short = Entry(frame, width=50)
btn_customer_short.grid(column=1, row=18)
customer_short_ex = Label(frame, text='МАОУ «Средняя школа №50»')
customer_short_ex.grid(column=1, row=19)


cost = Label(frame, text='Введите стоимость:', justify='right', font=("Arial", 14))
cost.grid(column=0, row=20)
btn_cost = Entry(frame, width=50)
btn_cost.grid(column=1, row=20)
cost_ex = Label(frame, text='100')
cost_ex.grid(column=1, row=21)


doer_label = Label(frame, text='Исполнитель:', justify='right', font=("Arial", 14))
doer_label.grid(column=0, row=22)
languages = ["ИП Мотыгуллин", "ООО Алгарыш",]
doer = ttk.Combobox(frame, values=languages)
doer.grid(column=1, row=22)


btn_company = Button(frame, text="Создать документы", command=clicked)
btn_company.grid(column=0, row=23)
