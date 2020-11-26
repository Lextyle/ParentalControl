import pygame
from pyautogui import size
from EntryField import *
from Button import *
pygame.init()
window_width, window_height = size()
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
font = pygame.font.Font("SFPixelate.ttf", 50)
def password_changes(change_type):
	if change_type == "Create Password":
		password_EntryField = EntryField(window_width // 2 - 300 // 2, window_height // 2, 300, 62, font, (30, 30, 30), [200, 200, 200])
	if change_type == "Change Password":
		new_password_EntryField = EntryField(window_width // 2 - 300 // 2, window_height // 2, 300, 62, font, (30, 30, 30), [200, 200, 200])
		password_EntryField = EntryField(window_width // 2 - 300 // 2, window_height // 2 - 142, 300, 62, font, (30, 30, 30), [200, 200, 200])
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
					file = open("password.py", "w")
					file.write(f"{password_EntryField.text}")
					file.close()
					break
			if change_type == "Change Password":
				file = open("password.py", "r")
				if password_EntryField.text == file.read():
					if new_password_EntryField.text != "":
						file = open("password.py", "w")
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
			new_password_EntryField.draw(window)
			cancel_button.draw(window)
		accept_button.draw(window)
		pygame.display.update()
file = open("password.py", "r")
if file.read() == "":
	password_changes("Create Password")
def main():
	file = open("password.py", "r")
	password = file.read()
	password_EntryField = EntryField(window_width // 2 - 300 // 2, window_height // 2, 300, 62, font, (30, 30, 30), [200, 200, 200])
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
				pygame.quit()
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