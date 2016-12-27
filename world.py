import random, enemies, player, npc, items

class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError("Create a subclass instead!")
	def battle_text(self):
		raise NotImplementedError("Create a subclass instead!")

	def modify_player(self, player):
		pass

class StartTile(MapTile):
	def intro_text(self):
		return """ \nYou find yourself in a cave with a flickering torch on the wall. \n You can make out four paths, equally as dark and foreboding. """

class BoringTile(MapTile):
	def intro_text(self):
		return """ \nThere is nothing to see in this part of the cave, you must soldier on. """

class VictoryTile(MapTile):
	def modify_player(self, player):
		player.victory = True
	def intro_text(self):
		return """ \nYou have found the exit to the cave!\n\n\n*******************\n*Victory is yours!*\n*******************\n\n"""

################### Enemy Tiles #######################

class EnemyTile(MapTile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.50:
			self.enemy = enemies.Goblin()
		elif r < 0.75:
			self.enemy = enemies.Ogre()
		elif r < 0.95:
			self.enemy = enemies.Necromancer()
		else:
			self.enemy = enemies.GiantSpider()
		super().__init__(x, y)

	def intro_text(self):
		if self.enemy.is_alive():
			return "\n{} Prepare for a fight!".format(str(self.enemy))
		else:
			return "\nThe lifeless corpse of the {} is strewn across the stone floor.".format(self.enemy.name)
	def battle_text(self):
		if self.enemy.is_alive():
			return "\nThe {} is still alive!".format(self.enemy.name)
		else:
			return "\nThe lifeless corpse of the {} is strewn across the sone floor.".format(self.enemy.name)

	def modify_player(self, player):
		if self.enemy.is_alive():
			player.hp = player.hp - self.enemy.damage
			print("\n{} attacks, doing {} damage. You have {} HP remaining.".format(self.enemy.name, self.enemy.damage, player.hp))


class BossBattleTile(MapTile):
	def __init__(self, x, y):
		self.enemy = enemies.Dragon()
		super().__init__(x, y)

	def intro_text(self):
		if self.enemy.is_alive():
			return "\n{} The end is near...".format(str(self.enemy))
		else:
			return "\nYou have done the impossible. You have slain the {}!".format(self.enemy.name)
	def battle_text(self):
		if self.enemy.is_alive():
			return "\nThe {} is still alive!".format(self.enemy.name)
		else:
			return "\nThe {} you have slain lies in a pool of it's own blood.".format(self.enemy.name)

	def modify_player(self, player):
		if self.enemy.is_alive():
			player.hp = player.hp - self.enemy.damage
			print("\nThe {} attacks, doing {} damage. You have {} HP remaining.".format(self.enemy.name, self.enemy.damage, player.hp))




class TraderTile(MapTile):
	def __init__(self, x, y):
		self.trader = npc.Trader()
		super().__init__(x, y)

	def trade(self, buyer, seller):
		for i, item in enumerate(seller.inventory, 1):
			print("{}. {} - {} Gold".format(i, item.name, item.value))
		while True:
			user_input = input("\nChoose an item or press Q to exit: ")
			if user_input in ['Q', 'q', 'quit']:
				return
			else:
				try:
					choice = int(user_input)
					to_swap = seller.inventory[choice -1]
					self.swap(seller, buyer, to_swap)
				except ValueError:
					print("Invalid choice!")

	def swap(self, seller, buyer, item):
		if item.value > buyer.gold:
			print("That is too expensive")
			return
		seller.inventory.remove(item)
		buyer.inventory.append(item)
		seller.gold = seller.gold + item.value
		buyer.gold = buyer.gold - item.value
		print("Thank you for your business, do come again!\n\n")

	def check_if_trade(self, player):
		while True:
			print("\nWould you like to (B)uy, (S)ell, or (Q)uit?")
			user_input = input()
			if user_input in ['Q', 'q']:
				return
			elif user_input in ['B', 'b']:
				print("\nHere is whats available to buy: ")
				self.trade(buyer=player, seller=self.trader)
			elif user_input in ['S', 's']:
				print("\nHere is what you have to sell: ")
				self.trade(buyer=self.trader, seller=player)
			else:
				print("Invalid choice!")

	def intro_text(self):
		return "\nA frail hunched over man approaches you, you hear the jingle of coins in his purse. He looks willing to trade."


################ QUEST ######################

class QuestGiverTile(MapTile):
	def __init__(self, x, y):
		self.trader = npc.QuestGiver()
		self.quest_taken = False
		self.reward_given = False
		super().__init__(x, y)

	def start_quest(self):
		if not self.quest_taken:
			self.quest_taken = True

	def modify_player(self, player):
		if player.quest_complete and not reward_given:
			player.gold = player.gold + npc.QuestGiver.gold
			npc.QuestGiver.gold = 0
			self.reward_given = True
			return "You are rewarded for your efforts!\n+ {} Gold added".format(npc.QuestGiver.gold)

	def intro_text(self):
		if self.quest_taken and reward_given:
			return "\nThanks for doing that for me!"
		elif self.quest_taken:
			return "\nHave you found it yet?"
		else:
			return "\nSomewhere in this cave you may find a magic ring. Bring it to me and I will reward you."

class MagicRingTile(MapTile):
	def __init__(self, x, y):
		self.ring_taken = False
		super().__init__(x, y)

	def modify_player(self, player):
		if not self.ring_taken:
			self.ring_taken = True
			player.inventory.append(items.MagicRing)
			print("\n{}\n has been added to your inventory.".format(items.MagicRing.name))

	def intro_text(self):
		if self.ring_taken:
			return "\nAnother unremarkable part of the cave. You must forge onwards"
		else:
			return "\nLying on the stone floor in front of you is a ring made of gold, you have found The Magic Ring!"


################### Find Tiles ######################

class FindGoldTile(MapTile):
	def __init__(self, x, y):
		self.gold = random.randint(1, 75)
		self.gold_claimed = False
		super().__init__(x, y)

	def modify_player(self, player):
		if not self.gold_claimed:
			self.gold_claimed = True
			player.gold = player.gold + self.gold
			print("\n{} gold added.".format(self.gold))

	def intro_text(self):
		if self.gold_claimed:
			return "\nAnother unremarkable part of the cave. You must forge onwards"
		else:
			return "\nSomething shiny catches your eye, you have found some gold!"

class FindItemTile(MapTile):
	def __init__(self, x, y):
		r = random.randint(1, 10)
		self.item_claimed = False
		if r < 5:
			self.item = items.SmallDagger()
		elif r < 8:
			self.item = items.BattleAxe()
		elif r <= 9:
			self.item = items.GreatSword()
		else:
			self.item = items.MageStaff()
		super().__init__(x, y)

	def modify_player(self, player):
		if not self.item_claimed:
			self.item_claimed = True
			player.inventory.append(self.item)
			print("\n{}\n has been added to your inventory.".format(self.item.name))

	def intro_text(self):
		if self.item_claimed:
			return "\nAn empty weapon rack hangs on the wall. There is nothing to be found in this room."
		else: 
			return "\nA weapon rack hangs on the wall. You go over to inspect the rack and find a new weapon!"



################ TRAP #################

class TrapTile(MapTile):
	def __init__(self, x, y):
		self.trap_damage = random.randint(5, 100)
		self.trap_triggered = False
		super().__init__(x, y)

	def modify_player(self, player):
		if not self.trap_triggered:
			self.trap_triggered = True
			player.hp = player.hp - self.trap_damage
			print("You have {} HP remaining.".format(player.hp))

	def intro_text(self):
		if self.trap_triggered:
			return "\nThe blood covered spiked log hangs in the center of the room"
		else:
			return "\nAs you open the door you hear a click. A large spiked log swings down from the ceiling and slams into you, knocking you to the ground and dealing {} damage.".format(self.trap_damage)





###############################  World Creation  ###################################


world_dsl = """
|EN|EN|BT|FG|TP|FI|BT|
|FG|FI|EN|FG|TT|FI|EN|
|BT|EN|BT|EN|EN|FG|FG|
|EN|ST|FI|FG|BT|BT|EN|
|TP|FG|BT|TT|EN|EN|BT|
|FI|EN|TP|EN|EN|FG|FI|
|TT|EN|FI|EN|VT|EN|TT|
|FG|BT|FG|BT|EN|FI|TP|
|TP|EN|BT|EN|TP|EN|FI|
"""
def is_dsl_valid(dsl):
	if dsl.count("|ST|") != 1:
		return False
	if dsl.count("|VT|") == 0:
		return False
	lines = dsl.splitlines()
	lines = [l for l in lines if l]
	pipe_counts = [line.count("|") for line in lines]
	for count in pipe_counts:
		if count != pipe_counts[0]:
			return False
	return True

tile_type_dict = {"VT": VictoryTile, 
				  "EN": EnemyTile, 
				  "BT": BoringTile, 
				  "ST": StartTile, 
				  "FG": FindGoldTile,
				  "TT": TraderTile,
				  "FI": FindItemTile,
				  "TP": TrapTile,
				  "BB": BossBattleTile,
				  "  ": None}

world_map = []



def parse_world_dsl():
	if not is_dsl_valid(world_dsl):
		raise SyntaxError("DSL is invalid!")

	dsl_lines = world_dsl.splitlines()
	dsl_lines = [x for x in dsl_lines if x]

	for y, dsl_row in enumerate(dsl_lines):
		row = []
		dsl_cells = dsl_row.split("|")
		dsl_cells = [c for c in dsl_cells if c]
		for x, dsl_cell in enumerate(dsl_cells):
			tile_type = tile_type_dict[dsl_cell]
			row.append(tile_type(x, y) if tile_type else None)

		world_map.append(row)


def tile_at(x, y):
	if x < 0 or y <0:
		return None
	try:
		return world_map[y][x]
	except IndexError:
		return None






