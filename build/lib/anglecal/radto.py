from degto import deg_degminsec

def rad_deg(rad) :
    pie = 3.141592653589793
    rad1 = 180.0 / pie
    deg = rad * rad1
    return deg

def rad_degminsec(rad):
    degree = rad_deg(rad)
    degminsec = deg_degminsec(degree)
    return degminsec
