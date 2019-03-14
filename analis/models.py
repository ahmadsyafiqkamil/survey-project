from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Proyek(models.Model):
    nama_proyek = models.CharField(max_length = 255)
    deskripsi_proyek = models.TextField()
    # id_perangkat = models.ForeignKey(Perangkat, on_delete=models.CASCADE)


class Organisasi(models.Model):
    nama_organisasi = models.CharField(max_length = 255)
    # id_proyek = models.ForeignKey(Proyek, on_delete=models.CASCADE)

class Perangkat(models.Model):
    survey = JSONField()
