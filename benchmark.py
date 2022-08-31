import numpy as np
import distance as tdist
import pickle
if __name__ == '__main__':
    traj_A = np.array([[1,1],[1,2],[3,2],[4,4],[4,5],[5,5]],dtype=float)
    traj_B = np.array([[1,1],[4,1],[4,3],[4,5],[4,6],[5,6]],dtype=float)
    dist = tdist.dtw(traj_A, traj_B)
    print(dist)
    dist = tdist.frechet(traj_A, traj_B)
    print(dist)
    dist = tdist.edr(traj_A, traj_B,eps=1)
    print(dist)
    dist = tdist.lcss(traj_A, traj_B,eps=1)
    print(dist)
    
#traj_list = pickle.load(open("E:\code\traj-dist\data\benchmark_trajectories.pkl", "rb"))[:10]


# Simple distance

#dist = tdist.sspd(traj_A, traj_B)
#print(dist)

# Pairwise distance

#pdist = tdist.pdist(traj_list, metric="sspd")
#print(pdist)

# Distance between two list of trajectories

#cdist = tdist.cdist(traj_list, traj_list, metric="sspd")
#print(cdist)
