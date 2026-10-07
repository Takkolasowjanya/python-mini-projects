#mobile number validator 
n=input()
if n.isdigit()and len(n)<=10:
	print("valid")
else:
	print("invaild")