from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from django.db.models import Q

class PostList(generic.ListView):
    template_name = "home/index.html"
    paginate_by = 6
    context_object_name = 'post_list'

    def get_queryset(self):
        queryset = Post.objects.filter(status=1)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(release_date__icontains=query) |
                Q(platform__icontains=query) |
                Q(genre__icontains=query)
            )
        return queryset

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(request, "home/post_detail.html", {"post": post})

def about(request):
    return render(request, 'about.html')