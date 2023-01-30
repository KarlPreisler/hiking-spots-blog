from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm, AddPostForm, EditPostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        if request.user.is_authenticated:
            post = get_object_or_404(Post, slug=slug, status=1)
            comments = post.comments.filter(
                approved=True).order_by("-created_on")
            liked = False
            if post.likes.filter(id=self.request.user.id).exists():
                liked = True
            comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment is awaiting approval!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostLike(LoginRequiredMixin, View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(View):
    """
    Add post view, displays & handles the form to add a post
    """
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'add_post.html',
            {
                "add_post_form": AddPostForm(),
            }
        )

    def post(self, request, *args, **kwargs):

        add_post_form = AddPostForm(data=request.POST)

        if add_post_form.is_valid():
            add_post_form.instance.user = self.request.user
            name = add_post_form.cleaned_data.get('name')
            add_post_form.save()
            messages.success(request, 'You successfully added a blog post')
        else:
            add_post_form = AddPostForm()

        return render(
            request,
            'add_post.html',
            {
                "add_post_form": AddPostForm(),
            }
        )


class EditPost(UpdateView):
    model = Post
    template_name = 'post_form.html'
    form_class = EditPostForm
    success_url = reverse_lazy('home')


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'delete_post.html'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        data_to_return = super(
            DeletePost, self).delete(request, *args, **kwargs)
        return data_to_return


class About(CreateView):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class Difficulty(CreateView):
    template_name = 'difficulty.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


def handler403(request, exception):
    """
    Custom 403 page
    """
    return render(request, 'errors/403.html', status=403)


def handler500(request):
    """
    Custom 500 page
    """
    return render(request, 'errors/500.html', status=500)


def handler404(request, exception):
    """
    Custom 404 page
    """
    return render(request, 'errors/404.html', status=404)


def handler405(request, exception):
    """
    Custom 405 page
    """
    return render(request, 'errors/405.html', status=405)
