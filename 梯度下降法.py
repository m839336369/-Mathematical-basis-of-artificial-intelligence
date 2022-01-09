import matplotlib.pyplot as plt
import sympy as sym
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sympy import symbols, diff

x, y = symbols("x,y")
Func = x - y + 2 * x * x + 2 * x * y + y * y
PxFunc = diff(Func, x)
PyFunc = diff(Func, y)
ax = plt.figure().add_subplot(111, projection='3d')
X, Y = np.mgrid[-1:2:40j, -2:2:40j]
Z = sym.lambdify(('x', 'y'), Func, "numpy")(X, Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="rainbow")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
step = 0.0008
now_x = 0
now_y = 0
tag_x = [now_x]
tag_y = [now_y]
tag_z = [Func.evalf(subs={x: now_x, y: now_y})]
new_x = now_x
new_y = now_y
Over = False
while Over is False:
    new_x -= step * PxFunc.evalf(subs={x: now_x, y: now_y})
    new_y -= step * PyFunc.evalf(subs={x: now_x, y: now_y})
    if Func.evalf(subs={x: now_x, y: now_y}) - Func.evalf(subs={x: new_x, y: new_y}) < 7e-9:
        Over = True
    now_x = new_x
    now_y = new_y
    tag_x.append(now_x)
    tag_y.append(now_y)
    tag_z.append(Func.evalf(subs={x: now_x, y: now_y}))
ax.plot(tag_x, tag_y, tag_z, 'bo')
plt.title('(x,y)~(' + str(x) + "," + str(y) + ')')
plt.show()
