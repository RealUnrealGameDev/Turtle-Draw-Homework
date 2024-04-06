import turtle as t

#Square
for i in range(4):
    t.fd(200)
    t.rt(90)

#first Triagle
t.lt(60)
t.fd(200)
t.rt(120)
t.fd(200)

#The Rest of the triangles
for i in range(3):
    t.lt(30)
    t.fd(200)
    t.rt(120)
    t.fd(200)



t.Screen().exitonclick()