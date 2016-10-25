from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField
from django.db.models.signals import pre_save
from django.utils import timezone
# Create your models here.
class Sponsor(models.Model):
        href = models.CharField(max_length=200, verbose_name="Link")
        start_date = models.DateTimeField(auto_now=False, auto_now_add=True)
        end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
        image = ImageField(upload_to='sponsors', verbose_name="Bilde")
        author = models.ForeignKey(User)

        def is_expired(self):
            if timezone.now() > self.end_date:
                return True
            return False
