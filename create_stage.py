from pxr import Usd

stage: Usd.Stage = Usd.Stage.CreateNew("./assets/stage.usda")
stage.Save()
