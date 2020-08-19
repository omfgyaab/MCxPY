# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:54:57 2020

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
        mc.postToChat(str(b))
        mc.setBlock(x,y,z,57)
                
        
    