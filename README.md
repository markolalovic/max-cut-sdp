# Max-Cut and Goemans-Williamson

<p align="center">
<img src="figures/front-figure-crop.png" alt="Max-Cut and SDP Relaxation" width="1500">
</p>

## Introduction

This repository contains a simple implementation [maxcut.py](https://github.com/markolalovic/max-cut-sdp/blob/299c5b53ca27fa8952eca8edd8e67eb1f5cd2982/maxcut.py) in Python using CVXPY [1] of Goemans-Williamson algorithm [2] for Max-Cut problem of finding a maximum cut of a graph

You can read more in the [summary](https://github.com/markolalovic/max-cut-sdp/raw/299c5b53ca27fa8952eca8edd8e67eb1f5cd2982/main.pdf) or check the presentation [slides](https://github.com/markolalovic/max-cut-sdp/raw/299c5b53ca27fa8952eca8edd8e67eb1f5cd2982/beamer/slides.pdf) for a quick overview.

## References
[1]: Diamond and Boyd. "CVXPY: A Python-embedded modeling language for convex optimization", version 1.2. [https://www.cvxpy.org/](https://www.cvxpy.org/)

[2]: Goemans and Williamson. "Improved approximation algorithms for maximum cut and
  satisfiability problems using semidefinite programming". J. ACM, 42(6):1115–1145, 1995.
  [http://www-math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf](http://www-math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf)
