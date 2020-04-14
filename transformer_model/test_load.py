import os
import transformer_model
from django.contrib.gis.gdal import DataSource


def run():
    tr_shp = os.path.abspath(os.path.join(os.path.dirname(transformer_model.__file__),'data', 'DS_Transformer_C2_Pro.shp'))
    ds = DataSource(tr_shp)
    layer = ds[0]
    for feat in layer:
        print(feat.get('facilityid'), feat.geom)
