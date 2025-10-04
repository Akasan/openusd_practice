from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("./assets/create_xform.usda")

xform = UsdGeom.Xform.Define(stage, "/World")
xform_api = UsdGeom.XformCommonAPI(xform)
xform_api.SetRotate((45, 45, 45))
cone = UsdGeom.Cone.Define(stage, xform.GetPath().AppendPath("Cone"))
box = UsdGeom.Cube.Define(stage, xform.GetPath().AppendPath("Cube"))
# cone = UsdGeom.Cone.Define(stage, "/Cone")
# box = UsdGeom.Cube.Define(stage, "/Cube")
# 
# cone.GetDisplayColorAttr().Set([(1.0, 0.5, 0.25)])
cone_xform_api = UsdGeom.XformCommonAPI(cone)
# cone_xform_api.SetScale((0.5, 0.5, 1.5))
cone_xform_api.SetTranslate((0.0, 1.5, 0.0))
# cone_xform_api.SetRotate((45, 167, -29))
stage.Save()
