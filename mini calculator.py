#simple calculator 
a=int(input())
b=int(input())
Operator=input("enter the operator:")
if Operator=="+":
	print(a+b)
elif Operator=="-":
	print(a-b)
elif Operator=="*":
	print(a*b)
elif Operator=="/":
	print(a/b)
elif Operator=="//":
	print(a//b)
elif Operator=="**":
	print(a**b)
elif Operator=="%":
	print(a%b)
else:
	print("invalid operator")