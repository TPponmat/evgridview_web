from django.shortcuts import render
from .models import Aoj_C2
from transformer_model.models import Transformer_C2

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.core.serializers import serialize
from django.contrib.gis.db.models.functions import AsGeoJSON, Centroid

from django.contrib.gis.gdal import DataSource
import transformer_model
import os

@csrf_exempt
def select_aoj_request(request):
    aoj_code = json.loads(request.GET["code"])
    
    tr_c2 = os.path.abspath(os.path.join(os.path.dirname(transformer_model.__file__), 'data','DS_Transformer_C2_Pro.shp'))
    
    aoj = Aoj_C2.objects.all().filter(code=aoj_code)
    aoj_poly = aoj[0].geom
    print(type(aoj_poly))
    
    tr = Transformer_C2.objects.all().filter(geom__within = aoj_poly)
    print(len(tr))
    
    qs = Aoj_C2.objects.all().filter(code=aoj_code).annotate(cent=AsGeoJSON(Centroid('geom')))
    for i in qs.values():
        print(json.loads(i.get("cent")).get("coordinates"))
        centroid_aoj = json.loads(i.get("cent")).get("coordinates")
    
    res = serialize(
        'geojson',
        Aoj_C2.objects.all().filter(code=aoj_code),
        fields=('geom', ),
    )
    
    result = []
    result_dict = {}
    for i in tr :
        # point_tr.append(i.geom.geojson)
        # pea_no.append(i.facilityid)
        # print(type(i.geom.json))
        json_obj = json.loads(i.geom.json)
        result_dict.update({"peano": i.facilityid, "ratekva": i.ratekva, 
                            "gistag" : i.tag, "feederID": i.feederid, "phase" : i.phasedesig,
                            "name" : i.name, "flag" : i.flag,
                            "impact" : i.impact, "baseload" : i.loadProfile_base,
                            "evload" : i.loadProfile_ev, "coordinate": json_obj["coordinates"]})
        
        result.append(result_dict)
        result_dict = {}
    
    print(result)   
    return JsonResponse({"data": res, "coordinate_cent" : centroid_aoj, \
                            "point": json.dumps(result)})