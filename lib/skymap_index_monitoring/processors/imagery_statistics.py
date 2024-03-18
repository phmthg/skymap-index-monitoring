from abc import ABC, abstractmethod
from typing import Optional
from shapely.geometry.base import BaseGeometry
from shapely.geometry import mapping
import numpy as np

from lib.skymap_index_monitoring.indices import index_statistics
from utils import *


class SatelliteImageryStatistics(ABC):
    def __init__(self, scene_id: str, index, cutline=Optional[BaseGeometry], **kwargs):
        self.get_expression: function = self.get_expression
        self.scene_id = scene_id
        self.index = index
        if not self.validate_index():
            raise Exception('Invalid index')
        if kwargs.get('custom_index_stats') is not None:
            statistics = [
                {'min_value': x['min_value'], 'color': x['color'], 'label': f"{x['name']} ({x['value']})"} for x in kwargs.get('custom_index_stats')
            ]
            self.statistics = sorted(statistics, key=lambda x: x['min_value'])
            print(self.statistics)
        else:
            self.statistics = index_statistics(index)
        self.expression = self.get_expression()
        if cutline:
            self.cutline = cutline

    @abstractmethod
    def validate_index(self) -> bool:
        pass

    @abstractmethod
    def get_expression(self) -> str:
        pass

    @abstractmethod
    def _read_image(self):
        pass

    @abstractmethod
    def get_cutline_info(self) -> dict:
        pass

    @abstractmethod
    def get_download_file(self):
        pass

    def _calculate_area_of_index(self):
        for j in range(0, len(self.statistics)):
            if j == len(self.statistics) - 1:
                logical_mask = (self.mask == 1) & \
                               (self.image_band >
                                self.statistics[j]['min_value'])
            else:
                logical_mask = (self.mask == 1) & \
                               (self.image_band > self.statistics[j]['min_value']) & \
                               (self.image_band <=
                                self.statistics[j + 1]['min_value'])

            result = np.count_nonzero(
                logical_mask * 1) / np.count_nonzero(self.image_mask)
            self.statistics[j]['area_percent'] = round(
                result, 4) if result >= 0.0001 else 0

    def calculate_index_stats(self):
        _average = np.average(self.image_band[self.mask == 1])
        _min = np.min(self.image_band[self.mask == 1])
        _max = np.max(self.image_band[self.mask == 1])
        return _average, _min, _max

    def get_feature_data(self):
        if isinstance(self.cutline, BaseGeometry):
            return self.reader.feature(expression=self.expression, shape=mapping(self.cutline),
                                       vrt_options={'CUTLINE_ALL_TOUCHED': True})
        return self.reader.read(expression=self.expression)

    @staticmethod
    @abstractmethod
    def get_none_nodata_footprint(scene_id) -> dict:
        pass
