import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import numpy as np

def star_points(center, outer_radius, inner_radius):
    """Generate the points of a five-pointed star given a center, outer radius, and inner radius."""
    points = []
    angle = np.pi / 5
    for i in range(5):
        # Outer points
        x_outer = center[0] + outer_radius * np.cos(i * 2 * angle + np.pi / 2)
        y_outer = center[1] + outer_radius * np.sin(i * 2 * angle + np.pi / 2)
        points.append((x_outer, y_outer))
        
        # Inner points
        x_inner = center[0] + inner_radius * np.cos((i * 2 + 1) * angle + np.pi / 2)
        y_inner = center[1] + inner_radius * np.sin((i * 2 + 1) * angle + np.pi / 2)
        points.append((x_inner, y_inner))
    
    return points

def interpolate(p1, p2, t):
    """Interpolate between two points p1 and p2 with parameter t (0 <= t <= 1)."""
    return p1[0] * (1 - t) + p2[0] * (t), p1[1] * (1 - t) + p2[1] * (t)

def animate_frame(i, ax, flag_points, star_points):
    # print('frame: ', i)
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 2)
    ax.axis('off')

    # Draw flag boundary
    if i < 100:
        t = i / 25
        idx = int(t) % 4
        t = t - int(t)
        if idx < 3:
            p1, p2 = flag_points[idx], flag_points[idx + 1]
        else:
            p1, p2 = flag_points[3], flag_points[0]
        interpolated_point = interpolate(p1, p2, t)
        ax.plot([p1[0], interpolated_point[0]], [p1[1], interpolated_point[1]], color='red', lw=2)
        for j in range(idx):
            ax.plot([flag_points[j][0], flag_points[j + 1][0]], [flag_points[j][1], flag_points[j + 1][1]], color='red', lw=2)

    if i >= 100:
        # Fill the flag with red
        rect = patches.Rectangle((0, 0), 3, 2, linewidth=0, edgecolor='none', facecolor='red')
        ax.add_patch(rect)

    # Draw star
    if i >= 104 and i< 355:
        t = (i - 104) / 25
        idx = int(t) % 10
        t = t - int(t)
        if idx < 9:
            p1, p2 = star_points[idx], star_points[idx + 1]
        else:
            p1, p2 = star_points[9], star_points[0]
        interpolated_point = interpolate(p1, p2, t)
        ax.plot([p1[0], interpolated_point[0]], [p1[1], interpolated_point[1]], color='yellow', lw=2)
        for j in range(idx):
            ax.plot([star_points[j][0], star_points[j + 1][0]], [star_points[j][1], star_points[j + 1][1]], color='yellow', lw=2)

    if i >= 354:
        # Fill the star with yellow
        star = patches.Polygon(star_points, closed=True, linewidth=0, edgecolor='none', facecolor='yellow')
        ax.add_patch(star)

def main():
    flag_points = [(0, 0), (3, 0), (3, 2), (0, 2)]
    
    center = (1.5, 1)
    outer_radius = 0.5
    inner_radius = outer_radius / 2.5
    star_pts = star_points(center, outer_radius, inner_radius)
    
    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig, animate_frame, frames=380, repeat=False, fargs=(ax, flag_points, star_pts))
    
    # Save the animation
    ani.save('vietnam_flag_animation.gif', writer='pillow', fps=10)

    plt.show()

if __name__ == "__main__":
    main()
