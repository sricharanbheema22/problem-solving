n = int(input("num: "))
for i in range((2*n)-1):
  for j in range((2*n)-1):
    if i+j==n-1 or i+j==(3*n)-3 or abs(j-i)==n-1:
      print("*",end="")
    else:
      print(" ",end="")
  print()

'''
num: 3
  *  
 * * 
*   *
 * * 
  *  
'''