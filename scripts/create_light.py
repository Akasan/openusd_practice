from pxr import Usd, UsdGeom, UsdLux, UsdShade, Gf

stage = Usd.Stage.CreateNew("./assets/create_light.usda")

world = UsdGeom.Xform.Define(stage, "/World")
geo_scope = UsdGeom.Scope.Define(
    stage,
    world.GetPath().AppendPath("Geometry")
)
box_geo = UsdGeom.Cube.Define(
    stage,
    geo_scope.GetPath().AppendPath("Cube")
)

light_scope = UsdGeom.Scope.Define(
    stage,
    world.GetPath().AppendPath("Lights")
)

distant_light = UsdLux.DistantLight.Define(
    stage,
    light_scope.GetPath().AppendPath("Sun")
)
sphere_light = UsdLux.SphereLight.Define(
    stage,
    light_scope.GetPath().AppendPath("ShpereLight")
)

distant_light.GetColorAttr().Set(
    Gf.Vec3f(1.0, 0.0, 0.0)
)
distant_light.GetIntensityAttr().Set(12.0)

if not (xform_api := UsdGeom.XformCommonAPI(distant_light)):
    raise Exception("Prim not compatible with XformCommonAPI")

xform_api.SetRotate((45.0, 0.0, 0.0))
xform_api.SetTranslate((-5.0, -10.0, 0.0))
xform_api = None

sphere_light.GetColorAttr().Set(Gf.Vec3f(0.0, 0.0, 1.0))
sphere_light.GetIntensityAttr().Set(50.0)

if not (xform_api := UsdGeom.XformCommonAPI(sphere_light)):
    raise Exception("Prim not compatible with XformCommonAPI")

xform_api.SetTranslate((5.0, 10.0, 0.0))

stage.Save()
