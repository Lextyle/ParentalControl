import pygame
from pyautogui import size
from EntryField import *
from Button import *
from getpass import getuser
pygame.init()
username = getuser()
try:
	file = open(fr"C:\Users\{username}\AppData\Local\dates.py", "r")
except:
	file = open(fr"C:\Users\{username}\AppData\Local\dates.py", "w")
	file.write("0:0-24:0\n0:0-24:0\n0:0-24:0\n0:0-24:0\n0:0-24:0\n0:0-24:0\n0:0-24:0")
file.close()
try:
	file = open(fr"C:\Users\{username}\AppData\Local\password.py", "r")
except:
	file = open(fr"C:\Users\{username}\AppData\Local\password.py", "w")
file.close()
window_width, window_height = size()
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
font = pygame.font.Font("SFPixelate.ttf", 25)
def change_dates():
	global EntryField
	jump_width = (window_width - (font.render("Monday", True, (20, 25, 2)).get_width() + font.render("Tuesday", True, (20, 25, 2)).get_width() + font.render("Wednesday", True, (20, 25, 2)).get_width() + font.render("Thursday", True, (20, 25, 2)).get_width() + font.render("Friday", True, (20, 25, 2)).get_width() + font.render("Saturday", True, (20, 25, 2)).get_width() + font.render("Sunday", True, (20, 25, 2)).get_width())) // 6
	jump_width_2 = (window_width - (200 * 7)) // 6
	file = open(fr"C:\Users\{username}\AppData\Local\dates.py", "r")
	delete_button_image = pygame.image.load(r"assets\delete_button_image.png")
	hover_delete_button_image = pygame.image.load(r"assets\hover_delete_button_image.png")
	monday_delete_buttons = []
	tuesday_delete_buttons = []
	wednesday_delete_buttons = []
	thursday_delete_buttons = []
	friday_delete_buttons = []
	saturday_delete_buttons = []
	sunday_delete_buttons = []
	text = file.read()
	dates = text.split("\n")
	monday_dates = dates[0].split(" ")
	tuesday_dates = dates[1].split(" ")
	wednesday_dates = dates[2].split(" ")
	thursday_dates = dates[3].split(" ")
	friday_dates = dates[4].split(" ")
	saturday_dates = dates[5].split(" ")
	sunday_dates = dates[6].split(" ")
	file.close()
	monday_EntryFields = []
	tuesday_EntryFields = []
	wednesday_EntryFields = []
	thursday_EntryFields = []
	friday_EntryFields = []
	saturday_EntryFields = []
	sunday_EntryFields = []
	x = 0
	y = 200
	for date in monday_dates:
		if date != "":
			entry_field = EntryField(x, y, 200, 32, font, (30, 30, 30), [255, 255, 255])
			entry_field.text = date
			monday_EntryFields.append(entry_field)
			monday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
		y += 32 + 5
	y = 200
	x += 200 + jump_width_2
	for date in tuesday_dates:
		if date != "":
			entry_field = EntryField(x, y, 200, 32, font, (30, 30, 30), [255, 255, 255])
			entry_field.text = date
			tuesday_EntryFields.append(entry_field)
			tuesday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
			y += 32 + 5
	y = 200
	x += 200 + jump_width_2
	for date in wednesday_dates:
		if date != "":
			entry_field = EntryField(x, y, 200, 32, font, (30, 30, 30), [255, 255, 255])
			entry_field.text = date
			wednesday_EntryFields.append(entry_field)
			wednesday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
			y += 32 + 5
	y = 200
	x += 200 + jump_width_2
	for date in thursday_dates:
		if date != "":
			entry_field = EntryField(x, y, 200, 32, font, (30, 30, 30), [255, 255, 255])
			entry_field.text = date
			thursday_EntryFields.append(entry_field)
			thursday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
			y += 32 + 5
	y = 200
	x += 200 + jump_width_2
	for date in friday_dates:
		if date != "":
			entry_field = EntryField(x, y, 200, 32, font, (30, 30, 30), [255, 255, 255])
			entry_field.text = date
			friday_EntryFields.append(entry_field)
			friday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
			y += 32 + 5
	y = 200
	x += 200 + jump_width_2
	for date in saturday_dates:
		if date != "":
			entry_field = EntryField(x, y, 200, 32, font, (30, 30, 30), [255, 255, 255])
			entry_field.text = date
			saturday_EntryFields.append(entry_field)
			saturday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
			y += 32 + 5
	y = 200
	x += 200 + jump_width_2
	for date in sunday_dates:
		if date != "":
			entry_field = EntryField(x, y, 200, 32, font, (30, 30, 30), [255, 255, 255])
			entry_field.text = date
			sunday_EntryFields.append(entry_field)
			sunday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
			y += 32 + 5
	accept_button = Button(window_width // 2 - pygame.image.load(r"assets\accept_button_image.png").get_width() // 2, window_height - 200, pygame.image.load(r"assets\accept_button_image.png"), pygame.image.load(r"assets\hover_accept_button_image.png"), 0, 0)
	monday_add_button = Button(0, 0, pygame.image.load(r"assets\add_button_image.png"), pygame.image.load(r"assets\hover_add_button_image.png"), 0, 0)
	tuesday_add_button = Button(0, 0, pygame.image.load(r"assets\add_button_image.png"), pygame.image.load(r"assets\hover_add_button_image.png"), 0, 0)
	wednesday_add_button = Button(0, 0, pygame.image.load(r"assets\add_button_image.png"), pygame.image.load(r"assets\hover_add_button_image.png"), 0, 0)
	thursday_add_button = Button(0, 0, pygame.image.load(r"assets\add_button_image.png"), pygame.image.load(r"assets\hover_add_button_image.png"), 0, 0)
	friday_add_button = Button(0, 0, pygame.image.load(r"assets\add_button_image.png"), pygame.image.load(r"assets\hover_add_button_image.png"), 0, 0)
	saturday_add_button = Button(0, 0, pygame.image.load(r"assets\add_button_image.png"), pygame.image.load(r"assets\hover_add_button_image.png"), 0, 0)
	sunday_add_button = Button(0, 0, pygame.image.load(r"assets\add_button_image.png"), pygame.image.load(r"assets\hover_add_button_image.png"), 0, 0)
	cancel_button = Button(window_width // 2 + pygame.image.load(r"assets\accept_button_image.png").get_width() // 2 + 20, window_height - 200, pygame.image.load(r"assets\cancel_button_image.png"), pygame.image.load(r"assets\hover_cancel_button_image.png"), 0, 0)
	while True:
		window.fill((60, 60, 60))
		if len(monday_EntryFields) > 0:
			monday_add_button.x = monday_EntryFields[-1].x + monday_EntryFields[-1].width // 2 - monday_add_button.image.get_width() // 2
			monday_add_button.y = monday_EntryFields[-1].y + monday_EntryFields[-1].height + 5
		else:
			monday_add_button.x = (0 + 100) - monday_add_button.image.get_width() // 2
			monday_add_button.y = 200
		if len(tuesday_EntryFields) > 0:
			tuesday_add_button.x = tuesday_EntryFields[-1].x + tuesday_EntryFields[-1].width // 2 - tuesday_add_button.image.get_width() // 2
			tuesday_add_button.y = tuesday_EntryFields[-1].y + tuesday_EntryFields[-1].height + 5
		else:
			tuesday_add_button.x = (font.render("Monday", True, (255, 255, 255)).get_width() + jump_width + 100) - tuesday_add_button.image.get_width() // 2
			tuesday_add_button.y = 200
		if len(wednesday_EntryFields) > 0:
			wednesday_add_button.x = wednesday_EntryFields[-1].x + wednesday_EntryFields[-1].width // 2 - wednesday_add_button.image.get_width() // 2
			wednesday_add_button.y = wednesday_EntryFields[-1].y + wednesday_EntryFields[-1].height + 5
		else:
			wednesday_add_button.x = (font.render("Monday", True, (255, 255, 255)).get_width() + jump_width + font.render("Tuesday", True, (255, 255, 255)).get_width() + jump_width + 100) - wednesday_add_button.image.get_width() // 2
			wednesday_add_button.y = 200
		if len(thursday_EntryFields) > 0:
			thursday_add_button.x = thursday_EntryFields[-1].x + thursday_EntryFields[-1].width // 2 - thursday_add_button.image.get_width() // 2
			thursday_add_button.y = thursday_EntryFields[-1].y + thursday_EntryFields[-1].height + 5
		else:
			thursday_add_button.x = (font.render("Monday", True, (255, 255, 255)).get_width() + jump_width + font.render("Tuesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Wednesday", True, (255, 255, 255)).get_width() + jump_width + 100) - thursday_add_button.image.get_width() // 2
			thursday_add_button.y = 200
		if len(friday_EntryFields) > 0:
			friday_add_button.x = friday_EntryFields[-1].x + friday_EntryFields[-1].width // 2 - friday_add_button.image.get_width() // 2
			friday_add_button.y = friday_EntryFields[-1].y + friday_EntryFields[-1].height + 5
		else:
			friday_add_button.x = (font.render("Monday", True, (255, 255, 255)).get_width() + jump_width + font.render("Tuesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Wednesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Thursday", True, (255, 255, 255)).get_width() + jump_width + 100) - friday_add_button.image.get_width() // 2
			friday_add_button.y = 200
		if len(saturday_EntryFields) > 0:
			saturday_add_button.x = saturday_EntryFields[-1].x + saturday_EntryFields[-1].width // 2 - saturday_add_button.image.get_width() // 2
			saturday_add_button.y = saturday_EntryFields[-1].y + saturday_EntryFields[-1].height + 5
		else:
			saturday_add_button.x = (font.render("Monday", True, (255, 255, 255)).get_width() + jump_width + font.render("Tuesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Wednesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Thursday", True, (255, 255, 255)).get_width() + jump_width + font.render("Friday", True, (255, 255, 255)).get_width() + jump_width + 100) - saturday_add_button.image.get_width() // 2
			saturday_add_button.y = 200
		if len(sunday_EntryFields) > 0:
			sunday_add_button.x = sunday_EntryFields[-1].x + sunday_EntryFields[-1].width // 2 - sunday_add_button.image.get_width() // 2
			sunday_add_button.y = sunday_EntryFields[-1].y + sunday_EntryFields[-1].height + 5
		else:
			sunday_add_button.x = (font.render("Monday", True, (255, 255, 255)).get_width() + jump_width + font.render("Tuesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Wednesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Thursday", True, (255, 255, 255)).get_width() + jump_width + font.render("Friday", True, (255, 255, 255)).get_width() + jump_width + font.render("Saturday", True, (255, 255, 255)).get_width() + jump_width + 100) - sunday_add_button.image.get_width() // 2
			sunday_add_button.y = 200
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			cancel_button.update(event)
			for delete_button in monday_delete_buttons:
				delete_button.update(event)
				if delete_button.pressed:
					index = monday_delete_buttons.index(delete_button)
					monday_delete_buttons.remove(delete_button)
					monday_EntryFields.pop(index)
					for monday_delete_button in monday_delete_buttons[index:len(monday_delete_buttons)]:
						monday_delete_button.y -= 32 + 5
					for monday_EntryField in monday_EntryFields[index:len(monday_EntryFields)]:
						monday_EntryField.y -= 32 + 5
			for delete_button in tuesday_delete_buttons:
				delete_button.update(event)
				if delete_button.pressed:
					index = tuesday_delete_buttons.index(delete_button)
					tuesday_delete_buttons.remove(delete_button)
					tuesday_EntryFields.pop(index)
					for tuesday_delete_button in tuesday_delete_buttons[index:len(tuesday_delete_buttons)]:
						tuesday_delete_button.y -= 32 + 5
					for tuesday_EntryField in tuesday_EntryFields[index:len(tuesday_EntryFields)]:
						tuesday_EntryField.y -= 32 + 5
			for delete_button in wednesday_delete_buttons:
				delete_button.update(event)
				if delete_button.pressed:
					index = wednesday_delete_buttons.index(delete_button)
					wednesday_delete_buttons.remove(delete_button)
					wednesday_EntryFields.pop(index)
					for wednesday_delete_button in wednesday_delete_buttons[index:len(wednesday_delete_buttons)]:
						wednesday_delete_button.y -= 32 + 5
					for wednesday_EntryField in wednesday_EntryFields[index:len(wednesday_EntryFields)]:
						wednesday_EntryField.y -= 32 + 5
			for delete_button in thursday_delete_buttons:
				delete_button.update(event)
				if delete_button.pressed:
					index = thursday_delete_buttons.index(delete_button)
					thursday_delete_buttons.remove(delete_button)
					thursday_EntryFields.pop(index)
					for thursday_delete_button in thursday_delete_buttons[index:len(thursday_delete_buttons)]:
						thursday_delete_button.y -= 32 + 5
					for thursday_EntryField in thursday_EntryFields[index:len(thursday_EntryFields)]:
						thursday_EntryField.y -= 32 + 5
			for delete_button in friday_delete_buttons:
				delete_button.update(event)
				if delete_button.pressed:
					index = friday_delete_buttons.index(delete_button)
					friday_delete_buttons.remove(delete_button)
					friday_EntryFields.pop(index)
					for friday_delete_button in friday_delete_buttons[index:len(friday_delete_buttons)]:
						friday_delete_button.y -= 32 + 5
					for friday_EntryField in friday_EntryFields[index:len(friday_EntryFields)]:
						friday_EntryField.y -= 32 + 5
			for delete_button in saturday_delete_buttons:
				delete_button.update(event)
				if delete_button.pressed:
					index = saturday_delete_buttons.index(delete_button)
					saturday_delete_buttons.remove(delete_button)
					saturday_EntryFields.pop(index)
					for saturday_delete_button in saturday_delete_buttons[index:len(saturday_delete_buttons)]:
						saturday_delete_button.y -= 32 + 5
					for saturday_EntryField in saturday_EntryFields[index:len(saturday_EntryFields)]:
						saturday_EntryField.y -= 32 + 5
			for delete_button in sunday_delete_buttons:
				delete_button.update(event)
				if delete_button.pressed:
					index = sunday_delete_buttons.index(delete_button)
					sunday_delete_buttons.remove(delete_button)
					sunday_EntryFields.pop(index)
					for sunday_delete_button in sunday_delete_buttons[index:len(sunday_delete_buttons)]:
						sunday_delete_button.y -= 32 + 5
					for sunday_EntryField in sunday_EntryFields[index:len(sunday_EntryFields)]:
						sunday_EntryField.y -= 32 + 5
			for entry_field in monday_EntryFields:
				entry_field.update(event)
			for entry_field in tuesday_EntryFields:
				entry_field.update(event)
			for entry_field in wednesday_EntryFields:
				entry_field.update(event)
			for entry_field in thursday_EntryFields:
				entry_field.update(event)
			for entry_field in friday_EntryFields:
				entry_field.update(event)
			for entry_field in saturday_EntryFields:
				entry_field.update(event)
			for entry_field in sunday_EntryFields:
				entry_field.update(event)
			accept_button.update(event)
			tuesday_add_button.update(event)
			monday_add_button.update(event)
			wednesday_add_button.update(event)
			thursday_add_button.update(event)
			friday_add_button.update(event)
			saturday_add_button.update(event)
			sunday_add_button.update(event)
		if cancel_button.pressed:
			main()
		if monday_add_button.pressed:
			if len(monday_EntryFields) > 0:
				entry_field = EntryField((200 + jump_width_2) * 0, monday_EntryFields[-1].y + monday_EntryFields[-1].height + 5, 200, 32, font, (30, 30, 30), [255, 255, 255])
				monday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				monday_EntryFields.append(entry_field)
			else:
				entry_field = EntryField((200 + jump_width_2) * 0, 200, 200, 32, font, (30, 30, 30), [255, 255, 255])
				monday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				monday_EntryFields.append(entry_field)
		if tuesday_add_button.pressed:
			if len(tuesday_EntryFields) > 0:
				entry_field = EntryField((200 + jump_width_2) * 1, tuesday_EntryFields[-1].y + tuesday_EntryFields[-1].height + 5, 200, 32, font, (30, 30, 30), [255, 255, 255])
				tuesday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				tuesday_EntryFields.append(entry_field)
			else:
				entry_field = EntryField((200 + jump_width_2) * 1, 200, 200, 32, font, (30, 30, 30), [255, 255, 255])
				tuesday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				tuesday_EntryFields.append(entry_field)
		if wednesday_add_button.pressed:
			if len(wednesday_EntryFields) > 0:
				entry_field = EntryField((200 + jump_width_2) * 2, wednesday_EntryFields[-1].y + wednesday_EntryFields[-1].height + 5, 200, 32, font, (30, 30, 30), [255, 255, 255])
				wednesday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				wednesday_EntryFields.append(entry_field)
			else:
				entry_field = EntryField((200 + jump_width_2) * 2, 200, 200, 32, font, (30, 30, 30), [255, 255, 255])
				wednesday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				wednesday_EntryFields.append(entry_field)
		if thursday_add_button.pressed:
			if len(thursday_EntryFields) > 0:
				entry_field = EntryField((200 + jump_width_2) * 3, thursday_EntryFields[-1].y + thursday_EntryFields[-1].height + 5, 200, 32, font, (30, 30, 30), [255, 255, 255])
				thursday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				thursday_EntryFields.append(entry_field)
			else:
				entry_field = EntryField((200 + jump_width_2) * 3, 200, 200, 32, font, (30, 30, 30), [255, 255, 255])
				thursday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				thursday_EntryFields.append(entry_field)
		if friday_add_button.pressed:
			if len(friday_EntryFields) > 0:
				entry_field = EntryField((200 + jump_width_2) * 4, friday_EntryFields[-1].y + friday_EntryFields[-1].height + 5, 200, 32, font, (30, 30, 30), [255, 255, 255])
				friday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				friday_EntryFields.append(entry_field)
			else:
				entry_field = EntryField((200 + jump_width_2) * 4, 200, 200, 32, font, (30, 30, 30), [255, 255, 255])
				friday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				friday_EntryFields.append(entry_field)
		if saturday_add_button.pressed:
			if len(saturday_EntryFields) > 0:
				entry_field = EntryField((200 + jump_width_2) * 5, saturday_EntryFields[-1].y + saturday_EntryFields[-1].height + 5, 200, 32, font, (30, 30, 30), [255, 255, 255])
				saturday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				saturday_EntryFields.append(entry_field)
			else:
				entry_field = EntryField((200 + jump_width_2) * 5, 200, 200, 32, font, (30, 30, 30), [255, 255, 255])
				saturday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				saturday_EntryFields.append(entry_field)
		if sunday_add_button.pressed:
			if len(sunday_EntryFields) > 0:
				entry_field = EntryField((200 + jump_width_2) * 6, sunday_EntryFields[-1].y + sunday_EntryFields[-1].height + 5, 200, 32, font, (30, 30, 30), [255, 255, 255])
				sunday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				sunday_EntryFields.append(entry_field)
			else:
				entry_field = EntryField((200 + jump_width_2) * 6, 200, 200, 32, font, (30, 30, 30), [255, 255, 255])
				sunday_delete_buttons.append(Button(entry_field.x + entry_field.width - delete_button_image.get_width() // 2, entry_field.y - delete_button_image.get_height() // 2, delete_button_image, hover_delete_button_image, 0, 0))
				sunday_EntryFields.append(entry_field)
		if accept_button.pressed:
			save = True
			text = ""
			for entry_field in monday_EntryFields:
				if entry_field.text.count("-") == 1:
					dates = entry_field.text.split("-")
					var = True
					if dates[0].count(":") == 1:
						hour = dates[0].split(":")[0]
						minute = dates[0].split(":")[1]
						try:
							if len(hour) < 3 and len(minute) < 3:
								hour = int(hour)
								minute = int(minute)
								if hour < 25 and minute < 61:
									text += f"{hour}:{minute}-"
									entry_field.text_color = [255, 255, 255]
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
									var = False
							else:
								entry_field.text_color = [200, 0, 0]
								save = False
								var = False
						except:
							entry_field.text_color = [200, 0, 0]
							var = False
							save = False
					else:
						entry_field.text_color = [200, 0, 0]
						var = False
						save = False
					if var:
						if dates[1].count(":") == 1:
							hour_1 = hour
							minute_1 = minute
							hour = dates[1].split(":")[0]
							minute = dates[1].split(":")[1]
							try:
								if int(hour) > hour_1 or (int(hour) == hour_1 and int(minute) > minute_1):
									try:
										if len(hour) < 3 and len(minute) < 3:
											hour = int(hour)
											minute = int(minute)
											if hour < 25 and minute < 61:
												text += f"{hour}:{minute}"
												entry_field.text_color = [255, 255, 255]
											else:
												entry_field.text_color = [200, 0, 0]
												save = False
										else:
											entry_field.text_color = [200, 0, 0]
											save = False
									except:
										entry_field.text_color = [200, 0, 0]
										save = False
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
							except:
								entry_field.text_color = [200, 0, 0]
								save = False
						else:
							entry_field.text_color = [200, 0, 0]
							save = False
						text += " "
				else:
					entry_field.text_color = [200, 0, 0]
					save = False
			text += "\n"
			for entry_field in tuesday_EntryFields:
				if entry_field.text.count("-") == 1:
					dates = entry_field.text.split("-")
					var = True
					if dates[0].count(":") == 1:
						hour = dates[0].split(":")[0]
						minute = dates[0].split(":")[1]
						try:
							if len(hour) < 3 and len(minute) < 3:
								hour = int(hour)
								minute = int(minute)
								if hour < 25 and minute < 61:
									text += f"{hour}:{minute}-"
									entry_field.text_color = [255, 255, 255]
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
									var = False
							else:
								entry_field.text_color = [200, 0, 0]
								save = False
								var = False
						except:
							entry_field.text_color = [200, 0, 0]
							var = False
							save = False
					else:
						entry_field.text_color = [200, 0, 0]
						var = False
						save = False
					if var:
						if dates[1].count(":") == 1:
							hour_1 = hour
							minute_1 = minute
							hour = dates[1].split(":")[0]
							minute = dates[1].split(":")[1]
							try:
								if int(hour) > hour_1 or (int(hour) == hour_1 and int(minute) > minute_1):
									try:
										if len(hour) < 3 and len(minute) < 3:
											hour = int(hour)
											minute = int(minute)
											if hour < 25 and minute < 61:
												text += f"{hour}:{minute}"
												entry_field.text_color = [255, 255, 255]
											else:
												entry_field.text_color = [200, 0, 0]
												save = False
										else:
											entry_field.text_color = [200, 0, 0]
											save = False
									except:
										entry_field.text_color = [200, 0, 0]
										save = False
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
							except:
								entry_field.text_color = [200, 0, 0]
								save = False
						else:
							entry_field.text_color = [200, 0, 0]
							save = False
						text += " "
				else:
					entry_field.text_color = [200, 0, 0]
					save = False
			text += "\n"
			for entry_field in wednesday_EntryFields:
				if entry_field.text.count("-") == 1:
					dates = entry_field.text.split("-")
					var = True
					if dates[0].count(":") == 1:
						hour = dates[0].split(":")[0]
						minute = dates[0].split(":")[1]
						try:
							if len(hour) < 3 and len(minute) < 3:
								hour = int(hour)
								minute = int(minute)
								if hour < 25 and minute < 61:
									text += f"{hour}:{minute}-"
									entry_field.text_color = [255, 255, 255]
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
									var = False
							else:
								entry_field.text_color = [200, 0, 0]
								save = False
								var = False
						except:
							entry_field.text_color = [200, 0, 0]
							var = False
							save = False
					else:
						entry_field.text_color = [200, 0, 0]
						var = False
						save = False
					if var:
						if dates[1].count(":") == 1:
							hour_1 = hour
							minute_1 = minute
							hour = dates[1].split(":")[0]
							minute = dates[1].split(":")[1]
							try:
								if int(hour) > hour_1 or (int(hour) == hour_1 and int(minute) > minute_1):
									try:
										if len(hour) < 3 and len(minute) < 3:
											hour = int(hour)
											minute = int(minute)
											if hour < 25 and minute < 61:
												text += f"{hour}:{minute}"
												entry_field.text_color = [255, 255, 255]
											else:
												entry_field.text_color = [200, 0, 0]
												save = False
										else:
											entry_field.text_color = [200, 0, 0]
											save = False
									except:
										entry_field.text_color = [200, 0, 0]
										save = False
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
							except:
								entry_field.text_color = [200, 0, 0]
								save = False
						else:
							entry_field.text_color = [200, 0, 0]
							save = False
						text += " "
				else:
					entry_field.text_color = [200, 0, 0]
					save = False
			text += "\n"
			for entry_field in thursday_EntryFields:
				if entry_field.text.count("-") == 1:
					dates = entry_field.text.split("-")
					var = True
					if dates[0].count(":") == 1:
						hour = dates[0].split(":")[0]
						minute = dates[0].split(":")[1]
						try:
							if len(hour) < 3 and len(minute) < 3:
								hour = int(hour)
								minute = int(minute)
								if hour < 25 and minute < 61:
									text += f"{hour}:{minute}-"
									entry_field.text_color = [255, 255, 255]
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
									var = False
							else:
								entry_field.text_color = [200, 0, 0]
								save = False
								var = False
						except:
							entry_field.text_color = [200, 0, 0]
							var = False
							save = False
					else:
						entry_field.text_color = [200, 0, 0]
						var = False
						save = False
					if var:
						if dates[1].count(":") == 1:
							hour_1 = hour
							minute_1 = minute
							hour = dates[1].split(":")[0]
							minute = dates[1].split(":")[1]
							try:
								if int(hour) > hour_1 or (int(hour) == hour_1 and int(minute) > minute_1):
									try:
										if len(hour) < 3 and len(minute) < 3:
											hour = int(hour)
											minute = int(minute)
											if hour < 25 and minute < 61:
												text += f"{hour}:{minute}"
												entry_field.text_color = [255, 255, 255]
											else:
												entry_field.text_color = [200, 0, 0]
												save = False
										else:
											entry_field.text_color = [200, 0, 0]
											save = False
									except:
										entry_field.text_color = [200, 0, 0]
										save = False
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
							except:
								entry_field.text_color = [200, 0, 0]
								save = False
						else:
							entry_field.text_color = [200, 0, 0]
							save = False
						text += " "
				else:
					entry_field.text_color = [200, 0, 0]
					save = False
			text += "\n"
			for entry_field in friday_EntryFields:
				if entry_field.text.count("-") == 1:
					dates = entry_field.text.split("-")
					var = True
					if dates[0].count(":") == 1:
						hour = dates[0].split(":")[0]
						minute = dates[0].split(":")[1]
						try:
							if len(hour) < 3 and len(minute) < 3:
								hour = int(hour)
								minute = int(minute)
								if hour < 25 and minute < 61:
									text += f"{hour}:{minute}-"
									entry_field.text_color = [255, 255, 255]
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
									var = False
							else:
								entry_field.text_color = [200, 0, 0]
								save = False
								var = False
						except:
							entry_field.text_color = [200, 0, 0]
							var = False
							save = False
					else:
						entry_field.text_color = [200, 0, 0]
						var = False
						save = False
					if var:
						if dates[1].count(":") == 1:
							hour_1 = hour
							minute_1 = minute
							hour = dates[1].split(":")[0]
							minute = dates[1].split(":")[1]
							try:
								if int(hour) > hour_1 or (int(hour) == hour_1 and int(minute) > minute_1):
									try:
										if len(hour) < 3 and len(minute) < 3:
											hour = int(hour)
											minute = int(minute)
											if hour < 25 and minute < 61:
												text += f"{hour}:{minute}"
												entry_field.text_color = [255, 255, 255]
											else:
												entry_field.text_color = [200, 0, 0]
												save = False
										else:
											entry_field.text_color = [200, 0, 0]
											save = False
									except:
										entry_field.text_color = [200, 0, 0]
										save = False
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
							except:
								entry_field.text_color = [200, 0, 0]
								save = False
						else:
							entry_field.text_color = [200, 0, 0]
							save = False
						text += " "
				else:
					entry_field.text_color = [200, 0, 0]
					save = False
			text += "\n"
			for entry_field in saturday_EntryFields:
				if entry_field.text.count("-") == 1:
					dates = entry_field.text.split("-")
					var = True
					if dates[0].count(":") == 1:
						hour = dates[0].split(":")[0]
						minute = dates[0].split(":")[1]
						try:
							if len(hour) < 3 and len(minute) < 3:
								hour = int(hour)
								minute = int(minute)
								if hour < 25 and minute < 61:
									text += f"{hour}:{minute}-"
									entry_field.text_color = [255, 255, 255]
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
									var = False
							else:
								entry_field.text_color = [200, 0, 0]
								save = False
								var = False
						except:
							entry_field.text_color = [200, 0, 0]
							var = False
							save = False
					else:
						entry_field.text_color = [200, 0, 0]
						var = False
						save = False
					if var:
						if dates[1].count(":") == 1:
							hour_1 = hour
							minute_1 = minute
							hour = dates[1].split(":")[0]
							minute = dates[1].split(":")[1]
							try:
								if int(hour) > hour_1 or (int(hour) == hour_1 and int(minute) > minute_1):
									try:
										if len(hour) < 3 and len(minute) < 3:
											hour = int(hour)
											minute = int(minute)
											if hour < 25 and minute < 61:
												text += f"{hour}:{minute}"
												entry_field.text_color = [255, 255, 255]
											else:
												entry_field.text_color = [200, 0, 0]
												save = False
										else:
											entry_field.text_color = [200, 0, 0]
											save = False
									except:
										entry_field.text_color = [200, 0, 0]
										save = False
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
							except:
								entry_field.text_color = [200, 0, 0]
								save = False
						else:
							entry_field.text_color = [200, 0, 0]
							save = False
						text += " "
				else:
					entry_field.text_color = [200, 0, 0]
					save = False
			text += "\n"
			for entry_field in sunday_EntryFields:
				if entry_field.text.count("-") == 1:
					dates = entry_field.text.split("-")
					var = True
					if dates[0].count(":") == 1:
						hour = dates[0].split(":")[0]
						minute = dates[0].split(":")[1]
						try:
							if len(hour) < 3 and len(minute) < 3:
								hour = int(hour)
								minute = int(minute)
								if hour < 25 and minute < 61:
									text += f"{hour}:{minute}-"
									entry_field.text_color = [255, 255, 255]
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
									var = False
							else:
								entry_field.text_color = [200, 0, 0]
								save = False
								var = False
						except:
							entry_field.text_color = [200, 0, 0]
							var = False
							save = False
					else:
						entry_field.text_color = [200, 0, 0]
						var = False
						save = False
					if var:
						if dates[1].count(":") == 1:
							hour_1 = hour
							minute_1 = minute
							hour = dates[1].split(":")[0]
							minute = dates[1].split(":")[1]
							try:
								if int(hour) > hour_1 or (int(hour) == hour_1 and int(minute) > minute_1):
									try:
										if len(hour) < 3 and len(minute) < 3:
											hour = int(hour)
											minute = int(minute)
											if hour < 25 and minute < 61:
												text += f"{hour}:{minute}"
												entry_field.text_color = [255, 255, 255]
											else:
												entry_field.text_color = [200, 0, 0]
												save = False
										else:
											entry_field.text_color = [200, 0, 0]
											save = False
									except:
										entry_field.text_color = [200, 0, 0]
										save = False
								else:
									entry_field.text_color = [200, 0, 0]
									save = False
							except:
								entry_field.text_color = [200, 0, 0]
								save = False
						else:
							entry_field.text_color = [200, 0, 0]
							save = False
						text += " "
				else:
					entry_field.text_color = [200, 0, 0]
					save = False
			if save:
				file = open(fr"C:\Users\{username}\AppData\Local\dates.py", "w")
				file.write(text)
				file.close()
				main()
		window.blit(font.render("Monday", True, (255, 255, 255)), (0, 20))
		window.blit(font.render("Tuesday", True, (255, 255, 255)), (font.render("Monday", True, (255, 255, 255)).get_width() + jump_width, 20))
		window.blit(font.render("Wednesday", True, (255, 255, 255)), (font.render("Monday", True, (255, 255, 255)).get_width() + jump_width + font.render("Tuesday", True, (255, 255, 255)).get_width() + jump_width, 20))
		window.blit(font.render("Thursday", True, (255, 255, 255)), (font.render("Monday", True, (255, 255, 255)).get_width() + jump_width + font.render("Tuesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Wednesday", True, (255, 255, 255)).get_width() + jump_width, 20))
		window.blit(font.render("Friday", True, (255, 255, 255)), (font.render("Monday", True, (255, 255, 255)).get_width() + jump_width + font.render("Tuesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Wednesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Thursday", True, (255, 255, 255)).get_width() + jump_width, 20))
		window.blit(font.render("Saturday", True, (255, 255, 255)), (font.render("Monday", True, (255, 255, 255)).get_width() + jump_width + font.render("Tuesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Wednesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Thursday", True, (255, 255, 255)).get_width() + jump_width + font.render("Friday", True, (255, 255, 255)).get_width() + jump_width, 20))
		window.blit(font.render("Sunday", True, (255, 255, 255)), (font.render("Monday", True, (255, 255, 255)).get_width() + jump_width + font.render("Tuesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Wednesday", True, (255, 255, 255)).get_width() + jump_width + font.render("Thursday", True, (255, 255, 255)).get_width() + jump_width + font.render("Friday", True, (255, 255, 255)).get_width() + jump_width + font.render("Saturday", True, (255, 255, 255)).get_width() + jump_width, 20))
		for entry_field in monday_EntryFields:
			entry_field.draw(window)
		for delete_button in monday_delete_buttons:
			delete_button.draw(window)
		for entry_field in tuesday_EntryFields:
			entry_field.draw(window)
		for delete_button in tuesday_delete_buttons:
			delete_button.draw(window)
		for entry_field in wednesday_EntryFields:
			entry_field.draw(window)
		for delete_button in wednesday_delete_buttons:
			delete_button.draw(window)
		for entry_field in thursday_EntryFields:
			entry_field.draw(window)
		for delete_button in thursday_delete_buttons:
			delete_button.draw(window)
		for entry_field in friday_EntryFields:
			entry_field.draw(window)
		for delete_button in friday_delete_buttons:
			delete_button.draw(window)
		for entry_field in saturday_EntryFields:
			entry_field.draw(window)
		for delete_button in saturday_delete_buttons:
			delete_button.draw(window)
		for entry_field in sunday_EntryFields:
			entry_field.draw(window)
		for delete_button in sunday_delete_buttons:
			delete_button.draw(window)
		cancel_button.draw(window)
		sunday_add_button.draw(window)
		saturday_add_button.draw(window)
		friday_add_button.draw(window)
		thursday_add_button.draw(window)
		tuesday_add_button.draw(window)
		monday_add_button.draw(window)
		wednesday_add_button.draw(window)
		accept_button.draw(window)
		pygame.display.update()
def password_changes(change_type):
	if change_type == "Create Password":
		password_EntryField = EntryField(window_width // 2 - 300 // 2, window_height // 2, 300, 32, font, (30, 30, 30), [200, 200, 200])
	if change_type == "Change Password":
		new_password_EntryField = EntryField(window_width // 2 - 300 // 2, window_height // 2, 300, 32, font, (30, 30, 30), [200, 200, 200])
		password_EntryField = EntryField(window_width // 2 - 300 // 2, window_height // 2 - 132, 300, 32, font, (30, 30, 30), [200, 200, 200])
	accept_button = Button(window_width // 2 - pygame.image.load(r"assets\accept_button_image.png").get_width() // 2, window_height - 200, pygame.image.load(r"assets\accept_button_image.png"), pygame.image.load(r"assets\hover_accept_button_image.png"), 0, 0)
	if change_type == "Change Password":
		cancel_button = Button(window_width // 2 + pygame.image.load(r"assets\accept_button_image.png").get_width() // 2 + 20, window_height - 200, pygame.image.load(r"assets\cancel_button_image.png"), pygame.image.load(r"assets\hover_cancel_button_image.png"), 0, 0)
	while True:
		window.fill((60, 60, 60))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit(change_type)
			password_EntryField.update(event)
			accept_button.update(event)
			if change_type == "Change Password":
				new_password_EntryField.update(event)
				cancel_button.update(event)
		if accept_button.pressed:
			if change_type == "Create Password":
				if password_EntryField.text != "":
					file = open(fr"C:\Users\{username}\AppData\Local\password.py", "w")
					file.write(f"{password_EntryField.text}")
					file.close()
					break
			if change_type == "Change Password":
				file = open(fr"C:\Users\{username}\AppData\Local\password.py", "r")
				if password_EntryField.text == file.read():
					if new_password_EntryField.text != "":
						file = open(fr"C:\Users\{username}\AppData\Local\password.py", "w")
						file.write(f"{new_password_EntryField.text}")
						file.close()
						main()
					else:
						password_EntryField.text_color = [255, 255, 255]
				else:
					password_EntryField.text_color = [200, 0, 0]
		if change_type == "Change Password":
			if cancel_button.pressed:
				main()
		window.blit(font.render(change_type, True, (255, 255, 255)), (window_width // 2 - font.render(change_type, True, (255, 255, 255)).get_width() // 2, 20))
		password_EntryField.draw(window)
		if change_type == "Change Password":
			window.blit(font.render("Enter Password", True, (255, 255, 255)), (window_width // 2 - font.render("Enter Password", True, (255, 255, 255)).get_width() // 2, (password_EntryField.y - font.render("Enter Password", True, (255, 255, 255)).get_height()) - 20))
			window.blit(font.render("Enter New Password", True, (255, 255, 255)), (window_width // 2 - font.render("Enter New Password", True, (255, 255, 255)).get_width() // 2, (new_password_EntryField.y - font.render("Enter New Password", True, (255, 255, 255)).get_height()) - 20))
			new_password_EntryField.draw(window)
			cancel_button.draw(window)
		accept_button.draw(window)
		pygame.display.update()
file = open(fr"C:\Users\{username}\AppData\Local\password.py", "r")
if file.read() == "":
	password_changes("Create Password")
file.close()
def main():
	file = open(fr"C:\Users\{username}\AppData\Local\password.py", "r")
	password = file.read()
	password_EntryField = EntryField(window_width // 2 - 300 // 2, window_height // 2, 300, 32, font, (30, 30, 30), [200, 200, 200])
	accept_button = Button(window_width // 2 - pygame.image.load(r"assets\accept_button_image.png").get_width() // 2, window_height - 200, pygame.image.load(r"assets\accept_button_image.png"), pygame.image.load(r"assets\hover_accept_button_image.png"), 0, 0)
	change_password_button = Button(20, 20, pygame.image.load(r"assets\change_password_button_image.png"), pygame.image.load(r"assets\hover_change_password_button_image.png"), 0, 0)
	while True:
		window.fill((60, 60, 60))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			password_EntryField.update(event)
			accept_button.update(event)
			change_password_button.update(event)
		if accept_button.pressed:
			if password_EntryField.text == password:
				change_dates()
			else:
				password_EntryField.text_color = [200, 0, 0]
		if change_password_button.pressed:
			password_changes("Change Password")
		change_password_button.draw(window)
		window.blit(font.render("Enter Password", True, (255, 255, 255)), (window_width // 2 - font.render("Enter Password", True, (255, 255, 255)).get_width() // 2, 20))
		password_EntryField.draw(window)
		accept_button.draw(window)
		pygame.display.update()
main()