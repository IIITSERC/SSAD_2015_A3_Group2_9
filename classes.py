import pygame
import os
import sys
import re

from pygame.locals import *
screen = pygame.display.set_mode((1280,720),FULLSCREEN)	
class mario(pygame.sprite.Sprite):
	"""this class will depict our main player"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		"""self.image,self.rect = load_image('snake.png')"""
		self.image = pygame.image.load('mario.jpeg')
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image,(30,30))
		self.rect.move_ip(30,660)
		screen.blit(self.image,self.rect)
		self.pellets = 0
		self.horizontal = 10
		self.vertical = 10
		self.distx = 0
		self.disty = 0
						

class background(pygame.sprite.Sprite):
	"""this class will control all the background functions and objects"""
	
	def __init__(self):
		"""this is the background screen"""
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('wallpaper.jpg')
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image,(1280,720))
		screen.blit(self.image,(0,0))

class wall(pygame.sprite.Sprite):
	"""this class will be the one which controls and makes all the walls"""

	def __init__(self,rect = None):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('brick-wall.png')
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image,(30,30))
		if rect!=None:
			self.rect = rect

class coin(pygame.sprite.Sprite):
	"""this class will initialize the coint"""

	def __init__(self,rect = None):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('coin.jpg')
		self.image = pygame.transform.scale(self.image,(20,20))
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image,(20,20))
		if rect != None:
			self.rect = rect
