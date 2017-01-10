# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-01-09T22:35:30+05:30
# @Email:  tamyworld@gmail.com
# @Filename: admin.py
# @Last modified by:   tushar
# @Last modified time: 2017-01-10T13:09:08+05:30



from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Task)
