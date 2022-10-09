import time
from result import *


def esdf(M, N, obstacle_list):
    """
    :param M: Row number
    :param N: Column number
    :param obstacle_list: Obstacle list
    :return: An array. The value of each cell means the closest distance to the obstacle
    """
    grid = np.zeros((M, N))
    grid[:, :] = np.inf
    dgrid = np.zeros((M, N))
    dgrid[:, :] = np.inf
    for (i, j) in obstacle_list:
        grid[i, j] = 0
        dgrid[i, j] = 0
    # print(grid)
    for i in range(M):
        v = np.zeros(N, dtype=int)
        z = np.zeros(N)
        k = 0
        v[0] = -1
        z[:] = np.inf
        z[0] = -np.inf
        q = 0
        while q < N:
            if grid[i, q] != np.inf:
                if v[k] == -1:
                    v[k] = q
                    k += 1
                else:
                    s = (q**2 - v[k]**2) / (2*(q-v[k]))
                    if s <= z[k]:
                        k -= 1
                        q -= 1
                    else:
                        k += 1
                        v[k] = q
                        z[k] = s
                        z[k+1] = np.inf
            q += 1
        k = 0
        if v[0] != -1:
            for q in range(N):
                while k+1 < N and z[k+1] < q:
                    k += 1
                dgrid[i, q] = (q-v[k])**2
    
    ###Column###
    for j in range(N):
        v = np.zeros(M, dtype=int)
        z = np.zeros(M)
        k = 0
        v[0] = 0
        z[:] = np.inf
        z[0] = -np.inf
        q = 1
        # print(dgrid)
        while q < M:
            if dgrid[q, j] == np.inf or dgrid[q, v[k]] == np.inf:
                q += 1
                continue

            s = (dgrid[q, j] + q**2 - dgrid[v[k], j] - v[k]**2) / (2*(q-v[k]))
            if s <= z[k]:
                k -= 1
                q -= 1
            else:
                k += 1
                v[k] = q
                z[k] = s
                z[k+1] = np.inf
            q += 1
        k = 0

        for q in range(M):
            while k+1 < M and z[k+1] < q:
                k += 1
            dgrid[q, j] = min(dgrid[q,j], (q-v[k])**2 + dgrid[v[k], j])
    # print(np.sqrt(dgrid))
    return np.sqrt(dgrid)

if __name__ == '__main__':
    st = time.time()
    for _ in range(int(2e4)):
        assert np.array_equal(esdf(M=3, N=3, obstacle_list=[[0, 1], [2, 2]]), res_1)
        assert np.array_equal(esdf(M=4, N=5, obstacle_list=[[0, 1], [2, 2], [3, 1]]), res_2)
        
    et = time.time()
    print(et-st)
