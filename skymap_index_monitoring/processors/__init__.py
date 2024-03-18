from .sentinel2 import Sentinel2
from .sentinel1 import Sentinel1
from .planet import Planet8Bands

from .sentinel2 import EXPRESSION as SEN2_EXPRESSION
from .sentinel1 import EXPRESSION as SEN1_EXPRESSION
from .planet import EXPRESSION as PLANET_EXPRESSION


def get_image_processor(source):
    source = source.lower()
    if source == 'sentinel2':
        return Sentinel2
    if source == 'sentinel1':
        return Sentinel1
    if source == 'planet':
        return Planet8Bands
    if source == 'planetscope':
        return Planet8Bands

    raise Exception('No source found')


def get_expression(source: str, index: str, **kwargs) -> str:
    match source.lower():
        case 'sentinel2':
            return str(SEN2_EXPRESSION.get(index.upper()))
        case 'sentinel1':
            return str(SEN1_EXPRESSION.get(index.upper()))
        case 'planet':
            return str(PLANET_EXPRESSION.get(index.upper()))
        case 'planet8bandssr':
            return str(PLANET_EXPRESSION.get(index.upper()))
        case 'planetscope':
            return str(PLANET_EXPRESSION.get(index.upper()))
        case _:
            raise Exception("Invalid image source")
