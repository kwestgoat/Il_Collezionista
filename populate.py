import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collezionista.settings')
django.setup()

from shop.models import Category, Comic

def populate():
    # Categorie
    cat_marvel, _ = Category.objects.get_or_create(name='Supereroi', slug='supereroi')
    cat_manga, _ = Category.objects.get_or_create(name='Manga', slug='manga')
    cat_bonelli, _ = Category.objects.get_or_create(name='Italiani', slug='italiani')
    cat_indie, _ = Category.objects.get_or_create(name='Indipendenti', slug='indipendenti')
    
    # Fumetti Finti
    comics_data = [
        {
            'category': cat_marvel,
            'title': 'L\'Uomo Ragno Cosmico #1',
            'slug': 'uomo-ragno-cosmico-1',
            'author': 'Stan Lee, Jack Kirby',
            'price': '4.99',
            'stock': 10,
            'description': 'Una nuova incredibile avventura nello spazio per il nostro amichevole Uomo Ragno di quartiere!'
        },
        {
            'category': cat_marvel,
            'title': 'I Vendicatori: Crisi Temporale',
            'slug': 'vendicatori-crisi-temporale',
            'author': 'Brian Michael Bendis',
            'price': '15.50',
            'stock': 5,
            'description': 'Il gruppo di eroi si trova ad affrontare una minaccia proveniente dal futuro.'
        },
        {
            'category': cat_manga,
            'title': 'Ninja Scroll of the Dragon vol. 1',
            'slug': 'ninja-scroll-dragon-1',
            'author': 'Akira Toriyama',
            'price': '5.90',
            'stock': 20,
            'description': 'L\'inizio dell\'epica saga del dragone bianco.'
        },
        {
            'category': cat_manga,
            'title': 'Samurai Cyberpunk vol. 3',
            'slug': 'samurai-cyberpunk-3',
            'author': 'Masamune Shirow',
            'price': '7.50',
            'stock': 2,
            'description': 'Le lame incontrano il neon in un futuro distopico.'
        },
        {
            'category': cat_bonelli,
            'title': 'Detective dell\'Occulto: Il Mistero di Venezia',
            'slug': 'detective-occulto-venezia',
            'author': 'Tiziano Sclavi',
            'price': '3.90',
            'stock': 15,
            'description': 'Indagare sui fantasmi della laguna non è mai stato così pericoloso.'
        },
        {
            'category': cat_indie,
            'title': 'Gatti Spaziali contro Alieni',
            'slug': 'gatti-spaziali-alieni',
            'author': 'Fumettista Sconosciuto',
            'price': '12.00',
            'stock': 8,
            'description': 'Una graphic novel indipendente acclamata dalla critica (e dai felini).'
        }
    ]
    
    for data in comics_data:
        comic, created = Comic.objects.get_or_create(
            slug=data['slug'],
            defaults=data
        )
        if not created:
            # Aggiorna se esiste
            for k, v in data.items():
                setattr(comic, k, v)
            comic.save()
            
    print("Database popolato con successo!")

if __name__ == '__main__':
    populate()
