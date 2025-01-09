from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("created_on")
    template_name = "gamecrit_post/index.html"
    paginate_by = 4

def display_game_review(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    gamecrit_post = get_object_or_404(queryset, slug=slug)
    comments = gamecrit_post.comments.all().order_by("-created_on")
    comment_count = gamecrit_post.comments.filter(approved=True).count()

    return render(
        request,
        "gamecrit_post/display_game_review.html",
        {"gamecrit_post": gamecrit_post,
        "comments": comments,
        "comment_count": comment_count,
        },
    )