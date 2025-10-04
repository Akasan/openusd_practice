from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("./assets/create_scope.usda")

world = UsdGeom.Xform.Define(stage, "/World")
stage.SetDefaultPrim(world.GetPrim())

geo_scope = UsdGeom.Scope.Define(
    stage,
    world.GetPath().AppendPath("Geometry")
)

box_geo = UsdGeom.Cube.Define(
    stage,
    geo_scope.GetPath().AppendPath("Cube")
)

stage.Save()
