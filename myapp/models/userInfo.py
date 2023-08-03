from django.db import models

class UserInfo(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    # @staticmethod
    # def register(self):
    #     return self.save()
    
    def __str__(self):
        return f"{self.email}"
        # return super().__str__()
    def get_category_by_filter(email):
        return UserInfo.objects.filter(email=email)
    def is_exit(email):
        try:
            return UserInfo.objects.get(email=email)
        except:
            return "doex not exist"
        