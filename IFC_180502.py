import ifcopenshell

file = ifcopenshell.open("180502.ifc")

project = file.by_type("IfcProject")[0]
print(project)

# IFCRelSpaceBoundary
boundary = file.by_type("IFCRelSpaceBoundary")
print(boundary)
for i in range(len(boundary)):
    print(boundary[i])

# IFCRelationship
relation = file.by_type("IFCRelationship")
print(relation)
for i in range(len(relation)):
    print(relation[i])

# IFCR한글로하면?
