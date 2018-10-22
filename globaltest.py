def global1():
    print (t)

def global2():
    global t
    t=2
    print (t)

t = 1

global1()
global2()
print(t)
