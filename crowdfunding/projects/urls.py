from django.urls import path
from . import views
from .views import PledgeList, ProjectList, ProjectDetail

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view())
]