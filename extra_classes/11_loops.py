# ehile loops and for loops
 #hile loops
 #while loop is used to execute a
 # block of code as long as the 
 # condition remains true.
 
#hile loops
# x=0
# while(x<=5):
#     print(x)
#     x=x+1

# for loop
# for x in range(4,11):
#     print(x)

#array
days = ["mon", "tues", "ved",
        "thurs", "fri", "sat", "sun",]

for d in days:
    # if d == "fri":break #loops stops
    if d == "fri":continue # skips the d
    print(d)