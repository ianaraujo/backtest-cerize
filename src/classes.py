class Porfolio:

    def __init__(self):
        self.holdings = dict()

    def buy(self, ticker: str, amount: int):
        if ticker not in self.holdings.keys():
            self.holdings[ticker] = 0
        
        self.holdings[ticker] += abs(amount)

    def list_holdings(self) -> dict:
        return self.holdings
    
class Tester:

    def __init__(self, portfolio, strategy, years=10):
        self.portfolio = portfolio
        self.strategy = strategy
        self.years = years

    def run(self):
        pass