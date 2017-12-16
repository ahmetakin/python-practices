class Song(object):
	def __init__(self,lyrics,isim):
		self.lyrics = lyrics
		self.isim = isim
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	def isim_yaz(self):
		print self.isim

happy_bday = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"],"ahmet")

dayz = Song(["Happy birthday to you","So I'll stop right there"],"ahnet")

happy_bday.sing_me_a_song()

dayz.sing_me_a_song()

print dayz.isim
dayz.isim_yaz()