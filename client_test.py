import unittest
from client3 import *

def throw_ex(priceA,priceB):
    if int(priceB) == 0 :
      return
    return priceA/priceB
    
class ClientTest(unittest.TestCase):
  def setUp(self):
      self.quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
          'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
          'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

  def test_getDataPoint_calculatePrice(self):
    for quote in self.quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'],
                       quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
  

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
          'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
          'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'],
                       quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getRatio(self):
    prices = {}
    for quote in self.quotes:
      stock,bid_price,ask_price,price = getDataPoint(quote)
      prices[stock] = price
    self.assertEqual(getRatio(prices['ABC'], prices['DEF']), (prices['ABC']/prices['DEF']))
  
      
  def test_IfPriceAIsZero(self):
      quotes = [
          {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
           'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {'price': 119.2, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
           'top_bid': {'price': 120.48, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      ]
      prices = {}
      for quote in quotes:
        price = (quote['top_bid']['price'] + quote['top_ask']['price'])/2
        prices[quote['stock']] = price 
      
      self.assertEqual(getRatio(prices['ABC'], prices['DEF']), throw_ex(prices['ABC'],prices['DEF']))
            
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(ClientTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
