import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

def update(val):
    a = s_a.val
    b = s_b.val
    c = s_c.val

    l.set_ydata(a*x**2 + b*x + c)
    ax.set_title(title_format.format(a))
    fig.canvas.draw_idle()

title_format = '{:1f}'

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.3)
plt.axvline(x=0, color='gray', linestyle='dashed')
plt.axhline(y=0, color='gray', linestyle='dashed')

x = np.arange(-10, 10, 0.01)
a = 1
b = 1
c = 1

delta = 0.1

y = a*x**2 + b*x + c

l, = plt.plot(x, y) 
ax.set_title(title_format.format(a))
plt.ylim(-10,10)

ax_a = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_b = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_c = plt.axes([0.25, 0.2, 0.65, 0.03])

# Sliders
s_a = Slider(ax_a, 'a', -10, 10, valinit=a, valstep=delta)
s_b = Slider(ax_b, 'b', -10, 10, valinit=b, valstep=delta)
s_c = Slider(ax_c, 'c', -10, 10, valinit=c, valstep=delta)


s_a.on_changed(update)
s_b.on_changed(update)
s_c.on_changed(update)

plt.show()

