from pygame import MOUSEBUTTONDOWN, MOUSEMOTION
class Button():
	def __init__(self, x, y, not_hover_image, hover_image, start_x, start_y):
		self.not_hover_image = not_hover_image
		self.hover_image = hover_image
		self.image = self.not_hover_image
		self.x = x
		self.y = y
		self.start_x = start_x
		self.start_y = start_y
		self.pressed = False
	def update(self, event):
		if event.type == MOUSEMOTION:
			if event.pos[0] - self.start_x in range(self.x, self.x + self.image.get_width()) and event.pos[1] - self.start_y in range(self.y, self.y + self.image.get_height()):
				self.image = self.hover_image
			else:
				self.image = self.not_hover_image
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				if event.pos[0] - self.start_x in range(self.x, self.x + self.image.get_width()) and event.pos[1] - self.start_y in range(self.y, self.y + self.image.get_height()):
					self.pressed = True
	def draw(self, window):
		self.pressed = False
		window.blit(self.image, (self.x, self.y))