# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:51:32 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    a=mc.events.pollBlockHits()
    if len(a)>0:
        hit=a[0]
        x=hit.pos.x
        y=hit.pos.y
        z=hit.pos.z
        b=mc.getBlock(x,y,z)
        mc.createExplotion