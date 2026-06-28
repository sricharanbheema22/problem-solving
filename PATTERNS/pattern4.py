n = int(input("num: "))
for i in  range(1,n+1):
  print(" " * (n-i),end = "")
  print("* " * i)

'''
num: 5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''