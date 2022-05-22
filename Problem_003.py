number = 600851475143
factors = []

def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

for i in range(1, int((number**0.5)+1),2):
    if isprime(i):
        if (number%i == 0):
            factors.append(i)
            
print("The Prime Factors Are : ", factors)
print("The Largest Prime Factor is : ", max(factors))



