import numpy as N
# Layout of vertices
# 
# -------in+n-1-------in+0-------in+1
#         /  \        /  \        / \
# \      /    \      /    \      /   \
#  \    /      \    /      \    /     \
#   \  /        \  /        \  /       \
#    \/          \/          \/         \
# (i-1)n+n-1--(i-1)n+0----(i-1)+1--------


r = 3.
length = 110.

n = 48

alpha = 2*N.pi/n

side = 2 * r * N.sin(alpha/2.)
targetHeight = side*N.sin(N.pi/3.)

nRows = int(length/targetHeight)
height = length/nRows

zs = N.mgrid[-length/2.:length/2.:(nRows+1)*1j]
thetas = N.mgrid[0:2*N.pi:alpha]

shift = 0
points = N.zeros((len(zs)*len(thetas), 3))
triangles = []
p = 0
for i, z in enumerate(zs):
    for j, theta in enumerate(thetas):
        points[p, 0] = r*N.cos(theta+shift)
        points[p, 1] = r*N.sin(theta+shift)
        points[p, 2] = z
        if i >= 1:
            if j>0:
                triangles.append( (p, p-1, p-n) )
                pass
            if j < n-1:
                triangles.append( (p, p-n, p-n+1) )
            else:
                triangles.append( (p, p-n, p-2*n+1) )
                triangles.append( (p, p-n+1, p-2*n+1) )
                pass
            pass
        
        p += 1
        continue
    shift += alpha/2.
    continue

triangles = N.array(triangles)

from enthought.tvtk.api import tvtk as vtk
pd = vtk.PolyData()
pd.points = points
pd.polys = triangles

stl = vtk.STLWriter()
stl.file_name = 'cyl.stl'
stl.input = pd
stl.write()
