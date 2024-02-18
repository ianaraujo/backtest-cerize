import random

from src.classes import Porfolio, Tester

ibov = ['BBDC4', 'PETR4', 'VALE3', 'ITUB4']

amostra = random.sample(ibov, 2)

portfolio = Porfolio()

portfolio.build(amostra)
portfolio.buy('BBDC4')

print(portfolio.list_holdings())
