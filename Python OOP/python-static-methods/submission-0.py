class CurrencyConverter:
    rates = {  
        'EUR': 1.20,  # 1 EUR = 1.20 USD
        'JPY': 0.01   # 1 JPY = 0.01 USD
    } # Class Mountain

    # static methods don't have access to self or cls
    # do not have access to instance attributes
    # can still access class attributes using the class name
    # belongs to class rather than specific object instance

    @staticmethod
    def to_usd(amount, from_currency):
        return amount * CurrencyConverter.rates[from_currency]
    




        
    

print(f"100 EUR = {CurrencyConverter.to_usd(100, 'EUR')} USD")     # 120 USD
print(f"100 JPY = {CurrencyConverter.to_usd(100, 'JPY')} USD")     # 1 USD
