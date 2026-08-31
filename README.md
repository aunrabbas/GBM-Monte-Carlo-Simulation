# GBM Monte Carlo Simulation

A stock price simulator built on Geometric Brownian Motion. Takes any ticker, pulls historical data, and simulates 1000 possible future price paths over the next trading year. Color coded by final price, with a matching histogram and VaR displayed in the title.

<img width="1000" height="514" alt="Screenshot 2026-08-10 at 8 54 45 PM" src="https://github.com/user-attachments/assets/cb2a18fe-d376-4355-b27e-d882d0605389" />


## What it does
- Downloads historical price data for any ticker via yfinance
- Calculates mean daily return and volatility from that historical data
- Simulates 1000 future price paths using GBM, each with a unique sequence of random shocks
- Color codes every path by its final price, warm colors (red) for lower outcomes, cool colors (blue) for higher
- Renders a side-by-side layout: simulation paths on the left, final price distribution histogram on the right
- Calculates and displays Value at Risk (VaR) at 95% confidence directly in the title

## Why GBM

Stock prices have two components every day: a general drift based on historical average return, and a random shock based on historical volatility. GBM models both simultaneously.

The drift uses the σ²/2 correction to account for the asymmetry of log normal distributions. Without it, simulated paths systematically drift too high. The random shocks are drawn from a normal distribution, scaled by historical volatility, which gives each simulation realistic day-to-day movement without predicting any specific outcome.

## What VaR actually means

Value at Risk at 95% confidence answers: across 1000 simulated futures, what is the worst price I should expect in 95% of scenarios?

The remaining 5% are the tail risk scenarios. VaR doesn't say those can't happen, it just tells you where the floor is for most realistic outcomes.

## Stack

```
yfinance     — historical price data
pandas       — return and volatility calculations
numpy        — GBM simulation, random normal generation
matplotlib   — dual panel visualization with colormap
```

## Usage

```bash
pip install yfinance pandas numpy matplotlib
python monte_carlo.py
```

Enter any valid ticker when prompted.

## How to read the chart

- Every line is one possible future for the stock over the next 252 trading days
- Red paths ended lower, blue paths ended higher
- The histogram on the right shows the distribution of all 1000 final prices
- The spread of paths widens over time because uncertainty compounds
- A high volatility stock like NVDA spreads much wider than a low volatility one like SPY

---

Built to understand how risk is actually modeled in quantitative finance, not just visualized.
