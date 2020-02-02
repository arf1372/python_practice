def findPrimeDevisor(n):
    i=2
    while n!=1:
        if n%i==0:
            n/=i
            biggestPrimeDevisor=i
        else:
            i+=1
    return biggestPrimeDevisor
if __name__ == '__main__':
    print(findPrimeDevisor(600851475143))
