# Max-Cut and Goemans-Williamson

<p align="center">
<img src="figures/front-figure-crop.png" alt="Max-Cut and SDP Relaxation" width="600">
</p>

<p align = "center">
<strong>Figure 1:</strong> An example of a maximum cut and a set of positive semidefinite matrices.
</p>

## Introduction
This repository contains a simple implementation [maxcut.py](https://github.com/markolalovic/max-cut-sdp/blob/299c5b53ca27fa8952eca8edd8e67eb1f5cd2982/maxcut.py) in Python using CVXPY [1] of Goemans-Williamson algorithm [2] for Max-Cut problem of finding a maximum cut of a graph. **Figure 1A** shows maximum cut of a cycle on 5 vertices. 

Goemans-Williamson algorithm achieves the best known approximation for Max-Cut problem that runs in polynomial time. It is using semidefinite programming (SDP) and hyperplane rounding technique. The SDP approach is based on representation of cuts by positive semidefinite matrices. **Figure 1B** shows the set of all 3x3 correlation matrices. The vertices (corners) of this set correspond to all the cuts of complete graph on 3 vertices. 

You can read more in the [summary](https://github.com/markolalovic/max-cut-sdp/raw/299c5b53ca27fa8952eca8edd8e67eb1f5cd2982/main.pdf) or check the presentation [slides](https://github.com/markolalovic/max-cut-sdp/raw/299c5b53ca27fa8952eca8edd8e67eb1f5cd2982/beamer/slides.pdf) for a quick overview.

## How-To
Dependencies are `NumPy` and `CVXPY`. They can be installed for example by using Pip:
```Bash
pip install numpy
pip install cvxpy
```

To find the best known approximation for Max-Cut problem in polynomial time, for example for a cycle on 5 vertices `[0, 1, 2, 3, 4]`, shown in Figure 1A, run:
```Python
## Import the functions
from maxcut import *

## Define a graph
n = 5
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]

## Run Goemans-Williamson algorithm
x = gw(n, edges)

## Find edges in the cut
xcut = cut(x, edges)

## Print results
print('Chosen subset: %s' % np.where(x == 1))
print('Cut size: %i' % len(xcut) )
print('Edges of the cut: %s' % xcut )
```
Algorithm is randomized and returns a random cut, but guarantees that `cut-size > 0.878 * max-cut-size`. For example above, the chosen subset and corresponding cut may vary, but the cut size will always be 4:
```
Chosen subset: [1 4]
Cut size: 4
Edges of the cut: [(0, 1), (1, 2), (3, 4), (0, 4)]
```

## References
[1]: Diamond and Boyd. "CVXPY: A Python-embedded modeling language for convex optimization", version 1.2. [https://www.cvxpy.org/](https://www.cvxpy.org/)

[2]: Goemans and Williamson. "Improved approximation algorithms for maximum cut and
  satisfiability problems using semidefinite programming". J. ACM, 42(6):1115–1145, 1995.
  [http://www-math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf](http://www-math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf)
