from pxr import UsdGeom, Usd, UsdLux, UsdPhysics, Gf

stage = Usd.Stage.CreateNew("./assets/schema.usda")
sphere = UsdGeom.Sphere.Define(stage, "/World/Sphere")
sphere.GetRadiusAttr().Set(10)

disk_light = UsdLux.DiskLight.Define(stage, "/World/Lights/DiskLight")
dl_attribute_name = disk_light.GetSchemaAttributeNames()
disk_light.GetIntensityAttr().Set(1_000)

cube = UsdGeom.Cube.Define(stage, "/World/Cube")
cube_rb_api = UsdPhysics.RigidBodyAPI.Apply(cube.GetPrim())
a = cube_rb_api.GetKinematicEnabledAttr()
cube_rb_api.CreateVelocityAttr(Gf.Vec3f(5.0, 5.0, 5.0))
stage.Save()
