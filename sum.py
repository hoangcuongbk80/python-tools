f = open("sum.txt", "r")
i=0
j=0
sum=0
for x in f:
    #if i%2==1:
    sum = sum + float(x)
    j=j+1
    i=i+1
    
print('sum: ', sum)
mean = sum/j
print('Mean: ', mean)