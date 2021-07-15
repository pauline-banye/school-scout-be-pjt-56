from django.db import models
from autoslug import AutoSlugField
from core.schools.models import School



"""SCHOOL NEWS MODEL""" 
class News(models.Model): # Create school news articles

    
    title = models.CharField(max_length=150, help_text='Enter title', blank=False, unique=True)
    slug = AutoSlugField(populate_from='title', blank=True, editable=True)
    category = models.CharField(max_length=150, help_text='Enter Name of category', blank=False, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="news")
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    info = models.TextField()
    snippet = models.CharField(max_length=250)
    date = models.DateField()
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "{}".format(self.title)

