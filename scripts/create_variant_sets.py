from pxr import Usd, UsdGeom, Gf

stage = Usd.Stage.CreateNew("./assets/create_variant_prims.usda")
world = UsdGeom.Xform.Define(stage, "/World")
stage.SetDefaultPrim(world.GetPrim())

box = UsdGeom.Xform.Define(
    stage,
    world.GetPath().AppendPath("Box")
)
geo_scope = UsdGeom.Scope.Define(
    stage,
    box.GetPath().AppendPath("Geometry")
)

geo_variant_sets = geo_scope.GetPrim().GetVariantSets()
shapes_variant_set = geo_variant_sets.AddVariantSet("shapes")
shapes_variant_set.AddVariant("Cube")
shapes_variant_set.AddVariant("Sphere")

shapes_variant_set.SetVariantSelection("Cube")

with shapes_variant_set.GetVariantEditContext():
    cube = UsdGeom.Cube.Define(
        stage,
        geo_scope.GetPath().AppendPath("Cube")
    )
    cube_prim = cube.GetPrim()
    UsdGeom.XformCommonAPI(cube_prim).SetTranslate(
        Gf.Vec3d(1, 0, 0)
    )
    cube_prim.SetTypeName("Cube")


shapes_variant_set.SetVariantSelection("Sphere")

with shapes_variant_set.GetVariantEditContext():
    sphere = UsdGeom.Sphere.Define(
        stage,
        geo_scope.GetPath().AppendPath("Sphere")
    )
    sphere_prim = sphere.GetPrim()
    UsdGeom.XformCommonAPI(sphere_prim).SetTranslate(
        Gf.Vec3d(0, 1, 0)
    )
    sphere_prim.SetTypeName("Sphere")

shapes_variant_set.SetVariantSelection("Cube")
stage.Save()
