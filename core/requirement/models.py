from core.schools.models import School
from django.db import models
from autoslug import AutoSlugField


class Requirements(models.Model):
    PROGRAM_TYPES = (
        ("Undergrad", "Undergraduate Degree"),
        ("Postgrad", "Postgraduate Degree"),
        ("Doctorate", "Doctorate Degree"),
    )
   
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', blank=True, editable=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="requirements")
    program = models.CharField(max_length=200, choices=PROGRAM_TYPES)
    description = models.TextField(max_length=5000)    

    def __str__(self):
        return self.title   