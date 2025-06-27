# main.py

import tkinter as tk
from tkinter import ttk, messagebox
from converter import CurrencyConverter

def main():
    converter = CurrencyConverter()
    currencies = list(converter.rates.keys())

    def perform_conversion():
        try:
            amount = float(amount_var.get())
            from_curr = from_currency_var.get()
            to_curr = to_currency_var.get()
            result = converter.convert(amount, from_curr, to_curr)
            result_var.set(f"{result} {to_curr}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input or API error: {e}")

    root = tk.Tk()
    root.title("Currency Converter")

    # Variables
    amount_var = tk.StringVar()
    from_currency_var = tk.StringVar(value="USD")
    to_currency_var = tk.StringVar(value="EUR")
    result_var = tk.StringVar()

    # Layout
    ttk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
    ttk.Entry(root, textvariable=amount_var).grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(root, text="From:").grid(row=1, column=0, padx=10, pady=10)
    ttk.Combobox(root, textvariable=from_currency_var, values=currencies, state="readonly").grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(root, text="To:").grid(row=2, column=0, padx=10, pady=10)
    ttk.Combobox(root, textvariable=to_currency_var, values=currencies, state="readonly").grid(row=2, column=1, padx=10, pady=10)

    ttk.Button(root, text="Convert", command=perform_conversion).grid(row=3, column=0, columnspan=2, pady=10)
    ttk.Label(root, textvariable=result_var, font=("Arial", 14)).grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

#Notes:

#    The GUI uses Tkinter for simplicity.

#    amount_var, from_currency_var, and to_currency_var store user input.

#    perform_conversion() calls the converter and updates the result.

#    Error handling is included for user input and API errors.

#    The layout is simple and user-friendly.
