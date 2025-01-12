from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import GamecritPostForm, GameCritCommentForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("created_on")
    template_name = "gamecrit_post/index.html"
    paginate_by = 4


class AddGamecritPost(CreateView):
    """
    Add gamecrit post view
    A user that is logged in can create a new post to the database
    used this video as tutorial: https://www.youtube.com/watch?v=vXMTp_1_L7Y
    """
    template_name = "gamecrit_post/gamecrit_post.html"
    model = Post
    form_class = GamecritPostForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super(AddGamecritPost, self).form_valid(form)



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

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        gamecrit_post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = GameCritCommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.username == request.user:
            comment = comment_form.save(commit=False)
            comment.post_id = gamecrit_post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('display_game_review', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comments
    """
    queryset = Post.objects.filter(status=1)
    gamecrit_post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.username == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Your comment was deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')
    return HttpResponseRedirect(reverse('display_game_review', args=[slug]))

