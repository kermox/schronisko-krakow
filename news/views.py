import operator
from itertools import chain

from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Post, FacebookPost


class NewsListView(ListView):
    model = Post
    template_name = 'news/news-list.html'
    paginate_by = 8
    extra_context = {
        'post_list_page': 'active'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsListView, self).get_context_data(object_list=self.get_queryset())
        context['topic_list'] = Topic.objects.all()
        return context

    def get_queryset(self):
        super(NewsListView, self).get_queryset()
        queryset = sorted(chain(Post.objects.filter(status='published', topic=None),
                                FacebookPost.objects.filter(status='published')),
                          key=operator.attrgetter('pinned', 'created_at'), reverse=True)
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post-details.html'
    context_object_name = 'post'
    extra_context = {
        'post_detail_page': 'active'

    }


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'news/news-topic-detail.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data()
        context['topic_page'] = 'active'
        context['topic_list'] = Topic.objects.all()
        context['topic_post_list'] = sorted(self.get_object(queryset=None).post_set.all(), key=operator.attrgetter(
                                                                                 'pinned', 'created_at'), reverse=True)
        return context


def update_facebook_posts(request):
    if request.method == "POST":
        from utils.facebook_posts import get_facebook_posts
        get_facebook_posts()
        return redirect(reverse('admin:news_facebookpost_changelist'))
