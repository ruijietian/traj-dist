# trajectory_distance
=====================

**trajectory_distance** is a Python module for computing distances between 2D-trajectory objects.
It is implemented in Python.

## Description

5 distances between trajectories are available in the **trajectory_distance**  package.

1. Frechet [1]
2. Hausdorff [2]
3. Discret Frechet [3]
4. DTW (Dynamic Time Warping) [4]
5. LCSS (Longuest Common Subsequence) [5]
6. EDR (Edit Distance on Real sequence) [6]

* All distances but *Discret Frechet* and *Discret Frechet* are are available with *Euclidean* option :
 *  *Euclidean* is based on Euclidean distance between 2D-coordinates.

* Python implementation is also available in this depository but are not used within `distance` module.

## Dependencies

**trajectory_distance** is tested to work under Python 3.6 and the following dependencies:
 
* NumPy >= 1.16.2
* shapely >= 1.6.4.post2
* geohash2 == 1.1
* pandas >= 0.24.2
* scipy >= 0.20.3

## How to use it

You only need to import the distance module.

```
import distance as tdist
```

All distances are in this module. There are also two extra functions 'cdist', and 'pdist' to compute pairwise distances between all trajectories in a list or two lists. 

Trajectory should be represented as nx2 numpy array. 
See `traj-dist/benchmark.py` file for a small working exemple. 

Some distance requires extra-parameters.
See the help function for more information about how to use each distance.

See `traj_dist/benchmark.py` to generate this benchmark on your computer.

## References

1. *H.  Alt  and  M.  Godau,  “Computing  the  frechet  distance  between  two
polygonal curves,”
International Journal of Computational Geometry &
Applications
, vol. 5, no. 01n02, pp. 75–91, 1995.*
2. *F. Hausdorff, “Grundz uge der mengenlehre,” 1914*
3. *D. J. Berndt and J. Clifford , “Using dynamic time warping to find patterns in time series.” in KDD workshop, vol. 10, no. 16. Seattle, WA, 1994, pp. 359–370* 
4. *M. Vlachos, G. Kollios, and D. Gunopulos, “Discovering similar multi-
dimensional trajectories,” in
Data Engineering, 2002. Proceedings. 18th
International Conference on
.IEEE, 2002, pp. 673–684*
5. *L. Chen, M. T. ̈
Ozsu, and V. Oria, “Robust and fast similarity search for
moving object trajectories,” in Proceedings of the 2005 ACM SIGMOD
international  conference  on  Management  of  data
.      ACM,  2005,  pp.
491–502.*

