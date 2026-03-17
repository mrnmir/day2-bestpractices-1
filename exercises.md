# Exercises for Day 2
Organising, debugging and profiling Python code

## 1. Creating a Python package
Following the slides from this morning's session, we will create an **animals** package.

> Please note that with Python 3, implicit relative imports are no longer supported [https://www.python.org/dev/peps/pep-0328/](https://www.python.org/dev/peps/pep-0328/)

#### a. Create a directory for package

#### b. Add the modules ```birds.py``` and ```mammals.py``` into your package directory

#### c. Add ```__init__.py``` module to your package
The ```__init__.py``` module should import the ```Birds``` and ```Mammals``` class from the two modules.

#### d. Test your animals package
Using a python script or an interactive python session outside the package, test your brand new package:

```
import animals

m = animals.Mammals()
m.printMembers()

b = animals.Birds()
b.printMembers()
```

#### e. Add another module called ```fish.py``` amd integrate it into your package

#### f. Reorganize your package such that you can use it like this:
```
import animals

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()
```

#### g. Run ```ruff``` on the files of your package

## 2. Debugging
Investigate buggy code using the *pdb* or *ipdb* debugger. Have a look at slides of this mornings's session for help.

#### a. Find all the bugs in the dicegame
Clone this repo (if you have not already done so), go to ```buggy```  and run the ```main.py``` with a debug tracer added to the code. Once you have fixed all errors, the game should correctly add up the values of the dice for 6 consecutive turns.

#### b. If you cannot get enough of debugging
Ask your neighbour to introduce more bugs into the above (or any other) code examples and try to find the bug using the debugger. 

## 3. Profiling
In this section, you should get more familiar with code profiling, in particular with the tools ```cProfile```, ```line_profiler``` and ```scalene```. Have a look at slides from this morning's session to understand what they are doing and when you should use them. Try out profiling both from the command line and using interactive python (e.g. jupyter notebook). If you get ```Command not found``` when running kernprof try searching for it in `~/.local/bin/kernprof`. Alternatively install it using Anaconda/conda (e.g. `conda install line_profiler`).

#### a. Investigate the performance of the ```matmult.py``` script
In which line(s) of the script would you start optimizing for speed?

#### b. Investigate the performance of the ```euler72.py``` script
In which line(s) of the script would you start optimizing for speed?
(This is one problem from the euler project: [https://projecteuler.net/problem=72](https://projecteuler.net/problem=72))

#### c. Improve the performance of the ```matmult.py``` script
What is the best performance that you achieved with N=250?

File: /Users/mirma246/Desktop/python_course_day2/day2-bestpractices-1/matmult.py
Function: matmult at line 6


#### Before:
```
Timer unit: 1e-09 s

Total time: 6.31831 s
File: /Users/mirma246/Desktop/python_course_day2/day2-bestpractices-1/matmult_original.py
Function: matmult at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           def matmult(N):
     7                                               # NxN matrix
     8         1          0.0      0.0      0.0      X = []
     9       251      29000.0    115.5      0.0      for i in range(N):
    10       250  125256000.0 501024.0      2.0          X.append([random.randint(0,100) for r in range(N)])
    11                                           
    12                                               # Nx(N+1) matrix
    13         1          0.0      0.0      0.0      Y = []
    14       251      16000.0     63.7      0.0      for i in range(N):
    15       250  123982000.0 495928.0      2.0          Y.append([random.randint(0,100) for r in range(N+1)])
    16                                           
    17                                               # result is Nx(N+1)
    18         1          0.0      0.0      0.0      result = []
    19       251      18000.0     71.7      0.0      for i in range(N):
    20       250    1005000.0   4020.0      0.0          result.append([0] * (N+1))
    21                                           
    22                                               # iterate through rows of X
    23       251      29000.0    115.5      0.0      for i in range(len(X)):
    24                                                   # iterate through columns of Y
    25     63000    7107000.0    112.8      0.1          for j in range(len(Y[0])):
    26                                                       # iterate through rows of Y
    27  15750250 1566197000.0     99.4     24.8              for k in range(len(Y)):
    28  15687500 4423155000.0    282.0     70.0                  result[i][j] += X[i][k] * Y[k][j]
    29                                           
    30       251      62000.0    247.0      0.0      for r in result:
    31       250   71457000.0 285828.0      1.1          print(r)
```
#### After:
```
Timer unit: 1e-09 s

Total time: 0.039587 s
File: /Users/mirma246/Desktop/python_course_day2/day2-bestpractices-1/matmult_optimized.py
Function: matmult at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           def matmult(N):
     8                                               # NxN matrix
     9         1       1000.0   1000.0      0.0      X = []
    10         1   28540000.0 2.85e+07     72.1      X = np.random.randint(0, 101, size=(N, N))
    11                                           
    12                                               # Nx(N+1) matrix
    13         1          0.0      0.0      0.0      Y = []
    14         1     497000.0 497000.0      1.3      Y = np.random.randint(0, 101, size=(N, N+1))
    15         1   10549000.0 1.05e+07     26.6      result = np.dot(X, Y)
    16         1          0.0      0.0      0.0      return result
```
