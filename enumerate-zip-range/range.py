range(10) # 0-10

list(range(10)) # [0,1,2,3,4,5,6,7,8,9]
#or
[*range(10)] # [0,1,2,3,4,5,6,7,8,9] => Broadcasting

[*range(2,7)] # [2,3,4,5,6]
#
[*range(2,7,2)] # [2,4,6]
#

for i in range(10):
   print(i)       # [0,1,2,3,4,5,6,7,8,9]

#
for j in range(10):
   if j>5:
      print(j) # [6,7,8,9]
      
      
