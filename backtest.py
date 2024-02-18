from src.classes import Porfolio, Tester

p1 = Porfolio()

p1.buy('AAPL', 300)
p1.buy('AAPL', 200)
p1.buy('GOOGL', 200)
p1.buy('META', 200)

print(p1.list_holdings())
