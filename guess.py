import random
answer = random.randint(1, 100)
count = 0
while True:
	x = input('請猜數字：')
	x = int(x)
	count += 1
	if x == answer:
		print('恭喜答對！')
		print('你已經猜了', count, '次')
		break
	elif x < answer:
		print('再大一些')
	elif x > answer:
		print('再小一些')
	print('你已經猜了', count, '次')