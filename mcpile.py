import sys
from command_joiner import *
from command_relativizer import *

final_tower = ["Command:/fill ~{width} ~{height} ~ ~ ~1 ~-1 air 0 replace"]

if __name__ == "__main__":
	#commands = open(sys.argv[1]).readlines()
	commands = ["Command:/" + i.strip() for i in open(sys.argv[1]).readlines() if (i[0] != "#" and len(i) > 1)]
	height = len(commands)
	width = ((height / 50) + 1) * 2 + 1
	if height > 50:
		height = 50
	clear_tower = "Command:" + mc_compile([final_tower[0].format(height=height,width=width)],[-2,0,0])
	commands.append(clear_tower)

	shift = width -1

	while len(commands) > 49:
		print("towering")
		inners = commands[-49:]
		del commands[-49:]
		inner_tower = "Command:" + mc_compile(inners,[-shift,0,0])
		shift -= 2
		commands.append(inner_tower)
	#print(clear_tower)

#	if len(commands) > 50:
		
	coms2 = []
	for i,c in enumerate(commands):
#		print(c)
		coms2.append(relativeCommand(c,[1,i-len(commands),2]))
	ret = mc_compile(coms2)
	print(ret)
