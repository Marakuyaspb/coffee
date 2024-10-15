from django.db import models

class CallMe(models.Model):
	id = models.AutoField(primary_key=True, verbose_name='Имя')
	first_name = models.CharField(max_length=30)
	phone = models.CharField(max_length=15)
	message = models.TextField(max_length=900, null=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']
	def __str__(self):
		return self.first_name