from django.db import models


# Create your models here.
class User(models.Model):
    DOCUMENT_TYPES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
        ('TI', 'Tarjeta de Identidad')
    ]

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    document_type = models.CharField(
        max_length=2,
        choices=DOCUMENT_TYPES,
        default='CC',
    )
    document = models.BigIntegerField(unique=True)
    city = models.CharField(max_length=50)
