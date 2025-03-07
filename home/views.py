from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from django.db.models import Q
from .forms import CommentForm
from django.contrib.auth.models import User
from .forms import PostForm

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
    

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'home/create_post.html', {'form': form})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True)
    comment_count = comments.count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.created_by = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(request, 'home/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form,
    })


def about(request):
    return render(request, 'about.html')

def profile_page(request):
    user = get_object_or_404(User, user=request.user)
    comments = user.commenter.all()


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.created_by != request.user:
        messages.error(request, 'You are not authorized to edit this comment.')
        return redirect('post_detail', slug=comment.post.slug)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully!')
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'home/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.created_by == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
    else:
        messages.error(request, 'You are not authorized to delete this comment.')
    return redirect('post_detail', slug=comment.post.slug)


