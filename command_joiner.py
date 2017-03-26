import sys

def compile(commands):
	#ret = summon + form_command(commands)
	if len(commands) == 0:
		return ""
	command = commands.pop()
	passenger = form_command(commands,1)
	ret = summon + base.replace("VAL_COMMAND",command)
	ret = ret.replace("VAL_PASSENGER",passenger)
	return ret

def form_command(commands,depth):
	if len(commands) == 0:
		return final_pass.replace("VAL_NUM",str(depth))
	command = commands.pop()
	passenger = form_command(commands,depth + 1)
	ret = inner.replace("VAL_COMMAND",command)
	ret = ret.replace("VAL_PASSENGER",passenger)
	return ret

summon = "/summon falling_block ~ ~1 ~ "

inner = "{id:falling_block,Block:command_block,Time:1,TileEntityData:{VAL_COMMAND},Passengers:[VAL_PASSENGER]}"

base = "{Block:command_block,Time:1,TileEntityData:{VAL_COMMAND},Passengers:[VAL_PASSENGER]}"

final_pass = """{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/fill ~ ~-VAL_NUM ~-1 ~ ~ ~-1 redstone_block},Passengers:[{id:falling_block,Block:redstone_block,Time:1}]}"""

#commands = ["Command:/setblock ~5 ~1 ~8 glass_pane" , "Command:/fill ~5 ~-2 ~5 ~15 ~5 ~15 planks 0 hollow"]

commands = ["Command:/" + i.strip() for i in open(sys.argv[1]).readlines()]
print(commands)

print (compile(commands))


"""

/summon falling_block ~ ~1 ~ {Block:command_block,Time:1,TileEntityData:{Command:/fill ~5 ~-2 ~5 ~15 ~5 ~15 planks 0 hollow},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/setblock ~5 ~1 ~8 glass_pane},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/fill ~ ~-3 ~-1 ~ ~50 ~-1 redstone_block},Passengers:[{id:falling_block,Block:redstone_block,Time:1}]}]}]}
/summon falling_block ~ ~1 ~ {Block:command_block,Time:1,TileEntityData:{Command:/fill ~5 ~-2 ~5 ~15 ~5 ~15 planks 0 hollow},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/setblock ~5 ~1 ~8 glass_pane},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/fill ~ ~-3 ~-1 ~ ~50 ~-1 redstone_block},Passengers:[{id:falling_block,Block:redstone_block,Time:1}]}]}]}
/summon falling_block ~ ~1 ~ {Block:command_block,Time:1,TileEntityData:{Command:/fill ~5 ~-2 ~5 ~15 ~5 ~15 planks 0 hollow},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/setblock ~5 ~1 ~8 glass_pane},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/fill ~ ~-3 ~-1 ~ ~50 ~-1 redstone_block},Passengers:[{id:falling_block,Block:redstone_block,Time:1}]}]}]}

setblock ~5 ~1 ~8 glass_pane
fill ~5 ~-2 ~5 ~15 ~5 ~15 planks 0 hollow

"""
