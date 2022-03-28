""" 2. Методы классов. Параметр self """

class Point:
	color = 'red'
	circle = 2

	def set_coords(self, x, y):
		self.x = x
		self.y = y
		print("вызов метода set_coords " +  str(self))

	def get_coords(self):
		return (self.x, self.y)

# атрибут класса связан с функцией, можем вызвать
print(Point.set_coords)
# Point.set_coords()

pt = Point()
print(pt.set_coords)
# интерпретатор автоматически подставляет указатель на экземпляр класса - всегда!
# pt.set_coords()

# не сможем вызвать так, потмоу что автоматически не подставляется self:
# Point.set_coords()
# но так будет работать
# Point.set_coords(pt)

"""self нужен чтобы добавить в экземпляр добавлял новые атрибуты"""
pt = Point()
pt.set_coords(1, 2)
# были добавлены новые атрибуты в экземпляр
print(pt.__dict__)

"""метод set_coords не копируется в каждый экземпляр, он берется из класса Point
благорадаря self мы знаем, с каким экземпляром работает метод set_coords"""

pt2 = Point()
pt2.set_coords(10, 20)
print(pt2.__dict__)
print(pt.get_coords())

f = getattr(pt, 'get_coords')
print(f)
print(f())


print('заглушка')
