from player import Player
from collections import OrderedDict
import world

def get_available_actions(room, player):
	actions = OrderedDict()
	print("\n*****************\nChoose an action: ")
	if player.inventory:
		action_adder(actions, 'i', player.print_inventory, "View inventory")
	if isinstance(room, world.TraderTile):
		action_adder(actions, 't', player.trade, "Trade")
	if isinstance(room, (world.EnemyTile or world.BossBattleTile)) and room.enemy.is_alive():
		action_adder(actions, 'a', player.attack, "Attack")
		action_adder(actions, 'f', player.flee, "Flee")
	else:
		if world.tile_at(room.x, room.y - 1):
			action_adder(actions, 'n', player.move_north, "Walk north")
		if world.tile_at(room.x, room.y + 1):
			action_adder(actions, 's', player.move_south, "Walk south")
		if world.tile_at(room.x + 1, room.y):
			action_adder(actions, 'e', player.move_east, "Walk east")
		if world.tile_at(room.x - 1, room.y):
			action_adder(actions, 'w', player.move_west, "Walk west")
	if player.hp < 100:
		action_adder(actions, 'h', player.heal, "Heal")
	return actions

def action_adder(action_dict, hotkey, action, name):
	action_dict[hotkey.lower()] = action
	action_dict[hotkey.upper()] = action
	print("{}: {}".format(hotkey, name))

def choose_action(room, player):
	action = None
	while not action:
		available_actions = get_available_actions(room, player)
		action_input = input("Action: ")
		action = available_actions.get(action_input)
		if action:
			action()
		else:
			print("You cannot do that here!")

def play():
	print("Escape from the cave.\n")
	player = Player()
	world.parse_world_dsl()

	while player.is_alive() and not player.victory:
		room = world.tile_at(player.x, player.y)
		if not player.inBattle:
			print(room.intro_text())
		else:
			print(room.battle_text())
		
		room.modify_player(player)
		if player.is_alive() and not player.victory:
			choose_action(room, player)
		elif not player.is_alive():
			print("\n\n\nYou have died.\nGame Over.\n\n")


	
play()