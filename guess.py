# 产生一个随机整数1~100（不要印出来）
# 让使用者重复输入数字去猜
# 猜对话 印出“终于猜对了”
# 猜错的话 要告诉他 比答案大/小

import random

r = random.randint(1,100)

while True:
	num = input('猜数字')
	num = int(num)
	if num == r:
		print('终于猜对了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')


