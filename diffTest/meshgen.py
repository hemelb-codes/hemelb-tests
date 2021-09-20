import numpy as N
import vtk

# Layout of vertices
#
# -------in+n-1-------in+0-------in+1
#         /  \        /  \        / \
# \      /    \      /    \      /   \
#  \    /      \    /      \    /     \
#   \  /        \  /        \  /       \
#    \/          \/          \/         \
# (i-1)n+n-1--(i-1)n+0----(i-1)+1--------


r = 3.0
length = 110.0

n = 48

alpha = 2 * N.pi / n

side = 2 * r * N.sin(alpha / 2.0)
targetHeight = side * N.sin(N.pi / 3.0)

nRows = int(length / targetHeight)
height = length / nRows

zs = N.mgrid[-length / 2.0 : length / 2.0 : (nRows + 1) * 1j]
thetas = N.mgrid[0 : 2 * N.pi : alpha]

shift = 0

pd = vtk.vtkPolyData()
points = vtk.vtkPoints()
points.Allocate(len(zs) * len(thetas))
pd.SetPoints(points)

triangles = pd.GetPolys()

p = 0
for i, z in enumerate(zs):
    for j, theta in enumerate(thetas):
        assert (
            points.InsertNextPoint(
                r * N.cos(theta + shift), r * N.sin(theta + shift), z
            )
            == p
        )
        if i >= 1:
            if j > 0:
                triangles.InsertNextCell(3, (p, p - 1, p - n))
                pass
            if j < n - 1:
                triangles.InsertNextCell(3, (p, p - n, p - n + 1))
            else:
                triangles.InsertNextCell(3, (p, p - n, p - 2 * n + 1))
                triangles.InsertNextCell(3, (p, p - n + 1, p - 2 * n + 1))
                pass
            pass

        p += 1
        continue
    shift += alpha / 2.0
    continue

stl = vtk.vtkSTLWriter()
stl.SetFileName("cyl.stl")
stl.SetInputData(pd)
stl.Write()
