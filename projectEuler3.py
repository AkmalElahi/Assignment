"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""
def generatePrime():
 primes=[]
 prime=False
 for i in range(1,10000):
   if i>=1:
       for j in range(2,i):
           if (i % j) == 0 :
               break
       else:
         primes.append(i)
 return primes
primeNo=generatePrime()
#print(primeNo)
factors=[]
dividened=600851475143
counter=0
while(dividened>1 and counter<len(primeNo)):
    rem=dividened % primeNo[counter]
    if rem==0:
        factors.append(primeNo[counter])
        dividened=dividened/primeNo[counter]
    counter=counter+1
print(factors)
print("the largest prime factor of the number 600851475143  = "+str(max(factors)))