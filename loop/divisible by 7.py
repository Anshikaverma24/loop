#print the number divisible by 7 between 1 to 100 

# WHILE LOOP
i=1
while i<=100:
    if i%7==0:
      print(i)
    i+=1

# FOR LOOP
for i in range (1,101,6):
    print(i)