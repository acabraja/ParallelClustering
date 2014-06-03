import pickle
from time import sleep
import random

def create_virtual_names():
	data = ['male', 'female']
	names = dict()
	for d in data:
		names[d]=[]
		f = open(d+'-name.txt', 'r')
		for line in f:
			names[d].append(line.split()[0])
		f.close()
	print len(names['male'])
	print len(names['female'])
	f = open('names.txt','wb')
	pickle.dump(names,f)

def create_virtual_user(names, mf):
	category = ['job', 'pay', ''] #.....
	name = random.choice(names[mf])
def main():
	create_virtual_names()

if __name__ == '__main__':
	main()