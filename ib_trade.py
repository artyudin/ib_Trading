from functools import wraps
from ib.opt import Connection, message #Import IbPy
from ib.ext.Contract import Contract
from ib.ext.Order import Order

def counter(func):
	@wraps(func)
	def tmp(*args, **kwargs):
		tmp.count += 1
		return func(*args, **kwargs)
	tmp.count = 900
	return tmp

def make_contract(symbol, sec_type, exch, prim_exch, curr):
	Contract.m_symbol = symbol 
	Contract.m_secType = sec_type
	Contract.m_exchange = exch
	Contract.m_primaryExch = prim_exch
	Contract.m_currency = curr
	return Contract

def make_order(action, quantity, price=None):
	if price is not None:
		order = Order()
		order.m_orderType = 'LMT'
		order.m_totalQuantity = quantity
		order.m_action = action
		order.m_action = action

	else:
		order = Order()
		order.m_orderType = 'MKT'
		order.m_totalQuantity = quantity
		order.m_action = action

	return order

@counter
def main():
	conn = Connection.create(port=7497, clientId=999) #Has to be connected to Global settings of TWS
	conn.connect()
	oid = main.count #Order number
	print (oid)

	cont = make_contract('AAPL', 'STK', 'SMART', 'SMART', 'USD') #Check exch name for stock symbol

	offer = make_order('BUY', 300)

	conn.placeOrder(oid, cont, offer)
	conn.disconnect()


main()
main()
main()
main()














