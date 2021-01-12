product = []
while True:
	name = input('Please enter the product name: ')
	if name == 'q':
		break
	price = input('Please enter the price: ')
	p = []
	# p.append(name)
	# p.append(price)跟第10行一樣意思
	# p = [name, price]
	product.append([name, price]) #比第10行更簡潔的寫法
print(product)

