import random as rnd
import time
import matplotlib.pyplot as plt


people=[100 for _ in range(50)]

for _ in range(0,100000):
    giver=rnd.randrange(0,50)
    reciever=rnd.randrange(0,50)

    while people[reciever]==0:
        reciever=rnd.randrange(0,50)
    
    if people[giver]!=0:
        people[giver] -= 1
        people[reciever] += 1

sorted_people = sorted(people)

print(sorted_people)
non_zero_people = [money for money in people if money != 0]
print(f"length of the sorted people who has the money is : {len(non_zero_people)}")

x=list(range(50))
y=sorted(people)

plt.xlabel("person")
plt.ylabel("money")
plt.title(" random money distribution (*100000 times) !")

plt.bar(x,y)
plt.grid()
plt.show()

print(f"the time to handle this process is \"  {time.process_time()}  \" seconds ")

