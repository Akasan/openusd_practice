from pxr import Usd, UsdGeom

stage: Usd.Stage = Usd.Stage.CreateNew("./assets/create_prims.usda")

world: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")
sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world.GetPath().AppendPath("Sphere"))
box: UsdGeom.Cube = UsdGeom.Cube.Define(
    stage,
    world.GetPath().AppendPath("Backdrop")
)

stage.Save()
