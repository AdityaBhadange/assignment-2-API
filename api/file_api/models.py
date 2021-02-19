from django.db import models

class File(models.Model):
	upload = models.FileField(upload_to='uploads/')