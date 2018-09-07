from django.db import models

# Create your models here.
class Room(models.Model):
	# Creating Model Data
	name = models.CharField(max_length=30)
	status = models.BooleanField(default=True,null=True)

	class Meta:
		db_table = "room_room"