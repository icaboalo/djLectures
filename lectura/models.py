from django.db import models

# Create your models here.
class Calendar(models.Model):

    class Meta:
        verbose_name = "Calendar"
        verbose_name_plural = "Calendars"

    #Attributes
    date = models.DateField(auto_now=False)

    def __str__(self):
    	return str(self.date)
    
class Lecture(models.Model):

    class Meta:
        verbose_name = "Lecture"
        verbose_name_plural = "Lectures"

    #Relations
    date = models.OneToOneField(Calendar, related_name='lectures', unique=True)

    #Attributes
    type = models.CharField(max_length = 50, blank=False)
    lecture = models.TextField(max_length=10000, blank=False)


    def __str__(self):
    	return self.type
    