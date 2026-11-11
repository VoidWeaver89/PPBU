from tkinter import *
from tkinter import ttk

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

# Целевая валюта (валюта расчета)
Label(root, text='Целевая валюта').pack(pady=(10, 0), padx=10)
target_combobox = ttk.Combobox(root, values=list(currencies.keys()), state="readonly")
target_combobox.pack(pady=3, padx=10)

Button(text='Получить курс обмена').pack(pady=15, padx=10)

root.mainloop()
