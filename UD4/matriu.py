import numpy as np
temperatures = np.array([
    [18, 20, 17],
    [19, 21, 18],
    [17, 19, 16],
    [22, 24, 20],
    [21, 23, 19],
    [15, 22, 18],
    [18, 20, 17]
])

print(temperatures)

print(temperatures[4,1])

print(temperatures[3,0])

print(temperatures [:,2])

print(temperatures [0,:])

print(temperatures [0,:] [1,:])

print(temperatures [2:5,0])

print(temperatures [temperatures < 18] )

print(temperatures[temperatures > 20 ])

print(temperatures [temperatures == 19])




