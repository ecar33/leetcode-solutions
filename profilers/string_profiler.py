import matplotlib as plt
import numpy as np
import string
import random
import time



def str_generator(size=6, chars=string.ascii_lowercase + string.digits + string.whitespace):
    return ''.join(random.choice(chars) for _ in range(size))

input_str = [str_generator(size = random.randrange(0,20)) for _ in range(20)]
print(input_str)


step = 2
def profile_function(f, n):
    '''Profile `f' by applying it on input strings of
    progressively increasing length up to `n'.'''
    runtimes = []
    for i in range(0, n, step):
        input_str = str_generator(size=i)
        start = time.perf_counter()
        f(input_str)
        runtimes.append([i, time.perf_counter() - start])
    return runtimes

def plot_runtimes(r, fitDegree, title):
    '''Plot runtimes along with a polynomial fit of `fitDegree' degree.
    By default don't create figure / show the plot, so that we can call
    this function inside a subplot() context.'''
    #plt.figure()
    plt.scatter(*zip(*r), s=5)
    plt.xlabel('Input string length')
    plt.ylabel('Execution time in sec')
    plt.title(title)

    # Add a polynomial fit
    if fitDegree >= 0:
        model = np.poly1d(np.polyfit(*zip(*r), fitDegree))
        polyline = np.linspace(1, len(r) * step, 50)
        plt.plot(polyline, model(polyline), 'r')
    #plt.show()