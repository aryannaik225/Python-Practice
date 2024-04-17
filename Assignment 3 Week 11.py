def spiral_recursive(left, right, n):
    if n == 2:
        return (left + right) / 2
    else :
        center = (left + right) / 2
        return spiral_recursive(right, center, n-1) 

def spiral_iterative(left, right, n):
    for i in range(n):
        center = (left + right)/2
        left = right
        right = center
    return center

print(spiral_recursive(0,1,4))
print(spiral_iterative(0,1,100))