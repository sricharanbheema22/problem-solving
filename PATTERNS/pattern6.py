n = int(input("num: "))
for i in range(n):
  print(" " * i ,end = "")
  print("* " *  (n-i))
for j in range(n):
  print(" " * (n-j-1),end = "")
  print("* " * (j+1))
'''
num: 5
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''