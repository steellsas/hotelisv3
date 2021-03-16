from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('rooms:room_list_by_category', args=[self.slug])


class Property(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Room(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='rooms',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    visible = models.BooleanField(default=False)
    properties1 = models.ManyToManyField(Property, null= True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('rooms:room_detail',
                       args=[self.id, self.slug])

class RoomImage(models.Model):
    image = models.ImageField(upload_to='room/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True)
    order = models.PositiveBigIntegerField(null=True)
    room = models.ForeignKey(Room, default=None, related_name='images', on_delete=models.PROTECT)


    def __str__(self):
        return self.title


