from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_base_label(event):
    code = base_combobox.get()
    name = cryptos[code]
    base_label.config(text=name)


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def exchange():
    base_code = base_combobox.get().strip()
    target_code = target_combobox.get().strip()

    # Запрос к Binance — цена выбранной криптовалюты в долларах (USDT)
    crypto_response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={base_code}USDT')
    crypto_data = crypto_response.json()
    price_in_usd = float(crypto_data['price'])

    # Запрос курса доллара США к выбранной целевой валюте
    fiat_response = requests.get('https://open.er-api.com/v6/latest/USD')
    fiat_data = fiat_response.json()
    usd_to_target = fiat_data['rates'][target_code]

    # Перемножаем цену в долларах на курс доллара к целевой валюте
    exchange_rate = price_in_usd * usd_to_target

    base = cryptos[base_code]
    target = currencies[target_code]

    # Вывод итогового результата
    mb.showinfo('Курс обмена',
                f'Курс: {exchange_rate:.4f} {target} ({target_code}) за 1 {base}')


# Популярные криптовалюты: ключ — тикер для Binance, значение — название
cryptos = {
    'BTC': 'Bitcoin (BTC)',
    'ETH': 'Ethereum (ETH)',
    'BNB': 'BNB (Binance Coin)',
    'SOL': 'Solana (SOL)',
    'XRP': 'XRP (Ripple)',
    'DOGE': 'Dogecoin (DOGE)'
}

# Целевые валюты: ключ — код валюты, значение — название
currencies = {
    'USD': 'Доллар США',
    'EUR': 'Евро',
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
root.title('КрипТрейс — Курсы криптовалют')
root.geometry('420x250')

# Базовая валюта (криптовалюта)
Label(root, text='Базовая валюта (криптовалюта)').pack(pady=(10, 0))
base_combobox = ttk.Combobox(root, values=list(cryptos.keys()), state="readonly")
base_combobox.pack(pady=3, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label(foreground='gray')
base_label.pack()

# Целевая валюта (валюта расчета)
Label(root, text='Целевая валюта').pack(pady=(10, 0), padx=10)
target_combobox = ttk.Combobox(root, values=list(currencies.keys()), state="readonly")
target_combobox.pack(pady=3, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)
target_label = ttk.Label(foreground='gray')
target_label.pack()

Button(text='Получить курс обмена', command=exchange).pack(pady=15, padx=10)

root.mainloop()
