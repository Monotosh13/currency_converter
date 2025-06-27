Currency Converter GUI App

A simple and user-friendly currency converter desktop application built with Python and Tkinter. The app fetches real-time exchange rates from an online API and allows you to convert any amount between supported currencies.
Features

    Live exchange rates using ExchangeRate-API

    Easy-to-use graphical interface (Tkinter)

    Supports multiple currencies

    Input validation and error handling

Screenshots

(Add your own screenshots here if desired)
Requirements

    Python 3.7 or higher

    Internet connection (for fetching live rates)

    Dependencies listed in requirements.txt

Installation

    Clone the repository or download the source code:

bash
git clone https://github.com/Monotosh13/currency_converter.git
cd currency_converter

Install dependencies:

    bash
    pip install -r requirements.txt

File Structure

text
currency_converter/
│
├── main.py          # Entry point for the GUI app
├── converter.py     # Core logic for currency conversion and API calls
└── requirements.txt # List of Python dependencies

Usage

    Run the application:

    bash
    python main.py

    How to use:

        Enter the amount you wish to convert.

        Select the source currency (From).

        Select the target currency (To).

        Click the Convert button.

        The converted amount will be displayed below.

Notes

    The app fetches exchange rates in real-time from the ExchangeRate-API. An active internet connection is required.

    If you encounter API errors or network issues, an error message will be displayed.

    You can extend the app by adding more features or customizing the UI as needed.

Troubleshooting

    No internet connection: Ensure you are connected to the internet to fetch the latest exchange rates.

    Module not found: Make sure you have installed all dependencies with pip install -r requirements.txt.

    API changes: If the API endpoint changes or is deprecated, update the URL in converter.py.
