from pxr import Usd, Sdf, UsdGeom

def add_payload(prim: Usd.Prim, payload_asset_path: str, payload_target_path: Sdf.Path) -> None:
    payloads: Usd.Payloads = prim.GetPayloads()
    payloads.AddPayload(
        assetPath=payload_asset_path,
        primPath=payload_target_path
    )


stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

payload_prim: Usd.Prim = UsdGeom.Xform.Define(
    stage,
    Sdf.Path("/World/payload")
).GetPrim()

add_payload(payload_prim, "./assets/new_stage.usda", Sdf.Path("/World/some/target"))

usda = stage.GetRootLayer().ExportToString()
print(usda)
