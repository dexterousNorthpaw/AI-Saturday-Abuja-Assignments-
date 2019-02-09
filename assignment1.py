#Assignment1
my_dict = { "fullName" : "Rayhan" , "reason": "be able implement AI in different fields" }

print('My name is ' + my_dict['fullName'] + ' and at the end of this cohort I want to ' + my_dict['reason']) 

numbers=[1,2,3,4,5,6,7,8,9]
odd=0
even=0
for i in numbers:
    if i%2==0:
        even+=1
    elif i%2==1:
        odd+=1


print("Number of even numbers is", even)
print("Number of Odd numbers is", odd)
