import yfinance as yf
import matplotlib.pyplot as plt 
import matplotlib.colors as clr 
import math as math 
import pandas as pd
import numpy as np


while True:
    stock = input("What stock do you want to analyze? (Example: AAPL, NVDA etc)")
    data = pd.DataFrame(yf.download(stock, period='3y'))["Close"]
    if data.empty:
        print("Try again, please use the ticker symbol!")
        continue
    else:
        break




mean_ret = data.pct_change().mean().mean() 
vol = (data.pct_change().std())[stock.upper()]

Simulations = []
final_values = []

plt.style.use('dark_background')
figure , axes = plt.subplots(1,2, gridspec_kw = {'width_ratios': [5,2]})

def Simulate_Stock():
    drift = (mean_ret - ((vol)**2)/2 )*(1/756)
    for i in range(1000):
        sim = []
        sim.append(data[stock.upper()].iloc[-1])
        for x in range(1, 756):
                shock = vol * np.random.normal() * math.sqrt(1/756)
                sim.append(sim[x-1] * math.e**(drift + shock))
        final_values.append(float(sim[-1]))
        Simulations.append(sim)

Simulate_Stock()


#colormap
cmp = plt.colormaps['RdYlBu']
color_norm = clr.Normalize(min(final_values),max(final_values))
n, bins, patches = axes[1].hist(final_values, 20, orientation = 'horizontal' )
patch_norm = clr.Normalize(patches[0].get_xy()[1],patches[-1].get_xy()[1])    




def Plot_Stock():
     for i in range(len(Simulations)):
          axes[0].plot(Simulations[i], color = cmp(color_norm(final_values[i])))
     for i in range(len(patches)):
          patches[i].set_facecolor(cmp(patch_norm(patches[i].get_xy()[1])))
          
     



Plot_Stock()

axes[1].tick_params(labelleft=False)
percentile = np.percentile(final_values, 5)
axes[0].set_xlabel("Days")
axes[0].set_ylabel("Stock Price $")

plt.suptitle(f"GBM Monte Carlo Simulation \nTicker Symbol: {stock.upper()}\n VaR: ${percentile:.2f}")
figure.tight_layout()
plt.show()
