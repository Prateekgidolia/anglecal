def deg_degminsec(degree):
    deg = int(degree)
    next = (degree - deg)*60
    minute = int(next)
    next = (next - minute)*60
    sec = int(next)
    return deg, minute, sec


def deg_rad(degree) :
    pie = 3.141592653589793
    deg1 = pie / 180.0
    rad = degree * deg1
    return rad

