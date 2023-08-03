from django.db import models
from .userInfo import UserInfo

class TODO(models.Model):
    status_choice={
        ('C','completed'),
        ('P',"Pending")
    }
    priority_choice={
        ('1',"1st"),
        ('2',"2nd"),
        ('3',"3rd"),
        ('4',"4th"),
        ('5',"5th"),
        ('6',"6th"),
        ('7',"7th"),
        ('8',"8th"),
        ('9',"9th"),
        ('10',"10th"),
    }
    
    title=models.CharField(max_length=50)
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    date=models.DateField( auto_now_add=True)
    status=models.CharField(max_length=2,choices=status_choice)
    priority=models.CharField(max_length=20,choices=priority_choice)