from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article, Category, Reporter, Tag

class ArticleListView(ListView):
    model = Article
    template_name = "news/home.html"
    context_object_name = "latest_articles"
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.filter(status="published")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["recent_articles"] = Article.objects.filter(
            status="published"
        ).order_by("-published_date")[:5]
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = "news/article_detail.html"
    context_object_name = "article"

    def get_queryset(self):
        return Article.objects.filter(status="published")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()

        context["related_articles"] = Article.objects.filter(
            category=article.category,
            status="published"
        ).exclude(id=article.id)[:3]

        context["categories"] = Category.objects.all()
        context["recent_articles"] = Article.objects.filter(
            status="published"
        ).order_by("-published_date")[:5]

        return context

class CategoryDetailView(ListView):
    template_name = "news/category_detail.html"
    context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs["slug"])
        return Article.objects.filter(category=self.category, status="published")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category

        context["categories"] = Category.objects.all()
        context["recent_articles"] = Article.objects.filter(
            status="published"
        ).order_by("-published_date")[:5]

        return context

class ReporterDetailView(ListView):
    template_name = "news/reporter_detail.html"
    context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self):
        self.reporter = get_object_or_404(Reporter, pk=self.kwargs["pk"])
        return Article.objects.filter(reporter=self.reporter, status="published")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reporter"] = self.reporter

        context["categories"] = Category.objects.all()
        context["recent_articles"] = Article.objects.filter(
            status="published"
        ).order_by("-published_date")[:5]

        return context

class TagDetailView(ListView):
    template_name = "news/tag_detail.html"
    context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs["slug"])
        return self.tag.articles.filter(status="published")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag

        context["categories"] = Category.objects.all()
        context["recent_articles"] = Article.objects.filter(
            status="published"
        ).order_by("-published_date")[:5]

        return context