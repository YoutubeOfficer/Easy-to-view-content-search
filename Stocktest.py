import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf

df_TSLA = yf.download('TSLA', start='2010-01-01', end='2023-12-31', progress=False)
df_AAPL = yf.download('AAPL', start='2010-01-01', end='2023-12-31', progress=False)
plt.plot(df_TSLA['Close'], label='TSLA', color = 'red')
plt.show()