from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
        return self.name
class Designation(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
            return self.name
class AvailableTime(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
class Doctor(models.Model):
    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True, blank=True)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='upload/', null=True, blank=True)  
    designation = models.ManyToManyField(Designation)
    specialization =  models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.name}"


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)

    def __str__(self):
        return f"Patient : {self.reviewer.first_name} ; Doctor {self.doctor.user.first_name}"
    





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_appointment = models.ManyToManyField(Doctor)

    def __str__(self):
        return self.user.username  