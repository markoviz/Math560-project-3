"""
Math 560
Project 3
Fall 2021

Partner 1:GEN XU (Net id 1082087)
Partner 2:
Date: 11/10
"""

# Import math, p3tests and p3currencies
import math
from p3tests import *
from p3currencies import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    # set all vertex have infinity distance and no previous vertex
    for vert in adjList:
        vert.dist = math.inf
        vert.prev = None
    # set distance of the start vertex be 0
    adjList[0].dist = 0

    # for each iterations:
    for ite in range(len(adjList)-1):
        # for each vertex v in the graph
        for v in adjList:
            # for each neighbour vertex of v
            # update distance of u if the new distance is smaller than the old
            for u in v.neigh:
                if u.dist > v.dist + adjMat[v.rank][u.rank] + tol:
                    u.dist = v.dist + adjMat[v.rank][u.rank]
                    u.prev = v

    # find the arbitrage path if there is a negative cost cycle.
    # set an empty array
    v_rank = []
    # let v_1 = u, and u is obtained from the function 'extraIteration'
    v_1 = extraIteration(adjList, adjMat, tol)
    # if v_1 exists, append the path backwards
    if v_1 != None:
        curr = v_1
        v_rank = [v_1.rank]
        # append vertex that belongs to the path
        while curr.prev.rank not in v_rank:
            v_rank.append(curr.prev.rank)
            curr = curr.prev
        v_rank.append(curr.prev.rank)

    # eliminate vertex not in the cycle
    index = -1
    # let index = the one that has the same rank
    # as the last vertex in the list
    for i in range(len(v_rank)):
        if v_rank[i] == v_rank[-1]:
            index = i
            break
    # slice the list and delete elements not in the cycle
    v_rank = v_rank[index:]
    # reverse the list of v_rank
    v_rank.reverse()
    return v_rank


# def a new function to do one more iteration to find the negative cost cycle
def extraIteration(adjList, adjMat, tol=1e-15):
    for v in adjList:
        for u in v.neigh:
            # if any vertex changes it value under this iteration
            # there exists a negative cost cycle, update u
            if u.dist > v.dist + adjMat[v.rank][u.rank] + tol:
                return u
    return None

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    # transforms rate to -log(rate) for rates in the  matrix.
    return [[-math.log(R) for R in row] for row in rates]

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
