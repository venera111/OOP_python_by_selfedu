from os.path import join

class FileObject:
	'''Обертка вокруг файла для закрытия файлового дескриптора'''
	def __init__(self, filepath='~', filename='file.txt'):
		self.file = open(join(filepath, filename), 'r+')

	def get_strings(self):
		for line in self.file.readlines():
			print(line)

	def __del__(self):
		self.file.close()
		del self.file

a = FileObject('/Users/yanalysova/Documents/OOP_python_by_selfedu/examples', 'hello.txt')
# print(a.__dict__) # атрибуты объекта класса FileObject
a.get_strings()
