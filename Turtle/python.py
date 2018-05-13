#这是一个蟒蛇绘制代码
import turtle as t
t.setup(600,300,400,400)
t.pencolor('red')
t.pensize(10)
t.penup()
t.fd(-250)
t.pendown()
t.right(40)
for i in range(4):
    t.circle (40,80)
    t.circle (-40,80)
t.circle (40,80/2)
t.fd(40)
t.circle(20,180)
t.fd(20)
