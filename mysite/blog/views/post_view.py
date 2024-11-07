from django.views import generic
from django.http import HttpResponse

from ..models import Post


from django.views import View
from django.http import HttpResponse


class ViewsExercicio(View):
    def get(self, request):
        return HttpResponse("Hello World")  # Resposta simples


class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # Retorna um simples "Hello, World!" como resposta
        return HttpResponse("Hello, World!")


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
