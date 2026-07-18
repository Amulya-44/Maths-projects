import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

total_points = 1000000
batch_size = 5000

inside_x, inside_y = [], []
outside_x, outside_y = [], []

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

circle_theta = np.linspace(0, 2 * np.pi, 100)
ax.plot(np.cos(circle_theta), np.sin(circle_theta), color='black', linewidth=2, label='Unit Circle')

scatter_inside = ax.scatter([], [], color='blue', s=3, label='Inside Circle')
scatter_outside = ax.scatter([], [], color='red', s=3, label='Outside Circle')
ax.legend(loc='upper right')

def init():
    scatter_inside.set_offsets(np.empty((0, 2)))
    scatter_outside.set_offsets(np.empty((0, 2)))
    return scatter_inside, scatter_outside

def update(frame):

    new_points = np.random.uniform(-1, 1, (batch_size, 2))

    for x, y in new_points:
        if x**2 + y**2 <= 1:
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)

    scatter_inside.set_offsets(np.c_[inside_x, inside_y])
    scatter_outside.set_offsets(np.c_[outside_x, outside_y])
 
    current_inside = len(inside_x)
    current_total = current_inside + len(outside_x)
    pi_estimate = 4 * current_inside / current_total
    
    ax.set_title(f"Monte Carlo Pi Estimation\nPoints: {current_total} | Estimated Pi: {pi_estimate:.4f}")
    
    return scatter_inside, scatter_outside

frames_count = total_points // batch_size
ani = FuncAnimation(fig, update, frames=frames_count, init_func=init, blit=True, interval=1, repeat=False)

plt.show()

