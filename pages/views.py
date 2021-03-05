from django.views.generic.base import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class AnimePageView(TemplateView):
    template_name = 'anime.html'

class JuegosPageView(TemplateView):
    template_name = 'juegos.html'

class MangaPageView(TemplateView):
    template_name = 'Mangas.html'
    
