import os #operation system
#讀取檔案
product = []
if os.path.isfile('products.csv'): #檢查檔案在不在
	print('The file is found')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name, price])
		print(product)
else:
	print('File not found...')

#讓使用者輸入
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

#印出所有購買紀錄
for p in product:
	print(p[0], '的價格是', p[1]) #知道for loop和二維清單拿出來的東西是什麼
#p[0]是第一個小清單的商品名, p[1]是價格

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #'w'是寫入模式, 'r'是讀取
	f.write('商品,價格\n')
	for p in product:
		f.write(p[0] + ',' +p[1] + '\n') #字串疊加功能 ',' 是excel中寫到下個儲存格的方式
		#\n是換行符號



