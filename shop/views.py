from django.shortcuts import render, get_object_or_404
from .models import Category, Comic
from django.db.models import Q

def home(request):
    categories = Category.objects.all()
    # Ultimi 4 arrivi
    recent_comics = Comic.objects.filter(available=True).order_by('-created')[:4]
    return render(request, 'shop/home.html', {
        'categories': categories,
        'recent_comics': recent_comics
    })

def about(request):
    return render(request, 'shop/about.html')

def comic_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    comics = Comic.objects.filter(available=True)
    
    query = request.GET.get('q')
    if query:
        comics = comics.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(description__icontains=query)
        )
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        comics = comics.filter(category=category)
        
    return render(request,
                  'shop/comic/list.html',
                  {'category': category,
                   'categories': categories,
                   'comics': comics,
                   'query': query})

def comic_detail(request, id, slug):
    comic = get_object_or_404(Comic,
                              id=id,
                              slug=slug,
                              available=True)
    return render(request,
                  'shop/comic/detail.html',
                  {'comic': comic})
