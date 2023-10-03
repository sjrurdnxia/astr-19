#This will probably print hello world!
array = [1,5,-88,-44,3,3,2]
target = 4
def PrintHelloWorld():
	print("Hello World")
def shutup():
	print("Hello Worldpt.2")
def shutups(array, target):
	cur = 0
	maxi = 0
	for i in array:
		if cur<0:
			cur = 0
		cur+=i
		maxi = max(cur,maxi)
	print(maxi)






def main():
	PrintHelloWorld()
	shutup()
	shutups(array, target)

if __name__=="__main__":
	main()
