import random


class Item():
	"""The base class for all items"""
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value
	def __str__(self):
		return "{}\n==========\n{}\nValue: {}\n".format(self.name, self.description, self.value)


##############Quest Items#################

class RustyKey(Item):
	def __init__(self):
		super().__init__(name = "Rusty Key", description = "A small brass key that shows signs of significant wear. It looks like it opens a chest of some sort.", value = 0)
class MagicRing(Item):
	def __init__(self):
		super().__init__(name = "Magic Ring", description = "A small golden ring. When you place it on your finger you become invisible. It seems....precious.", value = 50)


############Consumable Items###############

class Consumable(Item):
	def __init__(self, name, description, value, healing_value):
		self.healing_value = healing_value
		super().__init__(name, description, value)
	def __str__(self):
		return "{}\n==========\n{}\nValue: {}\nHealing Power: {}".format(self.name, self.description, self.value, self.healing_value)

class CrustyBread(Consumable):
	def __init__(self):
		super().__init__(name="Crusty Bread", description="A hard lump of bread that will offer very little in terms of sustinence.", value=5, healing_value=12)

class HealthPotion(Consumable):
	def __init__(self):
		super().__init__(name="Healing Potion", description="A red colored liquid that restores health when consumed.", value=25, healing_value=40)

class GreaterHealthPotion(Consumable):
	def __init__(self):
		super().__init__(name="Greater Healing Potion", description="A red colored liquid that restores health when consumed.", value=50, healing_value=75)

################Weapons#################

class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)
	def __str__(self):
		return "{}\n==========\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
	def __init__(self):
		super().__init__(name="Rock", description="A fist-sized rock, suitable for bludgeoning.", value=0, damage=5)

class BattleAxe(Weapon):
	def __init__(self):
		super().__init__(name="Battle-Axe", description="A heavy two handed axe. It looks to be in decent shape despite some rust.", value=25, damage=20)

class RustySword(Weapon):
	def __init__(self):
		super().__init__(name="Rusty Sword", description="A rust covered short sword in a state of disrepair. Slightly more effective than a rock.", value=3, damage=8)

class GreatSword(Weapon):
	def __init__(self):
		super().__init__(name="Steel GreatSword", description="A shiny sword close to 5 feet in length. It looks to be in pristine condition.", value=50, damage=35)

class SmallDagger(Weapon):
	def __init__(self):
		super().__init__(name="Small Dagger", description="Though it may look small and insignificant, this blade is deadly in the right hands.", value=10, damage=15)

class MageStaff(Weapon):
	def __init__(self):
		super().__init__(name="Mage Staff", description="A knotted wooden staff about 6 feet long. You can feel power radiating from it.", value=100, damage=60)

################Armour#################

class Armour(Item):
	def __init__(self, name, description, value, armour_rating):
		self.armour_rating = armour_rating
		super().__init__(name, description, value)
	def __str__(self):
		return "{}\n==========\n{}\nValue: {}\nArmour Rating: {}".format(self.name, self.description, self.value, self.armour_rating)

class LeatherArmour(Armour):
	def __init__(self):
		super().__init__(name="Leather Armour", description="A worn set of leather armour.", value=50, armour_rating=20)







