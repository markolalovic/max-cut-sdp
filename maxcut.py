#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''maxcut.py: A simple implementation using CVXPY of Goemans-Williamson
algorithm for Max-Cut problem of finding a maximum cut of a graph:
  Goemans and Williamson. Improved approximation algorithms for maximum cut and
  satisfiability problems using semidefinite programming. J. ACM, 42(6):1115–1145, 1995.
  http://www-math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf

Algorithm is randomized and returns a random subset S, but with guarantee on S:
    cut-size(S) > 0.878 * max-cut-size

Example. For a cycle on 5 vertices [0, 1, 2, 3, 4] we get:
  Chosen subset: [1 4]
  Cut size: 4
  Edges of the cut: [(0, 1), (1, 2), (3, 4), (0, 4)]
'''

import numpy as np
import cvxpy as cp
from scipy.linalg import sqrtm

def gw(n, edges):
    '''Goemans-Williamson algorithm for Max-Cut:
    Given a graph G(V=[n], E=edges), returns a vector x \in {-1, 1}^n
    that corresponds to the chosen subset of vertices S of V. '''
    ## SDP Relaxation
    X = cp.Variable((n, n), symmetric=True)
    constraints = [X >> 0]
    constraints += [
        X[i, i] == 1 for i in range(n)
    ]
    objective = sum( 0.5*(1 - X[i, j]) for (i, j) in edges )
    prob = cp.Problem(cp.Maximize(objective), constraints)
    prob.solve()

    ## Hyperplane Rounding
    Q = sqrtm(X.value).real
    r = np.random.randn(n)
    x = np.sign(Q @ r)

    return x

def cut(x, edges):
    '''Given a vector x \in {-1, 1}^n and edges of a graph G(V=[n], E=edges),
    returns the edges in cut(S) for the subset of vertices S of V represented by x.'''
    xcut = []
    for i, j in edges:
        if np.sign(x[i]*x[j]) < 0:
            xcut.append((i, j))
    return xcut

def example():
    ''' Cycle on n=5 vertices. '''
    ## Define the graph
    n = 5
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]

    ## Define SDP Relaxation and solve it
    x = gw(n, edges)

    ## Find the edges of a cut
    xcut = cut(x, edges)

    ## Result
    print('Chosen subset: %s' % np.where(x == 1))
    print('Cut size: %i' % len(xcut) )
    print('Edges of the cut: %s' % xcut )

if __name__ == '__main__':
    example()
    
