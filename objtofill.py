import sys

def getVerts(obj):
	raw_verts = [i[2:] for i in obj.split('\n') 
		if len(i) and "v" == i[0] and "n" != i[1]]
	verts = []
	#return raw_verts
	for raw in raw_verts:
		vertex = [int(round(float(i))) for i in raw.split(' ')]
		#print(vertex)
		verts.append(vertex)
	return verts

def getBounds(verts):
	x,y,z = verts[0]#lesser
	mx,my,mz = [i-1 for i in verts[0]]#max
	for vertex in verts:
		if x > vertex[0]:
			x = vertex[0]
		if y > vertex[1]:
			y = vertex[1]
		if z > vertex[2]:
			z = vertex[2]

		if mx < vertex[0]:
			mx = vertex[0] - 1
		if my < vertex[1]:
			my = vertex[1] - 1
		if mz < vertex[2]:
			mz = vertex[2] - 1
	
	return [x,y,z,mx,my,mz]

#o Stone.105_Cube.106
def getBlockName(obj):
	return obj.split('\n')[0].split(' ')[1].split('.')[0]

def makeFill(verts,name):
	return "fill {0} {1} {2} {3} {4} {5} {6}".format(verts[0],verts[1],verts[2],verts[3],verts[4],verts[5],name)


if __name__ == "__main__":
#	if len(sys.argv) > 2:
#		objects = [i for i in open(sys.argv[2]).read().split("\no")]
#	else:
#		objects = [i for i in open("house.obj").read().split("\no")]
#	print(sys.argv)
	objects = [i for i in open(sys.argv[1]).read().split("\no")]
	for o in objects[1:]:
	#	try:
		verts = getBounds(getVerts(o))
		block_name = getBlockName(o)
		print(makeFill(verts,block_name))
		#makeFill(getBounds(getVerts(o)))
	#	except Exception as e:
	#		print(o,e)


