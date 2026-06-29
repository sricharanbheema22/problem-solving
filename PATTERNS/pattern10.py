list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
count = 0
for i in range(0,5):
  for j in range(0,i):
    print(list[count],end="")
    count +=1
  print()


cnt = 65
for i in range(5):
  for j in range(i):
    print(chr(cnt),end="")
    cnt += 1
  print()

'''
A
BC
DEF
GHIJ
'''