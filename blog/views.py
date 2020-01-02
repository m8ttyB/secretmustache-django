from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from blog.forms import CommentForm
from blog.models import Post, Comment


class BlogIndexPageView(ListView):
    context_object_name = 'posts'
    template_name = 'blog_index.html'

    def get_queryset(self):
        """
        Return posts in descending order, most recent first
        """
        return Post.objects.all().order_by("-created_on")


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog_detail.html", context)
