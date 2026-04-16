""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc

def approximate_pi(n): # Ex1
    x1, x2, y1, y2 = [], [], [], []
    for _ in range(n):
        x = (random.uniform(-1, 1))
        y = (random.uniform(-1, 1))
        if x**2 + y**2 <= 1:
             x1.append(x)
             y1.append(y)
        else:
             x2.append(x)
             y2.append(y)
    plt.scatter(x1, y1, c='red', s=0.1)
    plt.scatter(x2, y2, c='blue', s=0.1)
    plt.show()
    print(f'n = {n}')
    print(f'pi is approximated as {4*len(x1)/n}')
    return 4*len(x1)/n

def sphere_volume(n, d): #Ex2, approximation
    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)] #comprehension to create list of lists containing all coordinates of all points
    p_in = list(filter(lambda p: sum(c**2 for c in p) <= 1, points)) #lambda function to check if a point is inside the hypersphere, filter used to copy only these points over to p_in
    return (len(p_in) / n) * 2**d

def hypersphere_exact(n,d): #Ex2, real value
    vol = (m.pi**(d/2)) / m.gamma((d/2)+1)
    return vol

#Ex3: parallel code - parallelize for loop

def sphere_volume_parallel1(n,d,np=10):
    start = pc()
    with future.ProcessPoolExecutor() as ex:
        processes = [ex.submit(sphere_volume, n, d) for _ in range(np)]
        results = [p.result() for p in processes]
    stop = pc()
    avg = sum(results) / len(results)
    print(f"Parallel time of {d} and {n}: {stop-start}\nAverage value: {avg}")
    return avg

#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):

    return
    
def main():
    #Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
    #Ex2
    n = 100000
    d = 2
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")
    print(f"Approximate volume of {d} dimensional sphere = {sphere_volume(n,d)}")

    n = 100000
    d = 11
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")
    print(f"Approximate volume of {d} dimensional sphere = {sphere_volume(n,d)}")

    #Ex3
    n = 100000
    d = 11
    values = []
    start = pc()
    for y in range (10):
        v = sphere_volume(n,d)
        values.append(v)
    stop = pc()
    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    print(f"Average value: {sum(values) / len(values)}")
    sphere_volume_parallel1(n, d, 10)
    

    #Ex4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    
    

if __name__ == '__main__':
	main()
