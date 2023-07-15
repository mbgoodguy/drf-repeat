from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}, ID: {self.id}'


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_books')
    reader = models.ManyToManyField(User, through='UserBookRelation', related_name='books')

    def __str__(self):
        return f'{self.name}'


class UserBookRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Worse'),
        (2, 'Bad'),
        (3, 'Normal'),
        (4, 'Good'),
        (5, 'Excellent'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)
