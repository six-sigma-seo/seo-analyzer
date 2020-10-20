from django.shortcuts import render

# Create your views here.
def scraping_view(request):
  return render(request, 'Hola Mundo esta será la pagina de inicio')