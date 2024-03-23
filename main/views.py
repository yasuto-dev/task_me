from django.http import HttpResponse
from django.views.generic import TemplateView
from users.models import User


#----Indexページ------
class IndexView(TemplateView):
    model = User
    template_name = "index.html"


# def index(request):

#     return HttpResponse("Hello, world. You're at the main index.")