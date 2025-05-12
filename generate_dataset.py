import yfinance as yf
import numpy as np
import pandas as pd

# Fetch list of S&P 500 stocks from Wikipedia
sp_assets = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
sp500_data = sp_assets[0][['Symbol', 'GICS Sector']]
sp500_data.columns = ['Symbol', 'Sector']
tickers = sp500_data['Symbol'].tolist()

# Define the benchmark (S&P 500 index)
benchmark_symbol = "^GSPC"
start_date = "2020-01-01"
end_date = "2024-12-31"
risk_free_rate = 0.016  # 1.6% annual rate

# Download benchmark data
print("Fetching benchmark data...")
benchmark_data = yf.download(benchmark_symbol, start=start_date, end=end_date, progress=False)
benchmark_returns = benchmark_data['Adj Close'].pct_change()

# Placeholder for data
summary_data = []

# Process data for each stock
print("Fetching stock data...")
for ticker in tickers:
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        stock_returns = stock_data['Adj Close'].pct_change()

        # Calculate risk measures
        beta = np.cov(stock_returns[1:], benchmark_returns[1:])[0, 1] / benchmark_returns[1:].var()
        volatility = stock_returns.std()

        # Calculate return measures
        avg_daily_return = stock_returns.mean()
        total_return = (stock_data['Adj Close'][-1] / stock_data['Adj Close'][0]) - 1

        # Calculate Sharpe Ratio (using risk-free rate of 2.3%)
        sharpe_ratio = (avg_daily_return - 0.023/252) / volatility if volatility != 0 else np.nan

        # Calculate CAPM Expected Return
        capm_expected_return = (risk_free_rate / 252) + beta * (benchmark_returns.mean() - (risk_free_rate / 252))

        # Average trading volume
        avg_volume = stock_data['Volume'].mean()
        
        # Other financial metrics
        stock_info = yf.Ticker(ticker).info
        market_cap = stock_info.get('marketCap')
        pe_ratio = stock_info.get('trailingPE')
        dividend_yield = stock_info.get('dividendYield')
        de_ratio = stock_info.get('debtToEquity')

        # Append results
        summary_data.append({
            'Symbol': ticker,
            'Sector': sp500_data.loc[sp500_data['Symbol'] == ticker, 'Sector'].values[0],
            'Beta': beta,
            'Volatility': volatility,
            'Sharpe_Ratio': sharpe_ratio,
            'Avg_Daily_Return': avg_daily_return,
            'Total_Return': total_return,
            'Avg_Volume': avg_volume,
            'CAPM_Expected_Return': capm_expected_return,
            'Market_Cap': market_cap,
            'PE_Ratio': pe_ratio,
            'Dividend_Yield': dividend_yield,
            'DE_Ratio': de_ratio
        })
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

# Convert to DataFrame and save to CSV
summary_df = pd.DataFrame(summary_data)
summary_df.to_csv("sp500_risk_return_dataset.csv", index=False)

# Display first few rows
print("Dataset generated successfully!")
print(summary_df.head())
