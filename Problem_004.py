palindromes = []

for i in range(100,1000):
    for x in range(100,1000):
        multiple = str(i*x)
        if (multiple == multiple[::-1]):
            palindromes.append(int(multiple))
            
print("Largest Palindrome is : ", max(palindromes))
