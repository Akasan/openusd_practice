from pxr import Usd, UsdGeom, Sdf, Gf

stage = Usd.Stage.CreateInMemory()

default_prim = UsdGeom.Xform.Define(
    stage,
    Sdf.Path("/World")).GetPrim()
UsdGeom.XformCommonAPI(default_prim).SetTranslate(Gf.Vec3d(1, 0, 0))
stage.SetDefaultPrim(default_prim)
usda = stage.GetRootLayer().ExportToString()
print(usda)
