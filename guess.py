import random

start = input('請輸入數字範圍開始值：')
end = input('請輸入數字範圍結束值：')
start = int(start)
end = int(end)

answer = random.randint(start, end)
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