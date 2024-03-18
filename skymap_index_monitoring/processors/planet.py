from .imagery_statistics import SatelliteImageryStatistics

EXPRESSION = {
    'NDVI': '(b8-b6)/(b8+b6)',
    'SAVI': '1.5*(b8-b6)/(b8+b6+0.5)',
    'RECI': 'where(b6 != 0, b8/b6-1, 0);',
    'GCI': 'where(b4 != 0, b8/b4-1, 0);',
    'EVI2': '2.5*(b8-b6)/(b8+2.4*b6+1)',
    'SIPI': 'where((b8-b6) != 0, (b8-b2)/(b8-b6), 0);',
    'NDRE': '(b8-b7)/(b8+b7)',
}


class Planet8Bands(SatelliteImageryStatistics):
    def __init__(self, scene_id: str, index, **kwargs):
        super().__init__(scene_id, index, **kwargs)
        # self.reader = Reader(self.scene_id)
        self.image_band = None
        self.image_mask = None
        self.mask = None

    def validate_index(self) -> bool:
        return self.index in EXPRESSION

    def get_expression(index) -> str:
        return EXPRESSION[index]

    def get_cutline_info(self):
        pass

    def _read_image(self):
        pass

    def get_download_file(self):
        pass

    @staticmethod
    def get_none_nodata_footprint(scene_id):
        pass
