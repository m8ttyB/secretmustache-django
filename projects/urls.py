from django.urls import path
from .views import ProjectHomePageView, ProjectDetailView

urlpatterns = [
    path('', ProjectHomePageView.as_view(), name='project_index'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]