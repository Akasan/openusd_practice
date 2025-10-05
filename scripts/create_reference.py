from pxr import Usd, UsdGeom, Gf

stage = Usd.Stage.CreateNew("./assets/cube_for_ref.usda")
cube = UsdGeom.Cube.Define(stage, "/Cube")
stage.SetDefaultPrim(cube.GetPrim())
stage.Save()

stage = Usd.Stage.CreateNew("./assets/create_reference.usda")
world = UsdGeom.Xform.Define(stage, "/World")
UsdGeom.Sphere.Define(
    stage,
    world.GetPath().AppendPath("Sphere"),
)

reference_prim = stage.DefinePrim(
    world.GetPath().AppendPath("Cube_Ref")
)
reference_prim.GetReferences().AddReference("./cube_for_ref.usda")
UsdGeom.XformCommonAPI(reference_prim).SetTranslate(Gf.Vec3d(5, 0, 0))
stage.Save()
