# генератор чисел Фибоначчи

def fibonacci():
	prev, cur = 0, 1
	while True:
		yield prev
		prev, cur = cur, prev + cur

# for i in fibonacci():
# 	print(i)
# 	if i > 100:
# 		break

'''	Объект-генератор реализует интерфейс итератора,
	соответственно с этим объектом можно работать,
	как с любым другим итерируемым объектом.'''

for id, num in enumerate(fibonacci()):
	print(f"id: {id}, num: {num}")
	if num > 100:
		break
