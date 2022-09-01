import numpy as np
import distance as tdist
if __name__ == '__main__':
    traj_1 = np.array([[1,1],[1,2],[3,2],[4,4],[5,4],[6,4]],dtype=float)
    traj_3 = np.array([[0,1],[4,2],[4,4],[3,6],[5,5],[6,4]],dtype=float)
    dist = tdist.dtw(traj_1, traj_3)
    print(dist)
    dist = tdist.frechet(traj_1, traj_3)
    print(dist)
    dist = tdist.edr(traj_1, traj_3,eps=1)
    print(dist)
    dist = tdist.lcss(traj_1, traj_3,delta=1,eps=1,)
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
