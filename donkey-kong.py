import sys
import re
import os
import math
import pygame
import classes

from classes import *
from pygame.locals import *

if not pygame.font:
	print "fonts disabled"
if not pygame.mixer:
	print "sound disabled"

screen = pygame.display.set_mode((1280,720),FULLSCREEN)	
class mainfunction:
	"""this class will start and control the main game"""
	"""It is like the main function in a c-program"""
	
	def __init__(self):
		pygame.init()
	
	def mainloop(self):
		self.load_sprites()
		while 1:
			for event in pygame.event.get():
				self.b_sprites.draw(screen)
				self.player_sprites.draw(screen)
				self.floorwalls_sprites.draw(screen)
				self.rightwalls_sprites.draw(screen)
				self.leftwalls_sprites.draw(screen)
				self.coins_sprites.draw(screen)
				pygame.display.flip()
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == KEYDOWN:
					if((event.key == K_a)
					or(event.key == K_s)
					or(event.key == K_d)
					or(event.key == K_w)
					or(event.key == K_q)):
						self.move(event.key)
				self.getcoins()
				self.floorwalls_sprites.draw(screen)
				self.rightwalls_sprites.draw(screen)
				self.leftwalls_sprites.draw(screen)
				self.coins_sprites.draw(screen)
				self.b_sprites.draw(screen)
	def getcoins(self):
		numcoins = pygame.sprite.spritecollide(self.player,self.coins_sprites,True)

					
	def load_sprites(self):
		"""load the sprites that we need"""
		self.player = mario()
		self.player_sprites = pygame.sprite.RenderPlain((self.player))
		self.b = background()
		self.b_sprites = pygame.sprite.Group()
		self.floorwalls_sprites = pygame.sprite.Group()
		self.leftwalls_sprites = pygame.sprite.Group()
		self.rightwalls_sprites = pygame.sprite.Group()
		self.coins_sprites = pygame.sprite.Group()
		x = 0
		while x < 720:
			self.leftwalls_sprites.add(wall(pygame.Rect(0,x,30,30)))
			self.rightwalls_sprites.add(wall(pygame.Rect(1250,x,30,30)))
			x = x+30

		x = 690
		i = 0
		while x > 0:
			if (i%2 == 0) and i!=0:
				y = 300
				while y < 1280:	
					self.coins_sprites.add(coin(pygame.Rect(y,x-20,20,20)))			
					self.floorwalls_sprites.add(wall(pygame.Rect(y,x,30,30)))
					y = y+30
			elif i==0:
			 	y = 0
			 	while y < 1280:
			 		self.floorwalls_sprites.add(wall(pygame.Rect(y,x,30,30)))
			 		y = y + 30
			else:
				y = 0
				while y < 900:
					self.floorwalls_sprites.add(wall(pygame.Rect(y,x,30,30)))
					y = y + 30
			i = i + 1
			x = x-120		

#Implementation of polymorphism as similar functions perform different processes depending on the input
	def checkcollisionleft(self):
		if pygame.sprite.spritecollideany(self.player,self.leftwalls_sprites) != None:
			self.player.rect.move_ip(-self.distx,self.disty)
	
	def checkcollisionright(self):
		if pygame.sprite.spritecollideany(self.player,self.rightwalls_sprites) != None:
			self.player.rect.move_ip(-self.distx,self.disty)
	def checkdown(self):
		if pygame.sprite.spritecollideany(self.player,self.floorwalls_sprites) != None:
			self.player.rect.move_ip(self.distx,-self.disty)
		
	
	def move(self,key):
		self.distx = 0
		self.vertical = 10
		self.horizontal = 10
		self.disty = 0
		if(key == K_a):
			self.distx = -self.horizontal
			self.player.rect.move_ip(self.distx,self.disty)
			self.checkcollisionleft()
		elif(key == K_d):
			 self.distx = self.horizontal
			 self.player.rect.move_ip(self.distx,self.disty)
			 self.checkcollisionright()
		elif(key == K_w):
		 	self.disty = -self.vertical
			self.player.rect.move_ip(self.distx,self.disty)
			self.checkdown()
		elif(key == K_s):
		 	self.disty = self.vertical
			self.player.rect.move_ip(self.distx,self.disty)
			self.checkdown()
		elif(key == K_q):
			sys.exit()

if __name__ == "__main__":
	start = mainfunction()
	start.mainloop()
		





