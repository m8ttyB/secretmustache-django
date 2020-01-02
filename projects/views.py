from django.views.generic import DetailView, ListView
from projects.models import Project


class ProjectHomePageView(ListView):
    context_object_name = 'projects'
    model = Project
    template_name = 'project_index.html'


class ProjectDetailView(DetailView):
    context_object_name = 'project'
    model = Project
    template_name = 'project_detail.html'
