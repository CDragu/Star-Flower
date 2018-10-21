import maya.cmds as cmds
import math
import random

import numpy

from numpy import linalg as LA



random.seed( 1234 )


cubeList = cmds.ls( 'myCube*' )
if len( cubeList ) > 0:
    cmds.delete( cubeList )


day = 100

e=0.0167

ra = 147098291

rp = 152098233

r = 10000000

sun = cmds.polySphere(r=1, sx=20, sy=20, ax=(0, 1, 0), cuv=2, ch=1, name = "myCube#")

earth = cmds.polySphere(r = 0.1, sx = 20, sy = 20, ax = (10, 1, 10), cuv = 2, ch =1, name = "myCube#")

for i in range(1, 366):
    j = i/58.12#represents 366 divided by 2 pi
    earthInPos = cmds.duplicate(earth)
    
    ex = math.sin(j) * (ra/r)
    ey = 0
    ez  = math.cos(j) * (rp/r)
    
    cmds.move(ex, ey, ez , earthInPos)
    point = cmds.duplicate(earthInPos)
    
    cmds.scale(0.1, 0.1, 0.1, point)
    
    px = ex - math.sin(j)        * 0.1
    py = ey                      * 0.1
    pz = ez - math.cos(j)        * 0.1
    
    pointNormal = cmds.duplicate(point)
    cmds.move(ex - math.sin(j) * 0.2,ey * 0.2, ez - math.cos(j) * 0.2, pointNormal)
    
    cmds.move(px ,py, pz, point)
    
    vex = -(ex - px)
    vey = -(ey - py)
    vez = -(ez - pz)
    
    vectorearth = cmds.duplicate(earth)
    
    cmds.move(vex * 10, vey * 10, vez * 10, vectorearth)
    #cmds.rotate( 0, '0deg', 0, vectorearth, pivot=(1, 0, 0) )
    #cmds.viewLookAt( vectorearth, pos=(3.0, 1.0, 0.0) )
    #con = cmds.aimConstraint( pointNormal, point, aimVector=[0,0,1] )
    #cmds.delete(con)
    
    vsx = ex
    vsy = ey
    vsz = ez
    
    vs = (vsx, vsy, vsz)
    ve = (vex, vey, vez)
    
    #print vs
    
    vs = vs / LA.norm(vs)
    ve = ve / LA.norm(ve)
    
    #print vs
   
    #for X
    
    vsx = (vs[0], 0, 0)
    vex = (ve[0], 0, 0)
    
    dotx =  numpy.linalg.multi_dot([vsx,vex])
    
    print numpy.arccos(dotx)* 57.2958
    
    #for Y
    
    vsy = (0, vs[1], 0)
    vey = (0, ve[1], 0)
    
    doty =  numpy.linalg.multi_dot([vsy,vey])
    
    print numpy.arccos(doty) * 57.2958
    
    #for Z
    
    vsz = (0, 0, vs[2])
    vez = (0, 0, ve[2])
    
    dotz =  numpy.linalg.multi_dot([vsz,vez])
    
    print numpy.arccos(dotz)* 57.2958
         
cmds.delete(earth)

#cmds.move(math.sin(day) * 2, 0, math.cos(day) * 2, earth)

#e = earth
#p = point on earth
#ve = vector from center of earth to point on earth
#vs = vector from sun to earth(sun is at 000)

