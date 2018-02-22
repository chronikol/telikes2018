import random
nums=[]
am=0
for i in range(30):
    nums.append(random.randint(-30,31))
print nums
j=2
k=3
for i in range(j):
    for j in range(i+1,k):
        for k in range(j+1,30):
            if ((i!=j and  j!=k and k!=i)and(nums[i]+nums[j]+nums[k]==0)):
                print nums[i],nums[j],nums[k]
                am=am+1
if (am==0):
    print "there is no such numbers"
