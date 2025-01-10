from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import GameCritCommentForm

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

    if request.method == "POST":
        comment_form = GameCritCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.username = request.user
            comment.post_id = gamecrit_post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for the comment. It is now in queue to be approved!'
    )

    comment_form = GameCritCommentForm()

    return render(
        request,
        "gamecrit_post/display_game_review.html",
        {"gamecrit_post": gamecrit_post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )