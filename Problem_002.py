first=1
second=2
third=0
sum=2 # Because 2 is even and kept as defalt value

while third < 4000000:
	third = first+second
	first = second
	second = third
	if third%2==0:
		sum+=third
print("Answer :", sum)

