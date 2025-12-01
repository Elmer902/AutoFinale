from django.db import models

from django.db import models
from django.core.validators import MinLengthValidator
class Messages(models.Model):
    message_read = "r"
    message_unread = "u"
    message_variables  = [(message_read, "Read"),(message_unread,"Unread")]

    username = models.CharField(max_length=255, validators=[MinLengthValidator(4)])
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    message_status = models.CharField(max_length=10,choices=message_variables, default=message_unread)
    class Meta:
        ordering = ['username']

class BlogPost(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='photo/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    
    
    
    
class Drivers_License(models.Model):
    title = models.CharField(max_length=25)
    main_image = models.ImageField(upload_to='photo/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    
    
    
    def __str__(self):
        return self.title
    
class License_Category(models.Model):
    title = models.CharField(max_length=40)
    short_description = models.TextField()
    detailed_description = models.TextField()
    license = models.ForeignKey(Drivers_License, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class detailed_List(models.Model):
    title = models.TextField()
    license = models.ForeignKey(Drivers_License,on_delete=models.CASCADE)
    license_category = models.ForeignKey(License_Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    