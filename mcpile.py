import sys
from command_joiner import *
from command_relativizer import *

if __name__ == "__main__":
	#commands = open(sys.argv[1]).readlines()
	commands = ["Command:/" + i.strip() for i in open(sys.argv[1]).readlines()]
	coms2 = []
	for i,c in enumerate(commands):
		coms2.append(relativeCommand(c,[0,i,0]))
	ret = mc_compile(coms2)
	print(ret)
