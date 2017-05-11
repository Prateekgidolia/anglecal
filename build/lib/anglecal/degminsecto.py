from degto import deg_rad
    

def degminsec_deg(a) :
    if (type(a) == tuple) :
        deg = a[0] + a[1]/60.0 + a[2]/3600.0
        return deg
    else :
        return "Wrong input data type. It should be Tuple (degree, Minute, second)"

def degminsec_rad(a) :
    if (type(a) == tuple) :
        deg = degminsec_deg(a)
        rad = deg_rad(deg)
        return rad
    else :
        return "Wrong input data type. It should be Tuple (degree, Minute, second)"
