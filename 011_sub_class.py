class animal(object):
	pass

class dog(animal):
	def __init__(self,name):
		self.name = name
class cat(animal):
	def __init__(self,name):
		self.name = name

rover =dog("rover")
satan =cat("satan")
