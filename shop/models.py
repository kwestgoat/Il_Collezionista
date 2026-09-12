from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:comic_list_by_category', args=[self.slug])

class Comic(models.Model):
    CONDITION_CHOICES = [
        ('M', 'Mint (Edicola)'),
        ('NM', 'Near Mint (Ottimo)'),
        ('FN', 'Fine (Buono)'),
        ('VG', 'Very Good (Discreto)'),
        ('GD', 'Good (Accettabile)')
    ]

    category = models.ForeignKey(Category, related_name='comics', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='comics/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=2, choices=CONDITION_CHOICES, default='NM', verbose_name="Stato di conservazione")
    is_sold = models.BooleanField(default=False, verbose_name="Venduto (Pezzo Unico)")
    stock = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:comic_detail', args=[self.id, self.slug])

class ComicImage(models.Model):
    comic = models.ForeignKey(Comic, related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comics_details/%Y/%m/%d')
    description = models.CharField(max_length=200, blank=True, help_text="Es. Fronte, Retro, Dettaglio strappo")

    def __str__(self):
        return f"Immagine per {self.comic.title} - {self.description}"
