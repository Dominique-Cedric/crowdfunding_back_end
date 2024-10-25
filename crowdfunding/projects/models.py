# from django.db import models
# from django.contrib.auth import get_user_model
# from datetime import datetime, timedelta

# User = get_user_model()

# #define the project class
# class Project(models.Model):
#    title = models.CharField(max_length=200)
#    description = models.TextField()
#    goal = models.IntegerField()
#    image = models.URLField()
#    is_open = models.BooleanField()
#    date_created = models.DateTimeField(auto_now_add=True)
   
#    owner = models.ForeignKey(
#        User, on_delete=models.CASCADE, related_name='owned_projects')
 

# #define the pledges class
# class Pledge(models.Model):
#     amount = models.IntegerField()
#     comment = models.CharField(max_length=200)
#     anonymous = models.BooleanField()

#     project = models.ForeignKey(
#             User,
#             on_delete=models.CASCADE,
#             related_name='pledges'
#         )

 
#     supporter = models.ForeignKey(
#        User,
#        on_delete=models.CASCADE,
#        related_name='supporter'
#    )

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Define the Project class
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owned_projects'
    )

# Define the Pledge class
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()

    project = models.ForeignKey(
        Project,  # Change this to refer to the Project model
        on_delete=models.CASCADE,
        related_name='pledges'
    )

    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supporter'
    )

    def percentage_of_goal(self):
        if self.project.goal > 0:
            return (self.amount / self.project.goal) * 100
        return 0  # Avoid division by zero