This project investigates the risk-return trade-off within the S&P 500, focusing on how risk, as measured by volatility, influences stock returns. The project goes on to further investigate how sector-specific risk impacts stock returns.  The study tests two key hypotheses derived from the Capital Asset Pricing Model (CAPM) and sector-specific dynamics:
  1.	Stocks with more volatility than the market deliver average daily returns that are at least 20% higher than stocks with equal/lower volatility than the market, consistent with the Capital Asset Pricing Model.
Supported by the data. High-beta stocks showed significantly higher average daily returns compared to low-beta stocks. However, beta alone is not a robust predictor of returns – inconsistent with the CAPM.
  2.	Sector is the most important feature in determining average daily returns due to its influence on risk profiles.
Not supported. Sector was not the most significant factor in predicting returns. Instead, volatility, dividend yield, and beta emerged as stronger predictors, with sector playing a secondary role.
The analysis revealed that while CAPM’s prediction of a positive relationship between beta and returns holds to some extent, the model’s linear assumptions are insufficient to fully explain stock returns. There is no overarching factor -whether risk or sector- to entirely model returns. Stock returns can be thought of as broader trends and multi-factor models, as the risk-return relationship is influenced by a variety of factors.


Introduction and Motivation
The risk-return trade-off is a fundamental principle of investment, that states potential returns increase with an increase in risk (Chen, J., 2024). This project investigates this relationship within stocks that are components of the S&P 500, focusing on how sector-specific risk metrics such as volatility influence returns.
The Capital Asset Pricing Model (CAPM), developed by William Sharpe and John Lintner in the 1960s, formalises the risk-return trade-off by establishing a linear relationship between the risk and expected return of an asset. Sharpe presented A theory of market equilibrium under conditions of risk where he argued that a rational investor can only obtain a higher expected rate of return on their investments by incurring additional risk (Sharpe, W., 1964) as represented in Figure 1, where the capital market line illustrates the trade-off between risk and return. Beyond the interest rate (risk free rate of return), investors incur additional risk for higher expected rates of return.
 
Figure 1: A representation of William's Sharpe's view of the capital market from A theory of market equilibrium under conditions of risk (Sharpe, W., 1964)
 
The CAPM formula is expressed as:
ER_i=R_f+ β_i (ER_m-R_f)
where: 
〖ER〗_i= expected return of investment 
R_f= risk free rate of return (2.3% for this study, based on 5-year Treasury yields from 2018)
β_i= beta of the investment  (volatility relative to the market)
ER_m-R_f=market risk premium (expected return of the market minus the risk-free rate)
Beta (β) measures an asset’s volatility relative to a benchmark such as the S&P500 representative of behaviour of the general market. A beta of greater than 1 indicates higher volatility than the market while a beta less than 1 suggests lower. Investors often target high beta, taking on more risk in hopes to gain from the volatility.
β=Covariance(R_e ,R_m )/Variance(R_m ) 
where: 
R_e= the return on an individual stock 
R_m= the return on the overall market (benchmark)
This project tests two key hypotheses derived from CAPM and sector-specific risk-return dynamics:
	"Stocks with a beta higher than 1.0 deliver average daily returns that are at least 20% higher than stocks with a beta lower than 1.0, consistent with the Capital Asset Pricing Model prediction."
	“As Sector is a key determiner of risk profile, it acts as the most important feature in determining average daily returns”
These hypotheses are rooted in financial theory, and the principles of the risk-return trade-off. The first hypothesis addresses the theory that greater systematic risk should offer higher returns as compensation. The second hypothesis builds on the observations of similar sector dynamics, where companies often exhibit similar risk-return profiles due to factors such as regulatory environments and technological advancements. 
For instance, the Technology sector, characterized by rapid innovation and high growth potential, often experiences wide dispersion in returns, presenting both opportunities and risks for investors (Cutter, P., 2024). Similarly, sectors like Energy and Consumer Discretionary exhibit distinct risk profiles driven by commodity price fluctuations and consumer demand cycles, respectively. 
By analysing data from the components of the S&P 500 for 5 years (2020-2024) this study employs various statistical and machine learning techniques to examine the validity of these hypotheses and provide a data driven perspective on the relationship between risk and return.
