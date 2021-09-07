#  print the pattern 1,-2,3,-4...

# WHILE LOOP
i=0
while i<=100:
    if i%2==0:
       print(-i)
    else:
         print(i)
    i+=1

# FOR LOOP
for i in range (0,101,2):
   print(-i)
   print(i)