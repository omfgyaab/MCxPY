# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:45:34 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
mc.player.setTilePos(-340,130,41)
mc.executeCommand("give APE_18 minecraft:diamond_sword")
#mc.player.setTilePos(-340,69,41)
x,y,z=mc.player.getTilePos()
def plantTree(x,y,z):
    mc.setBlocks(x,y+3,z-3,x+2,y+5,z-1,18)
    mc.setBlocks(x+1,y-1,z-2,x+1,y+3,z-2,17)
for i in range(0,25,5):
    plantTree(x+i,y,z)
    plantTree(x+i,y,z+4)
for i in range(0,20,1):
    mc.setBlocks(x,y-1,z-1,x+24,y-1,z+1,46)
while True:
    x,y1,z1=mc.player.getTilePos()
    if x>-320:
        mc.postToChat('歡迎來到體溫檢測站,請輸入你的體溫')
        mc.postToChat('白色羊毛:36.5')
        mc.postToChat('橘色羊毛:37')
        mc.postToChat('紫色羊毛:37.5')
        mc.postToChat('藍色羊毛:38')
        mc.postToChat('黃色羊毛:38.5')
        break
for i in range(0,5,1):    
    mc.setBlocks(x+2,y-1,z+i-2,x+3,y-1,z+i-2,35,0+i)
while True:
    a=mc.events.pollBlockHits()
    if len(a) > 0:
        hit=a[0]
        xx=hit.pos.x
        yy=hit.pos.y
        zz=hit.pos.z
        ii=mc.getBlockWithData(xx,yy,zz)
        jj=ii.data
        kk=ii.id
        if kk==35:
            if jj>2:
                mc.postToChat('你已發燒,請到隔離所進行隔離')
                mc.setTilePos(-457,4,-1338)
                break
            else:
                mc.postToChat('恭喜你沒發燒')
                break
    
        
    
   