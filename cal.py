import vector_cal as vc

v1 = vc.Vector2D(20,30,40)
v2 = vc.Vector2D(20,30,40)

# v1 == v2
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 == v2
print(v3)
print(v4)
print(v5)