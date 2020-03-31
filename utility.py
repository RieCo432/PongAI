from math import pi, sqrt


def mod2pi(angle):  # Simple function to emulate modulo 2 pi to keep angle value in range for the collision boxes

    while angle < pi:
        angle += 2 * pi
    while angle > pi:
        angle -= 2 * pi

    return angle


def get_dist(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


white = (255, 255, 255)
black = (0, 0, 0)