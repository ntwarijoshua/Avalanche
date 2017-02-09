from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Invitation(models.Model):
	tenant_name = models.CharField(max_length=100)
	tenant_domain = models.CharField(max_length=100)
	invitation_sent = models.BooleanField(default=False)
	invitation_expiration = models.DateField()
	invitation_token = models.CharField(max_length=100)
	invited_email = models.EmailField()
		