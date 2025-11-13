from django.db import models

class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender_options = [('m','Male'),
                      ('f', 'female')]
    gender = models.CharField(max_length=1,choices=gender_options)

 # Instance method
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    
# class methods
@classmethod
def get_all_emails(cls):
    return cls.objects.values_list('email', flat=True) 
 
# static method
@staticmethod
def validate_email(email):
    return email.endswith('@gmail.com')    
