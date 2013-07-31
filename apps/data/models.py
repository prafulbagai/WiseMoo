from django.db import models
from test.test_imageop import MAX_LEN
from django.db import models
from django.contrib.auth.models import  User
import os

# Create your models here.
def get_upload_path(instance, filename):
    return os.path.join('docs', instance.owner.username, filename)

class Document(models.Model):
    owner = models.ForeignKey(User)
    docfile = models.ImageField(upload_to=get_upload_path)
    
    
class WisemooUser(models.Model):
    name 	= models.CharField(max_length = 64)
    phone	= models.IntegerField()
    GENDER  = (
            	('m', 'Male'),
             	('f', 'Female'),
              )
    
    gender 	= models.CharField(max_length=1, choices=GENDER, default='m')
    user 	= models.ForeignKey(User)
    
    def __unicode__(self):
    	return u"%s" % (self.name)
