from django.db import models

# Create your models here.

class Hit(models.Model):
    ip = models.IPAddressField()
    url = models.TextField()


    def __unicode__(self):
        return "IP: {0}, URL: {1}".format(self.ip, self.url)
