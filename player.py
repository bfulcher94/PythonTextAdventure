import items, world, random
attackLast = False

class Player:
	def __init__(self):
		self.inventory = [items.RustySword(), items.CrustyBread(), items.CrustyBread()]
		self.x = 1  #world.start_tile_location[0]
		self.y = 3  #world.start_tile_location[1]
		self.hp = 100
		self.gold = 5
		self.inBattle = False
		self.victory = False
		self.armour_rating = 1
		self.quest_complete = False

	def is_alive(self):
		return self.hp > 0

	def print_inventory(self):
		print ("\nYou open your worn leather bag and find the following...")
		for item in self.inventory:
			print('\n' + str(item))
		best_weapon = self.most_powerful_weapon()
		print("\nThe strongest weapon you find is your {}\n\n".format(best_weapon.name))
		print("You have {} gold.".format(self.gold))

	def most_powerful_weapon(self):
		max_damage = 0
		best_weapon = None
		for item in self.inventory:
			try:
				if item.damage > max_damage:
					best_weapon = item
					max_damage = item.damage
			except AttributeError:
					pass
		return best_weapon


	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def move_north(self):
		self.move(dx=0, dy=-1)
		self.inBattle = False
	def move_south(self):
		self.move(dx=0, dy=1)
		self.inBattle = False
	def move_east(self):
		self.move(dx=1, dy=0)
		self.inBattle = False
	def move_west(self):
		self.move(dx=-1, dy=0)
		self.inBattle = False

	def attack(self):
		self.inBattle = True
		best_weapon = self.most_powerful_weapon()
		room = world.tile_at(self.x, self.y)
		enemy = room.enemy
		print("\nYou use {} against {}!\nIt does {} damage.".format(best_weapon.name, enemy.name, best_weapon.damage))
		enemy.hp -= best_weapon.damage
		if not enemy.is_alive():
			print("\nYou have slain the {}!".format(enemy.name))
		else:
			print("{} has {} HP remaining.\n".format(enemy.name, enemy.hp))

	def heal(self):
		consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]

		if not consumables:
			print("\nYou search in your bag for something to heal you, unfortunately you find nothing.")
			return
		for i, item in enumerate(consumables, 1):
			print("\nYou search your bag for something to heal yourself, you are in luck!\n\nChoose an item to restore your HP: ")
			print("{}. {}".format(i, item))
		valid = False
		while not valid:
			choice = input("")
			try:
				to_eat = consumables[int(choice) - 1]
				self.hp = min(100, self.hp + to_eat.healing_value)
				self.inventory.remove(to_eat)
				print("\nYou consume the item and begin to feel much better.\nCurrent HP: {}".format(self.hp))
				valid = True
			except (ValueError, IndexError):
				print("\nInvalid choice, try again.")

	def trade(self):
		room = world.tile_at(self.x, self.y)
		room.check_if_trade(self)

	def flee(self):
		success = random.randint(1, 10)
		room = world.tile_at(self.x, self.y)
		if success > 4:
			if world.tile_at(room.x, room.y - 1):
				self.move_north()
				print("You escaped the battle and headed north.")
			elif world.tile_at(room.x, room.y + 1):
				self.move_south()
				print("You escaped the battle and headed south.")
			elif world.tile_at(room.x + 1, room.y):
				self.move_east()
				print("You escaped the battle and headed east.")
			elif world.tile_at(room.x - 1, room.y):
				self.move_west()
				print("You escaped the battle and headed west.")
		else:
			return "Attempt to flee failed."





