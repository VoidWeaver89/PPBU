from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json
import pprint
from bottle import response


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)

# ФУНКЦИЯ ДЛЯ ВТОРОЙ ВАЛЮТЫ
def update_base2_label(event):
    code = base2_combobox.get()
    name = currencies[code]
    base2_label.config(text=name)


# ФУНКЦИЯ ОБМЕНА ДЛЯ ДВУХ ЗАПРОСОВ
def exchange():
    target_code = target_combobox.get().strip()
    base_code = base_combobox.get().strip()
    base2_code = base2_combobox.get().strip()

    if target_code and base_code:
        try:
            # Запрос для первой базовой валюты
            response1 = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response1.raise_for_status()
            data1 = response1.json()

            # Запрос для второй базовой валюты
            response2 = requests.get(f'https://open.er-api.com/v6/latest/{base2_code}')
            response2.raise_for_status()
            data2 = response2.json()

            if target_code in data1['rates']:
                exchange_rate1 = data1['rates'][target_code]
                exchange_rate2 = data2['rates'][target_code]
                base = currencies[base_code]
                base2 = currencies[base2_code]
                target = currencies[target_code]
                # Текст ответа для двух валют сразу
                mb.showinfo('Курсы обмена',
                    f'Курс 1: {exchange_rate1:.1f} {target} за 1 {base}\n'
                            f'Курс 2: {exchange_rate2:.1f} {target} за 1 {base2}')
            else:
                mb.showerror('Ошибка',
                            f'Валюта {target_code} не найдена')
        except Exception as er:
            mb.showerror('Ошибка', er)

    else:
        mb.showwarning('Внимание', 'Выберите все три валюты')


currencies = {
    'EUR': 'Евро',
    'USD': 'Доллар США',
    'JPY': 'Японская йена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'

}

root = Tk()
root.title('Курс обмена валют')
root.geometry('360x300')

# Первая базовая валюта
Label(root, text='Первая базовая валюта').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(pady=3, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label()
base_label.pack()

# Вторая базовая валюта
Label(root, text='Вторая базовая валюта').pack()
base2_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base2_combobox.pack(pady=3, padx=10)
base2_combobox.bind('<<ComboboxSelected>>', update_base2_label)
base2_label = ttk.Label()
base2_label.pack()

# Целевая валюта
Label(root, text='Целевая валюта' ).pack(padx=10)
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(pady=3, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)
target_label = ttk.Label()
target_label.pack()


Button(text='Получить курсы обмена',
       command=exchange).pack(pady=10, padx=10)


root.mainloop()
