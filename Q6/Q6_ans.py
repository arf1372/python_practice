moveLocation=lambda a,b:(a[0]+b[0],a[1]+b[1])
product=lambda a:a[0]*a[1]
mirror=lambda a:(-1*a[0],-1*a[1])
def fastPalindromic(NUMBER_OF_DIGITS):
    a=10**(NUMBER_OF_DIGITS)-1
    b=10**(NUMBER_OF_DIGITS)-1
    currentLocation=(0,0)
    step=(0,1)
    while min(a,b)>10**(NUMBER_OF_DIGITS-1):
        ans=product(moveLocation((a,b),mirror(currentLocation)))
        if ans==int(str(ans)[::-1]):
            return ans
        # print(currentLocation)
        currentLocation=moveLocation(currentLocation,step)
        if step==(0,1):
            step=(1,-1)
        elif step==(1,-1) and currentLocation[1]==0:
            step=(1,0)
        elif step==(1,0):
            step=(-1,1)
        elif step==(-1,1) and currentLocation[0]==0:
            step=(0,1)
        # else:
        #     raise Exception(f"I messed up :)\n\tstep={step}\n\tcurrentlocation={currentLocation}")
def slowPalindromic(NUMBER_OF_DIGITS):
    a=10**(NUMBER_OF_DIGITS)-1
    b=10**(NUMBER_OF_DIGITS)-1
    palindromics=[]
    for i in range(10**(NUMBER_OF_DIGITS-1),10**NUMBER_OF_DIGITS):
        for j in range(10**(NUMBER_OF_DIGITS-1),10**NUMBER_OF_DIGITS):
            ans=i*j
            if ans==int(str(ans)[::-1]):
                palindromics.append(ans)
    return max(palindromics)
if __name__ == '__main__':
    print(fastPalindromic(3))
    print(slowPalindromic(3))
