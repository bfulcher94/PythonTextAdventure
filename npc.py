import items

class NonPlayableCharacter():
	def __init__(self):
		raise NotImplementedError("Do not create raw NPC objects")
	def __str__(self):
		return self.name

class Trader(NonPlayableCharacter):
	def __init__(self):
		self.name = "Trader"
		self.gold = 250
		self.inventory = [items.CrustyBread(), items.CrustyBread(), items.HealthPotion(), items.HealthPotion(), items.BattleAxe(), items.GreatSword(), items.SmallDagger(),]

class QuestGiver(NonPlayableCharacter):
	def __init__(self):
		self.name = "Quest Giver"
		self.gold = 250
		self.inventory = []