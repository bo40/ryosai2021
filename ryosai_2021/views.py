

from django.views.generic import TemplateView 
from .models import Post, Pro


class TwentysixView(TemplateView):
    template_name = "1126.html"
    
class TwentysevenView(TemplateView):
    template_name = "1127.html"

class TwentyeightView(TemplateView):
    template_name = "1128.html"
    
class TwentynineView(TemplateView):
    template_name = "1129.html"

class ThirtyView(TemplateView):
    template_name = "1130.html"

class ThirtyoneView(TemplateView):
    template_name = "1131.html"
from django.views.generic import ListView

# ListViewは一覧を簡単に作るためのView

class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    template_name = "list.html"
    model = Post
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tag_list'] = Pro.objects.all
        return context

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# CreateViewは新規作成画面を簡単に作るためのView
class Create(CreateView):
    template_name = "create.html"
    model = Post
    
    # 編集対象にするフィールド
    fields = ["title", "body", "category"]
    success_url = reverse_lazy('list')
    


