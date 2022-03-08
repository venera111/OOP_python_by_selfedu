# vowels = ["a", "e", "i", "o", "u"]
# vowels_str = ",".join(vowels)
# print("String: ", vowels_str)

# names = ["Java", "Python", 1]
# delimiter = ","
# single_str = delimiter.join(names)
# names = [str(i) for i in names]
# print(names)

# sities = ["Moscow", "New York", "Melbourne"]
# delimiter = ", "
# sities = delimiter.join(sities)
# print(sities)

# animal = "Cheetah"
# delimiter = ","
# animal = delimiter.join(animal)
# print(animal)
# print(type(animal))
# animal = animal.split(delimiter)
# print(animal)
# print(type(animal))

# print("ABC" == "ABС")

# a = [1,1,6,4,6,3,2,8]
# print(list(set(a)))

# res = []
# for x in [1, 2, 2, 2, 3, 3, 1]:
#     if x not in res:
#         res.append(x)
# print(res)

# a,b,c = (1,2,3)
# print(a, b, c)
# print(type(a))

# a = sorted("This is a test string from Andrew".split(), key=lambda x: len(x))
# a = sorted("This is a test string from Andrew".split(), key=str.__len__)
# print(a)

# student_tuples = [
# 		('john', 'A', 15),
# 		('jane', 'B', 12),
# 		('dave', 'B', 10),
# ]
# a = sorted(student_tuples, key=lambda x: x[2])
# print(a)

class Student:
	def __init__(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age

	def __repr__(self): # печать при добавлении объектов в контейнеры типа списков
		return repr((self.name, self.grade, self.age))

student_objects = [
		Student('john', 'A', 15),
		Student('jane', 'B', 12),
		Student('dave', 'B', 10),
	]

# a = sorted(student_objects, key=lambda x: x.age)
# print(a)

from operator import itemgetter, attrgetter, methodcaller
a = sorted(student_objects, key=attrgetter('age'))
print(a)
