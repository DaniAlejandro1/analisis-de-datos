import requests as req
import pandas as pd
from IPython.display import display, Markdown


pd.set_option('display.max_columns', None)  # Show all columns in the DataFrame
pd.set_option('display.max_rows', None)  # Show all rows in the DataFrame


pd.set_option('display.float_format', '{:,.2f}'.format)  # coma para miles, 2 decimales, por defecto estaba entregando valores en notacion cientifica

class Data:
    r = req.get('https://restcountries.com/v3.1/all')
    data = r.json()

data = Data()

