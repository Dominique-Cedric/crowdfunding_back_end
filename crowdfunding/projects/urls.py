from django.urls import path
from . import views
from .views import PledgeList, ProjectList, ProjectDetail

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
    path('pledges/<int:pk>/like/', views.Liked.as_view()),
]


#allows URL patterns to accept different formats based on the request
urlpatterns = format_suffix_patterns(urlpatterns)