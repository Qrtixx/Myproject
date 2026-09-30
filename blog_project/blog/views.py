from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ArticleForm, CommentForm, RegistrationForm
from .models import Article, Category


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 6


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated:
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.author = request.user
            comment.save()
            messages.success(request, 'Комментарий добавлен.')
            return redirect(self.object.get_absolute_url())
        return render(request, self.template_name, {'object': self.object, 'comment_form': form})


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'

    def test_func(self):
        return self.get_object().author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.get_object().author == self.request.user


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            messages.success(request, 'Регистрация выполнена.')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})


def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'blog/article_list.html', {
        'articles': Article.objects.filter(category=category),
        'current_category': category,
    })
