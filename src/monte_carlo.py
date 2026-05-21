from __future__ import annotations
import utils, consts, mats
import argparse
import math
import random
from copy import deepcopy

def main(mat: utils.Material):
    n = 500
    best_p = None
    min_s = math.inf
    pos = utils.Circ_Design(mat, random.uniform(consts.LIM[0], consts.LIM[1]), random.uniform(consts.LIM[0], consts.LIM[1]))
    #pos = utils.Rect_Design(mat, random.uniform(consts.LIM[0], consts.LIM[1]), random.uniform(consts.LIM[0], consts.LIM[1]), random.uniform(consts.LIM[0], consts.LIM[1]), random.uniform(consts.LIM[0], consts.LIM[1]))
    for i in range(n):
        vel = utils.Circ_Design(mat, random.uniform(consts.V_LIM[0], consts.V_LIM[1]), random.uniform(consts.V_LIM[0], consts.V_LIM[1]))* [random.choice([-1,1]), random.choice([-1,1])]
        #vel = utils.Rect_Design(mat, random.uniform(consts.V_LIM[0], consts.V_LIM[1]), random.uniform(consts.V_LIM[0], consts.V_LIM[1]), random.uniform(consts.V_LIM[0], consts.V_LIM[1]), random.uniform(consts.V_LIM[0], consts.V_LIM[1]))
        pos = pos.reflect(pos+vel)[0]
        score = utils.score(pos)
        if score < min_s:
            #print(f'New Found! {score}, {pos}')
            best_p = pos
            min_s = score
        if random.uniform(0,1) > 0.9:
            best_p = pos
            min_s = score
    #Save to list 
    return (min_s, best_p)

if __name__ == '__main__':
    #Compare n dimensional vector between each run 
    N = 300
    meta_bs = math.inf
    meta_bp = None
    all_gbs = math.inf
    all_gbp = None
    for i in range(N):
        seed = 10
        random.seed(seed+i)
        for mat in mats.MATS:
            gbs, gbp = main(mat)  
            if gbs < all_gbs:
                all_gbs = gbs
                all_gbp = gbp
        if all_gbs < meta_bs:
            meta_bs = all_gbs
            meta_bp = all_gbp
        print(f"best iter score:    {all_gbs}")
        print(f"best iter position: {all_gbp}")
        print(f"curr Best score:    {meta_bs}")
        print(f"curr Best position: {meta_bp}")
    print(f"ALL Best score:    {meta_bs}")
    print(f"ALL Best position: {meta_bp}")

