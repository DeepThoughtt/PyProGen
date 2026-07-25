class Assets:

    def __init__(self):
        self.images = {}

    def load_assets(self, assets_dict):
        self.images = assets_dict["images"]

assets = Assets()
