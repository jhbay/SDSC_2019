from math import radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()

world_name = ' ///////// Earth-322222';
print('hello - ' + world_name);

# for loop ex.
for i in range(0,5):
    print('hi' + str(i))


