from django.db import models


class Book(models.Model):
    GENRE_CHOICES = [
        ('Technical', 'Technical'),
        ('Art', 'Art'),
        ('Economic', 'Economic'),
    ]
    TYPE_CHOICES = [
        ('Manual', 'Manual'),
        ('Book', 'Book'),
        ('Periodical', 'Periodical'),
    ]
    inventory_number = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    year = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    book_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    copies = models.PositiveIntegerField()
    max_days = models.PositiveIntegerField()


class Reader(models.Model):
    COURSE_CHOICES = [(i, str(i)) for i in range(1, 5)]
    card_number = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    course = models.IntegerField(choices=COURSE_CHOICES)
    group = models.CharField(max_length=50)


class BookIssue(models.Model):
    issue_code = models.CharField(max_length=100, unique=True)
    issue_date = models.DateField()
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
