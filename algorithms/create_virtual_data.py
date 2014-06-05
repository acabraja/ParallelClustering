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

def create_virtual_user(names, mf, id):
	user = {}
	category = ['sex','job', 'paid', 'married', 'profession',
				'childrens_10', 'childrens_other',
				'debt', 'job_position', 'number_of_loans',
				'cars', 'house', 'buildings','money_in_the_bank']
	user['id'] = id
	user['name'] = random.choice(names[mf])
	user['sex']  = random.choice(['M', 'F'])
	user['job'] = random.choice(['administrator']) #...
	user['paid'] = 0
	user['married'] = random.choice(['Y', 'N'])
	user['profession'] = random.choice(['']) #....
	user['childrens_10'] = 0
	user['childrens_other'] = 0
	user['debt'] = 0
	user['job_position'] = random.choice(['']) #...
	user['number_of_loans'] = 0
	user['cars'] = 0
	user['house'] = random.choice(['Y','N'])
	user['buildings'] = 0 # number of buildings
	user['money_in_the_bank'] = 0
	return user

def main():
	create_virtual_names()

if __name__ == '__main__':
	main()
