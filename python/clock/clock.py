class Clock():

	def __init__(self, hours, minutes):
		self.hours = int(hours) % 24
		self.minutes = int(minutes)

		self.hours += minutes // 60
		self.minutes %= 60 # damits weggerechnet wird

		self.hours %= 24

	def __str__(self):
		return '{0:02d}:{1:02d}'.format(self.hours, self.minutes)


	def __eq__(self, other):
		return self.__dict__ == other.__dict__


	def add(self, minutesToAdd):
		self.minutes += minutesToAdd
		if self.minutes > 60:
			h = (self.minutes) // 60 
			self.minutes -= h*60
			self.hours += h

		while self.minutes < 0:
			self.hours -= 1
			self.minutes = 60-(self.minutes*(-1))


		while self.hours > 23:
			self.hours -= 24

		while self.hours < 0:
			self.hours += 24 

		return self.__str__()