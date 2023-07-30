import random
answer = random.randint(1, 100)

while True:
	x = input('請猜數字：')
	x = int(x)
	if x == answer:
		print('恭喜答對！')
		break
	elif x < answer:
		print('再大一些')
	elif x > answer:
		print('再小一些')