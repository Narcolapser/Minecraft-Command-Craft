import sys
from command_joiner import *
from command_relativizer import *

final_tower = ["Command:/fill ~{width} ~{height} ~ ~ ~1 ~-1 air 0 replace"]

if __name__ == "__main__":
	#commands = open(sys.argv[1]).readlines()
	commands = ["Command:/" + i.strip() for i in open(sys.argv[1]).readlines() if (i[0] != "#" and len(i) > 1)]
	height = len(commands)
	width = 3
	clear_tower = "Command:" + mc_compile([final_tower[0].format(height=height,width=width)],[-2,0,0])
	#print(clear_tower)
#	commands.append(clear_tower)
#	ct = "Command:/summon falling_block ~-3 ~1 ~ {Block:command_block,Time:1,TileEntityData:{Command:/fill ~-3 ~1 ~2 ~ ~ ~-1 air 0 replace},Passengers:[{id:falling_block,Block:command_block,Time:1,TileEntityData:{Command:/fill ~ ~-1 ~-1 ~ ~ ~-1 redstone_block},Passengers:[{id:falling_block,Block:redstone_block,Time:1}]}]}"
#	commands.append(ct)
	#commands.append("Command:/fill ~ ~{0} ~ ~ ~ ~-1 air 0 replace".format(num))
#	if len(commands) > 50:
		
	coms2 = []
	for i,c in enumerate(commands):
#		print(c)
		coms2.append(relativeCommand(c,[1,i-len(commands),1]))
	ret = mc_compile(coms2)
	print(ret)
	
	#/fill ~ ~-43 ~ ~ ~ ~-1 air 0 replace
