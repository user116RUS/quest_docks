import os

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
    docs = ['dogovor.docx', 'act_priemki.docx', 'schet.docx']
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
            'cost': btn_cost.get(),
            'customer': btn_inf.get(),
            'customer_short': btn_customer_short.get(),
            'doer_full': current_doer['requisites'],
            'name': btn_director.get(),
            'amount': btn_mon.get(),
            'amount_text': btn_amount_text.get(),
            'quantity_number': str(btn_quan.get())[:int(btn_quan.get().find(' '))],
            'doer_fio': current_doer['fio'],
            'schet_num': btn_schet_num.get(),
            'agreement_number': btn_agreement_number.get(),
            'customer_adress': btn_customer_adress.get(),
            'doer_bank_name': current_doer['bank_name'],
            'doer_inn': current_doer['inn'],
            'doer_short_name': current_doer['short_name'],
            'doer_bik': current_doer['bik'],
            'doer_bik_schet': current_doer['bik_schet'],
            'doer_schet': current_doer['schet'],
            'doer_kpp': current_doer['kpp'],
            'doer_adress': current_doer['adress']
        }

        os.mkdir(f'files/{btn_customer_short.get()[:15]}')

        for doc in docs:
            file_name = f"files/{btn_customer_short.get()[:15]}/{doc[:5]}.docx"
            doc = DocxTemplate(doc)
            doc.render(context)
            doc.save(file_name)
        messagebox.showinfo(title='J-GET', message=f'Успешно создали файs')
    except Exception as e:
        os.rmdir(f'files/{btn_customer_short.get()[:15]}')
        messagebox.showerror(title='J-GET', message=f'Не удалось, причина: {e}')


"""
Elements
"""


company = Label(frame, text='Введите наименование учреждения:', font=("Arial", 11), anchor="e")
company.grid(column=0, row=0)
company_enter = Entry(frame, width=50)
company_enter.grid(column=1, row=0)
company_ex = Label(
    frame, text='Пример: Муниципальное автономное общеобразовательное\n'
                ' учреждение города Набережные Челны "Средняя общеобразовательная \nшкола №50 с углубленным изучением'
                'отдельных предметов",\n в лице директора Ахметзянова Рамиля Рустамовича')
company_ex.grid(column=1, row=1)


dicta = Label(frame, text='Введите название вашей услуги:', anchor="e", font=("Arial", 11))
dicta.grid(column=0, row=2)
btn_dicta = Entry(frame, width=50)
btn_dicta.grid(column=1, row=2)
dicta_ex = Label(frame, text='Пример: проведение научно-технического квеста', cursor='xterm')
dicta_ex.grid(column=1, row=3)


quan = Label(
    frame,
    text='Kоличество человек число, скобках словами:', font=("Arial", 11)
)
quan.grid(column=0, row=4)
btn_quan = Entry(frame, width=50)
btn_quan.grid(column=1, row=4)
quan_ex = Label(frame, text='Пример: 100 (Сто)', cursor='xterm')
quan_ex.grid(column=1, row=5)


date_time = Label(frame, text='Введите дату:', justify='right', font=("Arial", 11))
date_time.grid(column=0, row=6)
btn_time = Entry(frame, width=50)
btn_time.grid(column=1, row=6)
date_time_ex = Label(frame, text='Пример: "15"  июня 2023', cursor='xterm')
date_time_ex.grid(column=1, row=7)


place = Label(frame, text='Введите адрес и время проведения:', justify='right', font=("Arial", 11))
place.grid(column=0, row=8)
btn_place = Entry(frame, width=50)
btn_place.grid(column=1, row=8)
place_ex = Label(
    frame,
    text='г. Набережные Челны, ул. Шамиля Усманова, д.19. Время проведения: с 09:30', cursor='xterm'
    )
place_ex.grid(column=1, row=9)


mon = Label(frame, text='Введите цену (цифрами):', justify='right', font=("Arial", 11))
mon.grid(column=0, row=10)
btn_mon = Entry(frame, width=50)
btn_mon.grid(column=1, row=10)
mon_ex = Label(frame, text='Пример: 17 000')
mon_ex.grid(column=1, row=11)


amount_text = Label(frame, text='Введите цену (Словами):', font=("Arial", 11))
amount_text.grid(column=0, row=12)
btn_amount_text = Entry(frame, width=50)
btn_amount_text.grid(column=1, row=12)
amount_text_ex = Label(frame, text='Пример: семнадцать тысяч')
amount_text_ex.grid(column=1, row=13)


inf = Label(frame, text='Введите информация о заказчике:', justify='right', font=("Arial", 11))
inf.grid(column=0, row=14)
btn_inf = Entry(frame, width=50)
btn_inf.grid(column=1, row=14)
inf_ex = Label(frame, text='Карта партнера')
inf_ex.grid(column=1, row=15)


director = Label(frame, text='Введите имя директора', font=("Arial", 11))
director.grid(column=0, row=16)
btn_director = Entry(frame, width=50)
btn_director.grid(column=1, row=16)
director_ex = Label(frame, text='Пример: Р.Р. Ахметзянов')
director_ex.grid(column=1, row=17)


time_delta = Label(frame, text='Время проведения:', font=("Arial", 11))
time_delta.grid(column=0, row=18)
btn_time_delta = Entry(frame, width=50)
btn_time_delta.grid(column=1, row=18)
time_delta_ex = Label(frame, text='Пример: 09:30-10:30', cursor='xterm')
time_delta_ex.grid(column=1, row=19)


customer_short = Label(frame, text='Заказчик коротко:', font=("Arial", 11))
customer_short.grid(column=0, row=20)
btn_customer_short = Entry(frame, width=50)
btn_customer_short.grid(column=1, row=20)
customer_short_ex = Label(frame, text='МАОУ «Средняя школа №50»')
customer_short_ex.grid(column=1, row=21)


cost = Label(frame, text='Введите стоимость:', justify='right', font=("Arial", 11))
cost.grid(column=0, row=22)
btn_cost = Entry(frame, width=50)
btn_cost.grid(column=1, row=22)
cost_ex = Label(frame, text='100')
cost_ex.grid(column=1, row=23)


doer_label = Label(frame, text='Исполнитель:', justify='right', font=("Arial", 11))
doer_label.grid(column=0, row=24)
languages = ["ИП Мотыгуллин", "ООО Алгарыш",]
doer = ttk.Combobox(frame, values=languages)
doer.grid(column=1, row=24)

schet_num = Label(frame, text='Введите номер акта и счета:', justify='right', font=("Arial", 11))
schet_num.grid(column=0, row=25)
btn_schet_num = Entry(frame, width=50)
btn_schet_num.grid(column=1, row=25)
schet_num_ex = Label(frame, text='50/1 от 15 июня 2023 г.', cursor='xterm')
schet_num_ex.grid(column=1, row=26)


agreement_number = Label(frame, text='Введите номер основание договора:', justify='right', font=("Arial", 11))
agreement_number.grid(column=0, row=27)
btn_agreement_number = Entry(frame, width=50)
btn_agreement_number.grid(column=1, row=27)
agreement_number_ex = Label(frame, text='№ 50/23-11 от 18.05.2023 г', cursor='xterm')
agreement_number_ex.grid(column=1, row=28)


customer_adress = Label(frame, text='Введите юр адрес школы:', justify='right', font=("Arial", 11))
customer_adress.grid(column=0, row=29)
btn_customer_adress = Entry(frame, width=50)
btn_customer_adress.grid(column=1, row=29)


btn_company = Button(frame, text="Создать документы", command=clicked)
btn_company.grid(column=3, row=29)
