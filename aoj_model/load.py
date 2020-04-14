import os
from django.contrib.gis.utils import LayerMapping
from .models import Aoj_C2

aoj_c2_mapping = {
    'name': 'NAME',
    'code': 'CODE',
    'workreques': 'WORKREQUES',
    'designid': 'DESIGNID',
    'worklocati': 'WORKLOCATI',
    'area_code': 'AREA_CODE',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'geom': 'MULTIPOLYGON',
}

aoj_c2_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                        'data','AOJ_C2.shp'))
print(aoj_c2_shp)

def run(verbose=True):
    lm = LayerMapping(Aoj_C2, aoj_c2_shp, aoj_c2_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)