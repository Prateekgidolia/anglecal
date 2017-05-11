from radto import *
from degto import *
from degminsecto import *


for_rad = 0
for_deg = 1
for_dms = 2


def check(angle1, intype1, angle2, intype2, out_type) :
# if output demands in radian...
    if (out_type == 0) : 
        if (intype1 != out_type ) :
            if (intype1 == 1) :
                new1 = deg_rad(angle1)
            elif (intype1 == 2) :
                new1 = degminsec_rad(angle1)
            else :
                print("Given a wrong value for input data type.")
        else :
            new1 = angle1

        if (intype2 != out_type ) :
            if (intype2 == 1) :
                new2 = deg_rad(angle2)
            elif (intype2 == 2) :
                new2 = degminsec_rad(angle2)
            else :
                print("Given a wrong value for input data type.")
        else :
            new2 = angle2



# if output demands in degree...
    elif (out_type == 1) : 
        if (intype1 != out_type ) :
            if (intype1 == 0) :
                new1 = rad_deg(angle1)
            elif (intype1 == 2) :
                new1 = degminsec_deg(angle1)
            else :
                print("Given a wrong value for input data type.")
        else :
            new1 = angle1

        if (intype2 != out_type ) :
            if (intype2 == 0) :
                new2 = rad_deg(angle2)
            elif (intype2 == 2) :
                new2 = degminsec_deg(angle2)
            else :
                print("Given a wrong value for input data type.")
        else :
            new2 = angle2



# if output demands in degree/minute/second...
    elif (out_type == 2) : 
        if (intype1 != 1 ) :
            if (intype1 == 0) :
                new1 = rad_deg(angle1)
            elif (intype1 == 2) :
                new1 = degminsec_deg(angle1)
            else :
                print("Given a wrong value for input data type.")
        else :
            new1 = angle1

        if (intype2 != 1 ) :
            if (intype2 == 0) :
                new2 = rad_deg(angle2)
            elif (intype2 == 2) :
                new2 = degminsec_deg(angle2)
            else :
                print("Given a wrong value for input data type.")
        else :
            new2 = angle2

    else :
        print ("Given a wrong value for output data type.")


    return new1, new2


def addition(angle1, intype1, angle2, intype2, out_type) :
    numb = check(angle1, intype1, angle2, intype2, out_type)
    add = numb[0] + numb[1]
    if (out_type == 2) :
        addfinal = deg_degminsec(add)
    else :
        addfinal = add
    return addfinal



def subtract(angle1, intype1, angle2, intype2, out_type) :
    numb = check(angle1, intype1, angle2, intype2, out_type)
    sub = numb[0] - numb[1]
    if (out_type == 2) :
        subfinal = deg_degminsec(sub)
    else :
        subfinal = sub
    return subfinal
