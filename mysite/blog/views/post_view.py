from django.views import generic
from django.http import HttpResponse

from ..models import Post


from django.views import View
from django.http import HttpResponse

# vai alimentar a lista no index.html

# ao a url chamar essa view ela devolve uma list de todas as publicações


class PostView(generic.ListView):
    # filtra todos com status = 1 (seria publicado)
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # declara o template
    template_name = 'index.html'


class ViewsExercicio(View):
    def get(self, request):
        return HttpResponse("Hello World")  # Resposta simples


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
