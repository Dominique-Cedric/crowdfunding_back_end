from django.urls import path
from . import views
from .views import PledgeList, ProjectList, ProjectDetail, PledgeDetail

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
    # path('projects/<int:project_id>/pledges/<int:pledge_id>/progress/', PledgeProgress.as_view(), name='pledge-progress'),
    # path('projects/check_pledge_progress', PledgeProgress.as_view()),

]

