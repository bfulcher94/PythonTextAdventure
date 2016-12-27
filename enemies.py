import random

class Enemy:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage

	def __str__(self):
		return "An enemy awaits!"

	def is_alive(self):
		return self.hp > 0

class Goblin(Enemy):
	def __init__(self):
		super().__init__(name = "Goblin Warrior", hp = 15, damage = 5)
	def __str__(self):
		return "\nA fierce looking goblin stops sharpening its blade and advances towards you."

class Ogre(Enemy):
	def __init__(self):
		super().__init__(name = "Ogre", hp = 40, damage = 15)
	def __str__(self):
		return "\nYou peer around the corner to find a large Ogre lurking in the coridoor ahead."

class Necromancer(Enemy):
	def __init__(self):
		super().__init__(name = "Necromancer", hp = 60, damage = 10)
	def __str__(self):
		return "\nAs you advance, a blast of smoke appears before you. When the smoke clears you see a necromancer blocking your path."

class GiantSpider(Enemy):
	def __init__(self):
		super().__init__(name = "Giant Spider", hp = 80, damage = 20)
	def __str__(self):
		return "\nA giant spider crawls down the side of the cave wall and begins moving towards you."


#################Boss###################

class Dragon(Enemy):
	def __init__(self):
		super().__init__(name = "Dragon", hp = 250, damage = 40)
	def __str__(self):
		return "\nA dragon occupies the corridor ahead. This fearsome beast is the strongest enemy you will face.\nEngage him if you dare!\n"