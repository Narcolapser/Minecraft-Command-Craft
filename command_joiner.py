import sys

def compile(commands):
	#ret = summon + form_command(commands)
	if len(commands) == 0:
		return ""
	command = commands.pop()
	passenger = form_command(commands)
	ret = summon + base.replace("VAL_COMMAND",command)
	ret = ret.replace("VAL_PASSENGER",passenger)
	return ret

def form_command(commands):
	if len(commands) == 0:
		return final_pass
	command = commands.pop()
	passenger = form_command(commands)
	ret = inner.replace("VAL_COMMAND",command)
	ret = ret.replace("VAL_PASSENGER",passenger)
	return ret

def form_inner_command(command,passenger):
	pass

#def form_final_command(command,depth):
#	return "{" + base.format("{" + fruition.format(depth) + "}", "") + "}"


#def recurse(commands,depth):
#	print(len(commands))
#	if len(commands)==0:
#		command = commands.pop()
#	print(command,len(commands))
#	passenger = recurse(commands,depth+1)
#	return "{" + base.format("{" + command + "}",passenger) + "}"

summon = "/summon falling_block ~ ~1 ~ "

inner = "{id:falling_block,Block:command_block,Time:1,TileEntityData:{VAL_COMMAND},Passengers:[VAL_PASSENGER]}"

base = "{Block:command_block,Time:1,TileEntityData:{VAL_COMMAND},Passengers:[VAL_PASSENGER]}"

#fruition = "Command:/fill ~ ~-{0} ~-1 ~ ~{0} ~-1 redstone_block"

final_pass = """{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/fill ~ ~-3 ~-1 ~ ~50 ~-1 redstone_block},Passengers:[{id:falling_block,Block:redstone_block,Time:1}]}"""

#commands = ["Command:/setblock ~5 ~1 ~8 glass_pane" , "Command:/fill ~5 ~-2 ~5 ~15 ~5 ~15 planks 0 hollow"]

commands = ["Command:/" + i.strip() for i in open(sys.argv[1]).readlines()]
print(commands)

print (compile(commands))


"""

/summon falling_block ~ ~1 ~ {Block:command_block,Time:1,TileEntityData:{Command:/fill ~5 ~-2 ~5 ~15 ~5 ~15 planks 0 hollow},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/setblock ~5 ~1 ~8 glass_pane},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/fill ~ ~-3 ~-1 ~ ~50 ~-1 redstone_block},Passengers:[{id:falling_block,Block:redstone_block,Time:1}]}]}]}
/summon falling_block ~ ~1 ~ {Block:command_block,Time:1,TileEntityData:{Command:/fill ~5 ~-2 ~5 ~15 ~5 ~15 planks 0 hollow},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/setblock ~5 ~1 ~8 glass_pane},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/fill ~ ~-3 ~-1 ~ ~50 ~-1 redstone_block},Passengers:[{id:falling_block,Block:redstone_block,Time:1}]}]}]}
/summon falling_block ~ ~1 ~ {Block:command_block,Time:1,TileEntityData:{Command:/fill ~5 ~-2 ~5 ~15 ~5 ~15 planks 0 hollow},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/setblock ~5 ~1 ~8 glass_pane},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/fill ~ ~-3 ~-1 ~ ~50 ~-1 redstone_block},Passengers:[{id:falling_block,Block:redstone_block,Time:1}]}]}]}




"""
