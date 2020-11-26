from pygame import Surface, KEYDOWN, K_BACKSPACE, K_RETURN,  MOUSEBUTTONDOWN
class EntryField():
	def __init__(self, x, y, width, height, font, color, text_color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.surface = Surface((self.width, self.height))
		self.font = font
		self.color = color
		self.text_color = text_color
		self.text = ""
		self.activated = False
	def update(self, event):
		if event.type == KEYDOWN:
			if self.activated:
				if event.key == K_BACKSPACE:
					self.text = self.text[0:-1]
				elif event.key != K_RETURN:
					self.text += event.unicode
				else:
					self.activated = False
		if event.type == MOUSEBUTTONDOWN:
			if event.pos[0] in range(self.x, self.x + self.width) and event.pos[1] in range(self.y, self.y + self.height):
				self.activated = True
			else:
				self.activated = False
	def draw(self, window):
		if self.activated:
			try:
				self.surface.fill((self.color[0] + 40, self.color[1] + 40, self.color[2] + 40))
			except:
				self.surface.fill((255, 255, 255))
		else:
			self.surface.fill(self.color)
		text_render = self.font.render(self.text, True, self.text_color)
		if text_render.get_width() > self.width:
			self.surface.blit(text_render, ((text_render.get_width() - self.width) * -1, self.height - text_render.get_height()))
		else:
			self.surface.blit(text_render, (0, self.height - text_render.get_height()))
		window.blit(self.surface, (self.x, self.y))