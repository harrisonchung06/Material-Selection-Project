from __future__ import annotations
import utils, consts, mats
import argparse
import math
import random
from copy import deepcopy

def main(mat: utils.Material):
    #seed = 239
    #random.seed(seed)
    S = 700
    n = 150

    # Hyperparameters
    w  = 0.2
    c = [0.1,0.1]

    # Initialise swarm
    p = []
    for i in range(S):
        pos = utils.Circ_Design(mat, random.uniform(consts.LIM[0], consts.LIM[1]), random.uniform(consts.LIM[0], consts.LIM[1]))
        vel = utils.Circ_Design(mat, random.uniform(consts.V_LIM[0], consts.V_LIM[1]), random.uniform(consts.V_LIM[0], consts.V_LIM[1]))
        #pos = utils.Rect_Design(mat, random.uniform(consts.LIM[0], consts.LIM[1]), random.uniform(consts.LIM[0], consts.LIM[1]), random.uniform(consts.LIM[0], consts.LIM[1]), random.uniform(consts.LIM[0], consts.LIM[1]))
        #vel = utils.Rect_Design(mat, random.uniform(consts.V_LIM[0], consts.V_LIM[1]), random.uniform(consts.V_LIM[0], consts.V_LIM[1]), random.uniform(consts.V_LIM[0], consts.V_LIM[1]), random.uniform(consts.V_LIM[0], consts.V_LIM[1]))
        p.append(utils.Particle(
            position=pos,
            velocity=vel,
            best_position=deepcopy(pos),
            best_score=math.inf   
        ))

    # PSO main loop
    for iteration in range(n): #For each iteration
        for i in range(S): #For each particle
            p[i].position = p[i].position+p[i].velocity

            p[i].position, p[i].velocity = p[i].position.reflect(p[i].velocity)

            s = utils.score(p[i].position)   
            if s < p[i].best_score:
                p[i].best_score = s
                p[i].best_position = deepcopy(p[i].position)  

        bs  = [p[i].best_score    for i in range(S)]
        bp  = [p[i].best_position for i in range(S)]
        gbs = min(bs)
        gbp = bp[bs.index(gbs)]

       #print(f"Iteration {iteration}: {gbs:.6e}, {gbp}")
        
        for i in range(S):
            r1 = [random.random(), random.random()]
            r2 = [random.random(), random.random()]

            #r1 = [random.random(), random.random(), random.random(), random.random()]
            #r2 = [random.random(), random.random(), random.random(), random.random()]

            p[i].velocity = (p[i].velocity.__scale__(w) 
                + (p[i].best_position - p[i].position).__mul__([c[0]*r1[0], c[0]*r1[1]]) 
                + (gbp - p[i].position).__mul__([c[1]*r2[0], c[1]*r2[1]]))
            
            #p[i].velocity = (p[i].velocity.__scale__(w) 
                #+ (p[i].best_position - p[i].position).__mul__([c[0]*r1[0], c[0]*r1[1], c[0]*r1[2], c[0]*r1[3]]) 
                #+ (gbp - p[i].position).__mul__([c[1]*r2[0], c[1]*r2[1], c[1]*r2[2], c[1]*r2[3]]))

    print(f"Best score:    {gbs}")
    print(f"Best position: {gbp}")
    print(f"\n")
    return (gbs, gbp)

if __name__ == '__main__':
    all_gbs = math.inf
    all_gbp = None
    for mat in mats.MATS:
        seed = 239
        random.seed(seed+random.randint(1,3))
        gbs, gbp = main(mat)  
        if gbs < all_gbs:
            all_gbs = gbs
            all_gbp = gbp
    print(f"ALL Best score:    {all_gbs}")
    print(f"ALL Best position: {all_gbp}")