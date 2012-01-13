from django.db import models

class Excuse(models.Model):
    excuse = models.TextField()

    def __unicode__(self):
        return self.excuse

