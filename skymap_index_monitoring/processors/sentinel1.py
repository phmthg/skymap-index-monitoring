from .imagery_statistics import SatelliteImageryStatistics
from .imagery_statistics import *
from skymap_index_monitoring.image_readers.sentinel1 import S1L1CReader
from skymap_index_monitoring.utils.tile_helper import crop_tile
# from typing import Optional


EXPRESSION = {
    'NDVI': '(b8-b6)/(b8+b6)',
    'SAVI': '1.5*(b8-b6)/(b8+b6+0.5)',
    'RECI': 'where(b6 != 0, b8/b6-1, 0);',
    'GCI': 'where(b4 != 0, b8/b4-1, 0);',
    'EVI2': '2.5*(b8-b6)/(b8+2.4*b6+1)',
    'SIPI': 'where((b8-b6) != 0, (b8-b2)/(b8-b6), 0);',
    'NDRE': '(b8-b7)/(b8+b7)',
    'NDRVI': '2*(vh-vv)/(vh+vv)',
    'RI': 'where(vv != 0, vh/vv, 0);',
    'RVI': '4*vh/(vh+vv)',
    'RVI4S1': 'sqrt(vv/(vv+vh))*4*vh/(vh+vv)',
}


class Sentinel1(SatelliteImageryStatistics):
    def __init__(self, scene_id: str, index, cutline: BaseGeometry):
        super().__init__(scene_id, index, cutline)
        with S1L1CReader(self.scene_id) as reader:
            self.reader = reader
        self.image_band = None
        self.image_mask = None
        self.mask = None

    def validate_index(self) -> bool:
        return self.index in EXPRESSION

    def get_expression(self) -> str:
        return EXPRESSION[self.index]

    def get_cutline_info(self) -> dict:
        self._read_image()
        cloud_cover = -1
        self._calculate_area_of_index()
        _avg, _min, _max = self.calculate_index_stats()
        return {
            'field_cloud_cover': cloud_cover,
            'statistics': self.statistics,
            'index_average': _avg,
            'index_min': _min,
            'index_max': _max
        }

    def _read_image(self):
        _image_data = self.reader.part(
            bbox=self.cutline.bounds, height=512, width=512, expression=self.expression)
        self.image_band = crop_tile(_image_data, geometry=self.cutline)[0]
        self.image_mask = (self.image_band != 0) * 1
        self.mask = self.image_mask

    def get_download_file(self):
        return file_from_image_data(self.get_feature_data())

    @staticmethod
    def get_none_nodata_footprint(scene_id):
        pass
