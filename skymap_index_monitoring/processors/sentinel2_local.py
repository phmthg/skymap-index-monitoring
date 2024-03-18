from rio_tiler.io.rasterio import Reader
from .imagery_statistics import *

EXPRESSION = {
    'NDVI': '(b4-b3)/(b4+b3)',
    'SAVI': '1.5*(b4-b3)/(b4+b3+0.5)',
    'RECI': 'where(b3 != 0, b4/b3-1, 0);',
    'GCI': 'where(b2 != 0, b4/b2-1, 0);',
    'EVI2': '2.5*(b4-b3)/(b4+2.4*b3+1)',
    'SIPI': 'where((b4-b3) != 0, (b4-b1)/(b4-b3), 0);',
    'NDWI': '(b2-b4)/(b2+b4)',
    'NDTI': 'where((b2-b4)/(b2+b4) >= -0.25, (b3-b2)/(b3+b2), 1.1);'
}


class Sentinel2Local(SatelliteImageryStatistics):
    def __init__(self, image_path: str, index, **kwargs):
        super().__init__(image_path, index, **kwargs)
        # with Reader(self.scene_id) as reader:
        #     self.reader = reader
        self.reader = Reader(self.scene_id)
        self.image_band = None
        self.image_mask = None
        self.mask = None

    def validate_index(self) -> bool:
        return self.index in EXPRESSION

    def get_expression(self) -> str:
        return EXPRESSION[self.index]

    def _read_image(self):
        _image_data = self.reader.read(expression=self.expression)
        self.image_band = _image_data.data
        self.image_mask = (self.image_band != 0) * 1
        self.mask = self.image_mask

    def get_info(self):
        self._read_image()
        self._calculate_area_of_index()
        _avg, _min, _max = self.calculate_index_stats()
        return {
            'statistics': self.statistics,
            'index_average': _avg,
            'index_min': _min,
            'index_max': _max
        }

    def get_download_file(self):
        return file_from_image_data(self.get_feature_data())

    @staticmethod
    def get_none_nodata_footprint(scene_id):
        pass

    @staticmethod
    def get_expression(index) -> str:
        return EXPRESSION[index]
