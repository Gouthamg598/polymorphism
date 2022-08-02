"""polymorphism is defined as the method in child class is same as the method in parent class"""
class polymorphism:
    def  country(self):
        print("India")

class ch1(polymorphism):
    def country(self):
        print('USA')

class ch2(polymorphism):
    def country(self):
        print("UK") 

class ch3(polymorphism):
    def country(self):
        print("australia")

p=polymorphism()
c1=ch1()
c2=ch2()
c3=ch3()
p.country()     #India
c1.country()    #USA
c2.country()    #UK
c3.country()    #australia

'''===========using for loop========'''
class india:
    def country(self):
        pass
    def languages(self):
        print("different languages used in india")
    def religions(self):
        print("all kinds of religions")
    def states(self):
        print('30 states in india')

class us:
    def country(self):
        pass
    def languages(self):
        print("most of them use english")
    def religions(self):
        print("christians")
    def states(self):
        print("50 states in us")
i=india()
u=us()
for c in (i,u):
    c.country()
    c.languages()
    c.religions()
    c.states()

'''===output==='''

# different languages used in india
# all kinds of religions
# 30 states in india
# most of them use english
# christians
# 50 states in us

'''============using function========''
class trans:
    def transport(self):
        print("indian railways is the largest transportaion  in india system handle by the central government")
    def people(self):
        print("daily lakhs of people travelling in railways")
    def km(self):
        print("67,956 KM of railway track is available in india")
class road:
    def transport(self):
        print("road transportation is the second largest transportation in india")
    def people(self):
        print("most of the travell by roads ")
    def km(self):
        print("15100 KM natioanl ways in india ")

def fun(ob):
    ob.transport()
    ob.people()
    ob.km()
t=trans()
r=road()
fun(t)
fun(r)
    
'''==========output=========='''
# indian railways is the largest transportaion  in india system handle by the central government
# daily lakhs of people travelling in railways
# 67,956 KM of railway track is available in india
# road transportation is the second largest transportation in india
# most of the travell by roads
# 15100 KM natioanl ways in india
