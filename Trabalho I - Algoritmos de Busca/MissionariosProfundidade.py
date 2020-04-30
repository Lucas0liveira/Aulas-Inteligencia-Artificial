
#class Node: 
	#v = [0,0,0]
	#kid = None 

class Node:
	def __init__(self, v=[0,0,0], kid=None):
		self.v = v
		self.kid = kid


def Operation1(node):
	aux = Node()
	aux = node
	x = aux.v[0]
	y = aux.v[1]
	z = aux.v[2]
	#print("1")
	z = z  -1
	x = x-1
	y = y-1
	current = [x,y,z]
	print("Nó atual →",current)
	if((x>=0 and x<=3) and (y>=0 and y<=3) and (z>=0 and z<=1)):
		if(((x==1) or (x==2)) and (y!=x)):
			Operation2(node);
		else:
			aux.kid = Node()
			aux = aux.kid
			aux.v[0] = x
			aux.v[1] = y
			aux.v[2] = z
			print(aux.v)
			print("↓")
	else:
		Operation2(node);

def Operation2(node):
	aux = Node()
	aux = node
	x = aux.v[0]
	y = aux.v[1]
	z = aux.v[2]
	#print("2")
	z = z+1
	x = x+1
	current = [x,y,z]
	print("Nó atual →",current)
	if((x>=0 and x<=3) and (y>=0 and y<=3) and (z>=0 and z<=1)):
		if(((x==1) or (x==2)) and (y!=x)):
			Operation3(aux);
		else:
			aux.kid = Node()
			aux = aux.kid
			aux.v[0] = x
			aux.v[1] = y
			aux.v[2] = z
			print(aux.v)
			print("↓")
	else:
		Operation3(aux);

def Operation3(node):
	aux = Node()
	aux = node
	x = aux.v[0]
	y = aux.v[1]
	z = aux.v[2]
	#print("3")
	z = z-1 
	y = y-2
	current = [x,y,z]
	print("Nó atual →",current)
	if((x>=0 and x<=3) and (y>=0 and y<=3) and (z>=0 and z<=1)):
		if(((x==1) or (x==2)) and (y!=x)):
			Operation4(aux);
		else:
			aux.kid = Node()
			aux = aux.kid
			aux.v[0] = x
			aux.v[1] = y
			aux.v[2] = z
			print(aux.v)
			print("↓")
	else:
		Operation4(aux);

def Operation4(node):
	aux = Node()
	aux = node
	x = aux.v[0]
	y = aux.v[1]
	z = aux.v[2]
	#print("4")
	z = z+1
	y = y+1
	current = [x,y,z]
	print("Nó atual →",current)
	if((x>=0 and x<=3) and (y>=0 and y<=3) and (z>=0 and z<=1)):
		if(((x==1) or (x==2)) and (y!=x)):
			Operation5(aux);
		else:
			aux.kid = Node()
			aux = aux.kid
			aux.v[0] = x
			aux.v[1] = y
			aux.v[2] = z
			print(aux.v)
			print("↓")
	else:
		Operation5(aux);

def Operation5(node):
	aux = Node()
	aux = node
	x = aux.v[0]
	y = aux.v[1]
	z = aux.v[2]
	#print("5")
	z = z-1
	x = x-2
	current = [x,y,z]
	print("Nó atual →",current)
	if((x>=0 and x<=3) and (y>=0 and y<=3) and (z>=0 and z<=1)):
		if(((x==1) or (x==2)) and (y!=x)):
			Operation6(aux);
		else:
			aux.kid = Node()
			aux = aux.kid
			aux.v[0] = x
			aux.v[1] = y
			aux.v[2] = z
			print(aux.v)
			print("↓")
	else:
		Operation6(aux);

def Operation6(node):
	aux = Node()
	aux = node
	x = aux.v[0]
	y = aux.v[1]
	z = aux.v[2]
	#print("6")
	z = z+1
	x = x+1
	y = y+1
	current = [x,y,z]
	print("Nó atual →",current)
	if((x>=0 and x<=3) and (y>=0 and y<=3) and (z>=0 and z<=1)):
		if(((x==1) or (x==2)) and (y!=x)):
			Operation5(aux);
		else:					
			aux.kid = Node()
			aux = aux.kid
			aux.v[0] = x
			aux.v[1] = y
			aux.v[2] = z
			print(aux.v)
			print("↓")
			Operation5(aux)
	else:
		Operation5(aux)

def showSequence(node):
	while node:
		print (node.v)
		print ("↓")
		node = node.kid
	print

head = Node()
head.v[0] = 3
head.v[1] = 3
head.v[2] = 1
aux = Node()
aux = head
v = [0,0,0]

print(head.v)

while (v != head.v):
	Operation1(aux);


#showSequence(head);



end = input("Fim da execução")

