from random import random


def digitSum(num):
	result = 0
	for i in str(num):
		result +=int(i)
	if len(str(result)) > 1:
		result = digitSum(result)
	return result
	
	
	
def tarkista(arr):
	s = digitSum(sum(arr))
	total = 0
	for i in arr:
		total += digitSum(i)
	assert(digitSum(total)==s)

def kaikki(times = 10,length=100):
	for i in range(10**6):
		a=[]
		for i in range(times):
			a.append(int(random()*length))
		tarkista(a)
		
if __name__ == "__main__":
	kaikki()
	