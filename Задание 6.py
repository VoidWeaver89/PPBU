from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_currency_label(event):
    code = currency_combobox.get()
    name = cryptos[code]
    currency_label.config(text=name)


# ФУНКЦИЯ ЗАПРОСА КУРСА КРИПТОВАЛЮТЫ К ДОЛЛАРУ
def exchange():
    code = currency_combobox.get().strip()

    if code:
        try:
            # Запрос к CoinGecko — курс выбранной криптовалюты к USD
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={code}&vs_currencies=usd')
            response.raise_for_status()
            data = response.json()

            if code in data:
                exchange_rate = data[code]['usd']
                name = cryptos[code]
                # Текст ответа
                mb.showinfo('Курс криптовалюты',
                            f'Курс: {exchange_rate:.2f} USD за 1 {name}')
            else:
                mb.showerror('Ошибка',
                             f'Валюта {code} не найдена')
        except Exception as er:
            mb.showerror('Ошибка', er)

    else:
        mb.showwarning('Внимание', 'Выберите криптовалюту')


# Популярные криптовалюты: ключ — id в CoinGecko, значение — название
cryptos = {
    'bitcoin': 'Bitcoin (BTC)',
    'ethereum': 'Ethereum (ETH)',
    'tether': 'Tether (USDT)',
    'binancecoin': 'BNB',
    'solana': 'Solana (SOL)',
    'ripple': 'XRP',
    'dogecoin': 'Dogecoin (DOGE)'
}

root = Tk()
root.title('Курс криптовалют к доллару США')
root.geometry('360x180')

# Криптовалюта
Label(root, text='Криптовалюта').pack(padx=10)
currency_combobox = ttk.Combobox(root, values=list(cryptos.keys()), state="readonly")
currency_combobox.pack(pady=3, padx=10)
currency_combobox.bind('<<ComboboxSelected>>', update_currency_label)
currency_label = ttk.Label()
currency_label.pack()


Button(text='Получить курс к доллару',
       command=exchange).pack(pady=15, padx=10)


root.mainloop()
