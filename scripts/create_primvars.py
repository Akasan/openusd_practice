from pxr import Usd, UsdGeom, Sdf, Gf

stage = Usd.Stage.CreateNew("assets/create_primvars.usda")
world = UsdGeom.Xform.Define(stage, "/World")
cube = UsdGeom.Cube.Define(
    stage,
    world.GetPath().AppendPath("Cube")
)
cube_prim = cube.GetPrim()
primvar_api = UsdGeom.PrimvarsAPI(cube_prim)
primvar_api.CreatePrimvar(
    "displayColor", 
    Sdf.ValueTypeNames.Color3fArray
)
primvar = primvar_api.GetPrimvar("displayColor")
primvar.Set([Gf.Vec3f(0.0, 1.0, 0.0)])
values = primvar.Get()
print(values)
stage.Save()
