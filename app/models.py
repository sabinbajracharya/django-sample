from django.db import models
from django.forms import ModelForm

# Create you models here
# https://docs.djangoproject.com/en/1.8/ref/models/fields/

class Artist(models.Model):
	def __unicode__(self):
		return 'Artist: ' + self.name
	# name = models.CharField(primary_key=True)
	# custom_id = models.IntField(primary_key=True)
	# custom_id = models.Autofield(primary_key=True) # Auto Generated integer

	name = models.CharField("artist", max_length=50) # "artist" is verbose_name property | 'a' of artist is automatically capitalized
	year_formed = models.PositiveIntegerField() # Underscore has special meaning! When generating label for auto generated form the underscore is replaced by space and first letter of the frist world is capitalize

class Album(models.Model):
	def __unicode__(self):
		return "Album: " + self.name  

	name = models.CharField(max_length=50)
	artist = models.ForeignKey(Artist); # Artist primary key is the Album foreign key

class ArtistForm(ModelForm):
	class Meta :
		model = Artist
		fields = ['name', 'year_formed']
