import random
#monte carlo method for calculating pi
def calculate_pi():
    #define the square having length from -1 to 1
    #and breadth from -1 to 1
    #let radius of circle be 1
    iterations = int(input("Enter number of iterations:"))
    points_within_square=points_within_circle=0.0
    for i in range(iterations):
        (x,y)=(random.uniform(-1,1),random.uniform(-1,1))
        points_within_square+=1
        if (x**2) + (y**2)<=1:
            points_within_circle+=1
    pi = 4*points_within_circle/points_within_square
    print(f"Value of pi={pi}")
calculate_pi()