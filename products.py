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

for p in product:
	print(p[0], '的價格是', p[1]) #知道for loop和二維清單拿出來的東西是什麼
#p[0]是第一個小清單的商品名, p[1]是價格	

