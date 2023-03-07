from django.http import response
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from articles.models import Article


# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'pages/home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'pages/articles/article-detail.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'pages/articles/article-create.html'
    fields = ['title', 'body', 'published', 'thumbnail', 'image']
    success_url = reverse_lazy('articles')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    success_url = reverse_lazy('articles')
    template_name = 'pages/articles/article-update.html'
    fields = ['title', 'body', 'published', 'thumbnail', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('articles')
    template_name = 'pages/articles/article-delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
