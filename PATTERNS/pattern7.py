n = int(input("num: "))
for i in range(n):
  for j in range(2*n):
    if i == j or i+1 == (2*n)-j-1:
      print("*",end = "")
    else:
      print(" ",end = "")
  print()

'''
num: 5
*       * 
 *     *  
  *   *   
   * *    
    *     
'''