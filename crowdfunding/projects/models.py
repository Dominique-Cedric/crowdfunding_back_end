from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField()
   goal = models.IntegerField()
   image = models.URLField()
   supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pledges'
    )
   
   #define the project type
   Project_type = (
       ('donations', 'DONATIONS'),  # Retained donations option only
    )
   
   #describe certain attributes of the model
   cause = models.CharField(choices=Project_type, max_length=20, default="DONATIONS")  # Default updated to donations
   
   #tracks which users have liked the project
   liked_by = models.ManyToManyField(
        User,
        related_name='liked_projects'
    )
   
   #return human-readable format
   def __str__(self):
        return f"{self.cause} Project"   
   
   is_open = models.BooleanField()
   date_created = models.DateTimeField(auto_now_add=True)
   owner = models.ForeignKey(
       get_user_model(),
       on_delete=models.CASCADE,
       related_name='owned_projects'
   )
   
   #access the total number of likes for a project instance
   @property
   def total_likes(self):
    return self.liked_by.aggregate(count=models.Count('id'))['count']

#define the pledges
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
       get_user_model(),
       on_delete=models.CASCADE,
       related_name='pledges'
   )


