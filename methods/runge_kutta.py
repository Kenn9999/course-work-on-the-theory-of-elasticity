def runge_kutta_method(f, x0, y0, h):
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + 0.5 * h, y0 + 0.5 * k1)
    k3 = h * f(x0 + 0.5 * h, y0 +0.5 * k2)
    k4 = h * f(x0 + h, y0 + k3)

    x_next = x0 + h
    y_next = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return x_next, y_next
