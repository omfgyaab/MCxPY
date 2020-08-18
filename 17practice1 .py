# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:55:06 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
import random
while True:
    x,y,z=mc.player.getPos()
    color=random.randrange(0,9)
    mc.setBlock(x,y,z,38,color)
    time.sleep(1)