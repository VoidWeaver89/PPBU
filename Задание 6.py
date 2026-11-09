from tkinter import *
from tkinter import ttk

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

currency_label = ttk.Label()
currency_label.pack()

Button(text='Получить курс к доллару').pack(pady=15, padx=10)

root.mainloop()
