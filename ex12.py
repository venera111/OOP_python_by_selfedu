""" 12. Магический метод __call__. Функторы и классы-декораторы """
#благодаря __call__ мы класс можем вызывать подобно функции

# class Counter:
# 	def __init__(self) -> None:
# 		self.__counter = 0

# 	def __call__(self, *args, **kwds):
# 		print("__call__")
# 		self.__counter += args[0]
# 		return self.__counter

# c = Counter() #вызов класса и запуск метода __call__: __new__, __init__
# c2 = Counter()
# c(1) #благодаря __call__ экзмпляры класса можно вызывать как функции - функторы
# c(1)
# res = c(1)
# res2 = c2(-4)
# print(res, res2) #счетчики работают независимо для экземпляров - посчитать ко-во вызовов экз-ов класса

import math
# класс-декоратор: вычисление производной функции в точке х
class Derivate:
	def __init__(self, func):
		self.fn = func     # сохраняем ссылку на функцию sin() в приват переменной

	def __call__(self, x, dx=0.0001, *args, **kwargs):
		return (self.fn(x + dx) - self.fn(x)) / dx #численно

@Derivate #если закомментировать, увидим значение функции в точке
def df_sin(x):
	return math.sin(x)

# print(df_sin(math.pi/3)) #значение функции sin(pi/4)
# df_sin = Derivate(df_sin) #класс-декоратор
print(df_sin(math.pi/3)) #значение производной

pass
