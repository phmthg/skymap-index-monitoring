from .imagery_statistics import *
from shapely.geometry import Polygon
from rio_tiler.io import COGReader
from utils.tile_helper import crop_tile
import numpy as np
from lib.skymap_index_monitoring.image_readers.sentinel2 import S2COGReader


EXPRESSION = {
    'NDVI': '(B08-B04)/(B08+B04)',
    'SAVI': '1.5*(B08-B04)/(B08+B04+0.5)',
    'RECI': 'where(B04 != 0, B08/B04-1, 0);',
    'GCI': 'where(B03 != 0, B08/B03-1, 0);',
    'EVI2': '2.5*(B08-B04)/(B08+2.4*B04+1)',
    'SIPI': 'where((B08-B04) != 0, (B08-B02)/(B08-B04), 0);',
    'NDRE': '(B08-B05)/(B08+B05)',
    'NDMI': '(B08-B11)/(B08+B11)',
    'NDBI': '(B11-B08)/(B11+B08)',
    'NDCI': '(B05-B04)/(B05+B04)',
    'NDESI': '(B04-B02)/(B04+B02) + (B07-B06)/(B07+B06)',
    'NSI': '(B03+B04)/(log(B11))',
    'CMI': 'B11/B12',
    'FMI': 'B11/B08',
    'FFI': '(B12/B08)+(B03/B04)'
}


class Sentinel2(SatelliteImageryStatistics):

    def __init__(self, scene_id: str, index, cutline: BaseGeometry):
        super().__init__(scene_id, index, cutline)
        with S2COGReader(self.scene_id) as reader:
            self.reader = reader
        self.image_band = None
        self.image_mask = None
        self.cloud_mask = None
        self.mask = None

    def validate_index(self) -> bool:
        return self.index in EXPRESSION

    def get_expression(self) -> str:
        return EXPRESSION[self.index]

    def get_cutline_info(self):
        self._read_image()
        cloud_cover = self.calculate_cloud_cover()
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
        if not geometry_contains(Polygon([tuple(l) for l in self.reader.stac_item['geometry']['coordinates'][0]]),
                                 self.cutline):
            raise Exception('The image doesnt contain the cutline')

        _image_data = self.reader.part(
            bbox=self.cutline.bounds, height=512, width=512, expression=self.expression)
        self.image_band = crop_tile(_image_data, geometry=self.cutline)[0]
        self.image_mask = (self.image_band != 0) * 1

        with COGReader(self.reader._get_band_url("B01").replace("B01", "SCL")) as cog:
            _scl_data = cog.part(bbox=self.cutline.bounds,
                                 height=512, width=512)
            scl_band = crop_tile(_scl_data, geometry=self.cutline)[0]
            self.cloud_mask = (np.logical_or(scl_band == 8, scl_band == 9)) * 1

        self.mask = ((self.image_mask == 1) & (self.cloud_mask == 0)) * 1

    def calculate_cloud_cover(self):
        no_pixel_farm = np.count_nonzero(self.image_mask)
        no_pixel_covered_by_cloud = np.count_nonzero(self.cloud_mask)
        cloud_cover = no_pixel_covered_by_cloud / no_pixel_farm

        if cloud_cover >= 1:
            raise Exception('100% covered by cloud')

        return cloud_cover

    def get_download_file(self):
        return file_from_image_data(self.get_feature_data())

    @staticmethod
    def get_none_nodata_footprint(scene_id):
        pass
