from random import randint

name = input("Ismingizni kiriting:")
surname = input("Familyangizni kiriting:")

name1 = name[0]
rand = randint(0,100)

print(name+"."+surname)
print(surname+'_'+name)
print(surname+str(rand))
print(name1+surname)



