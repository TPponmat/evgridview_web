from django.contrib.gis.db import models


class Aoj_C2(models.Model):
    
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=14)
    workreques = models.CharField(max_length=20)
    designid = models.CharField(max_length=20)
    worklocati = models.CharField(max_length=20)
    area_code = models.CharField(max_length=2)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    
    def __str__(self):
        return self.name

