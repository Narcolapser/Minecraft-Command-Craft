import sys

#fill 25 0 25 5 5 25 stone
#fill ~25 ~ ~25 ~5 ~5 ~25 stone

#This script will take a command that uses absolute coordinates and translate them into relative
#coordinates with an offset specified.

def is_digit(n):
	try:
		int(n)
		return True
	except ValueError:
		return  False

def findTriads(val):
	parts = val.split()
	triads = []
	triad_offset = 0
	for i,p in enumerate(parts):
		if triad_offset:
			triad_offset -= 1
			continue
		if is_digit(p):
			try:
				if is_digit(parts[i+1]):
					if is_digit(parts[i+2]):
						triad_offset = 2
						triads.append(i)
			except:
				pass
#	print(triads)
	return triads

def offsetTriads(val,offsets):
	triads = findTriads(val)
	#if there are no triads, no work needs to be done.
	if len(triads) == 0:
		return val

	parts = val.split()
	for triad in triads:
		x = int(parts[triad + 0])
		y = int(parts[triad + 1])
		z = int(parts[triad + 2])
		
		parts[triad + 0] = "~" + str(x + offsets[0])
		parts[triad + 1] = "~" + str(y + offsets[1])
		parts[triad + 2] = "~" + str(z + offsets[2])
		
	ret = ' '.join(parts)
	#print(ret)
	return ret
	
def relativeTriads(val):
	return val
	triads = findTriads(val)
	#if there are no triads, no work needs to be done.
	if len(triads) == 0:
		return val

	parts = val.split()
	for triad in triads:
		parts[triad + 0] = "~" + parts[triad + 0]
		parts[triad + 1] = "~" + parts[triad + 1]
		parts[triad + 2] = "~" + parts[triad + 2]
		
	ret = ' '.join(parts)
	#print(ret)
	return ret

def relativeCommand(val,offsets=None):
	if not offsets:
		offsets = [0,0,0]
	ret = offsetTriads(val,offsets)
	ret = relativeTriads(ret)
	return ret

if __name__ == "__main__":
	if len(sys.argv) < 5:
		print("ERROR: 5 arguments needed. The command to relativize, and 3 offsets.")
		sys.exit()
	command = sys.argv[1]
	try:
		offsets = [int(i) for i in sys.argv[2:5]]
	except Exception as e:
		print(e)
	#print(command,offsets)
	print(relativeCommand(command,offsets))
	
#findTriads(command)
#offsetTriads(command,[0,3,0])
#relativeTriads(command)

