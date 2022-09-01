# Tinba: Incremental Partitioning Framework for Efficient Trajectory Analytics

**trajectory_distance** is a Python module for computing distances between 2D-trajectory objects.
It is implemented in Python.

## Description

5 distances between trajectories are available in the **trajectory_distance**  package.

1. Frechet [1]
2. DTW (Dynamic Time Warping) [2]
3. LCSS (Longuest Common Subsequence) [3]
4. EDR (Edit Distance on Real sequence) [4]

* All distances are available with *Euclidean* option :
 *  *Euclidean* is based on Euclidean distance between 2D-coordinates.

* Python implementation is also available in this depository but are not used within `distance` module.

## Dependencies

**trajectory_distance** is tested to work under Python 3.6 and the following dependencies:
 
* NumPy >= 1.17.3
* shapely >= 1.8.4
* geohash2 == 1.1
* pandas >= 0.25.2
* scipy >= 1.3.2

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

See `traj-dist/benchmark.py` to generate this benchmark on your computer.

## References

1. *H.  Alt  and  M.  Godau,  “Computing  the  frechet  distance  between  two polygonal curves,”
International Journal of Computational Geometry & Applications , vol. 5, no. 01n02, pp. 75–91, 1995.*
2. *D. J. Berndt and J. Clifford , “Using dynamic time warping to find patterns in time series.” in KDD workshop, vol. 10, no. 16. Seattle, WA, 1994, pp. 359–370.* 
3. *M. Vlachos, G. Kollios, and D. Gunopulos, “Discovering similar multi-dimensional trajectories,” in Data Engineering, 2002. Proceedings. 18th
International Conference on .IEEE, 2002, pp. 673–684.*
4. *L. Chen, M. T. ̈Ozsu, and V. Oria, “Robust and fast similarity search for moving object trajectories,” in Proceedings of the 2005 ACM SIGMOD international  conference  on  Management  of  data. ACM, 2005,  pp. 491–502.*
