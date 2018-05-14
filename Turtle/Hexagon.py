#这是个六角形的绘制代码
import turtle as t
t.color('red','yellow')
t.begin_fill()
for i in range(6):
    t.fd(100)
    t.right(60)
for i in range(6):
    t.left(60)
    t.fd(100)
    t.right(120)
    t.fd(100)
t.end_fill()
