class Setting():
    def __init__(self,height = None, wide = None,bgc = None):
        self.height = height if height is not None else 800
        self.wide = wide if wide is not None else 1200
        self.bgc = bgc if bgc is not None else (230,230,230)
        self.Locations = [[0,0],[1060,0],[1060,660],[0,660]]