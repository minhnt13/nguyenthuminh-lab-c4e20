def is_inside(point, rect):
    x_point = point[0]
    y_point = point[1]
    x_A = rect[0]
    y_A = rect[1]
    x_D = rect[0] + rect[2]
    y_D = rect[1] + rect[3]
    if x_A <= x_point <= x_D:
        if y_A <= y_point <= y_D:
            return True
    else:
        return False

# check 
if is_inside([100, 120], [140, 60, 100, 200]):
    print("You have bugs")
elif is_inside([200, 120], [140, 60, 100, 200]):
    print("Your function is correct")
