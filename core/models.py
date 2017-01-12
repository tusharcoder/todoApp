# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-01-09T22:35:30+05:30
# @Email:  tamyworld@gmail.com
# @Filename: models.py
# @Last modified by:   tushar
# @Last modified time: 2017-01-12T15:27:34+05:30



from django.db import models

# Create your models here
class Task(models.Model):
    """Class for the model task"""
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    priority = models.PositiveIntegerField()
    def __unicode__(self):
        return self.title
