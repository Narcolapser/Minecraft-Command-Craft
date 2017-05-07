import sys
from command_joiner import *
from command_relativizer import *

final_tower = ["Command:/fill ~{width} ~{height} ~ ~ ~1 ~-1 air 0 replace"]

max_height = 50

if __name__ == "__main__":
	#commands = open(sys.argv[1]).readlines()
	commands = ["Command:/" + i.strip() for i in open(sys.argv[1]).readlines() if (i[0] != "#" and len(i) > 1)]
	height = len(commands)
	width = ((height / max_height) + 1) * 2 + 1
	if height > max_height:
		height = max_height
	clear_tower = "Command:" + mc_compile([final_tower[0].format(height=height,width=width)],[-2,0,0])
	#commands.append(clear_tower)

	shift = 1
	tower_num = len(commands) / (max_height-2) + 1
	first_tower_modifier = len(commands) % (max_height - 2)
	if first_tower_modifier < 2:
		first_tower_modifier = 1
	else:
		first_tower_modifier = 0

	while len(commands) > max_height - 1:
		#print("towering")
		inners = [relativeCommand(i,[tower_num-first_tower_modifier,j-(max_height-2),2]) for j,i in enumerate(commands[-(max_height - 1):])]
		tower_num -= 1
		del commands[-(max_height - 1):]
		inner_tower = "Command:" + mc_compile(inners,[-shift,0,0])
		commands.append(inner_tower)
	#print(clear_tower)

#	if len(commands) > 50:
		
	coms2 = []
	for i,c in enumerate(commands):
#		print(c)
		coms2.append(relativeCommand(c,[1,i-len(commands),2]))
	ret = mc_compile(coms2)
	print(ret)
