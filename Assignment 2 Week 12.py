# OK THIS NEEDS TO BE WRITTEN HERE

# A square metal plate in 2D space is the setup we are going to work with. The spatial extent of the metal plate is given by:

# 0 ≤ x,y ≤ 5

# The temperature at any point (x,y) on the plate is given by the following equation. The temperature is measured in Celsius and can be negative:

# f(x,y) = 30 + x^2 + y^2 − 3x − 4y

# A micro-organism lives on the surface of the metal plate. It occupies only those points on the plate where both the coordinates are integers. The organism cannot survive in high temperatures and instinctively moves to regions of low temperature that are less or equal to a threshold T. If no such region is found, it can't survive. The terms high and low are used in a relative sense and should be compared with respect to the threshold.

# Write a function named survival that accepts the value of T as argument and returns True if the organism can survive on the metal plate, and False otherwise.

def temperature(x,y):
    return (30+(x**2)+(y**2)-(3*x)-(4*y))


def survival(T):
    plate = []
    for rows in range(0,6):
        row = []
        for columns in range(0,6):
            row.append(temperature(rows,columns))
        plate.append(row)
    for rows in range(0,6):
        for columns in range(0,6):
            if plate[rows][columns] <= T:
                return True
    return False