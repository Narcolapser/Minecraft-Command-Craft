def getVerts(obj):
	raw_verts = [i[2:] for i in obj.split('\n') if "v" == i[0] and "n" != i[1]]
	verts = []
	#return raw_verts
	for raw in raw_verts:
		vertex = [int(round(float(i))) for i in raw.split(' ')]
		verts.append(vertex)
	return verts

def getBounds(verts):
	x,y,z = verts[0]
	mx,my,mz = verts[0]
	for vertex in verts:
		if x > vertex[0]:
			x = vertex[0]
		if y > vertex[1]:
			y = vertex[1]
		if z > vertex[2]:
			z = vertex[2]

		if mx < vertex[0]:
			mx = vertex[0]
		if my < vertex[1]:
			my = vertex[1]
		if mz < vertex[2]:
			mz = vertex[2]
	
	return [x,y,z,mx,my,mz]

def makeFill(verts):
	return "fill {0} {1} {2} {3} {4} {5} stone".format(verts[0],verts[1],verts[2],verts[3],verts[4],verts[5])

objects = [i for i in open("house.obj").read().split("\no")]
for o in objects:
	try:
		print(makeFill(getBounds(getVerts(o))))
	except Exception as e:
		print(o,e)

