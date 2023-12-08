from django.shortcuts import render
from .models import Book, Reader, BookIssue
from datetime import date

# Book.objects.create(
#     inventory_number='B001',
#     author='John Doe',
#     title='Django for Beginners',
#     genre='Technical',
#     year=2021,
#     pages=300,
#     price=29.99,
#     book_type='Book',
#     copies=5,
#     max_days=15
# )
#
# Book.objects.create(
#     inventory_number='B002',
#     author='Jane Smith',
#     title='Advanced Django',
#     genre='Technical',
#     year=2022,
#     pages=350,
#     price=34.99,
#     book_type='Manual',
#     copies=3,
#     max_days=20
# )
#
# # Sample data for Readers
# Reader.objects.create(
#     card_number='R001',
#     last_name='Brown',
#     first_name='Charlie',
#     phone='123456789',
#     address='123 Main St',
#     course=2,
#     group='CS101'
# )
#
# Reader.objects.create(
#     card_number='R002',
#     last_name='Johnson',
#     first_name='Lucy',
#     phone='987654321',
#     address='456 Elm St',
#     course=3,
#     group='CS102'
# )
#
# # Sample data for Book Issues
# BookIssue.objects.create(
#     issue_code='I001',
#     issue_date=date.today(),
#     reader=Reader.objects.get(card_number='R001'),
#     book=Book.objects.get(inventory_number='B001')
# )
#
# BookIssue.objects.create(
#     issue_code='I002',
#     issue_date=date.today(),
#     reader=Reader.objects.get(card_number='R002'),
#     book=Book.objects.get(inventory_number='B002')
# )


def lib_view(request):
    books = Book.objects.all()
    readers = Reader.objects.all()
    book_issues = BookIssue.objects.all()

    return render(request, 'UniversityLib/lib.html', {
        'books': books,
        'readers': readers,
        'book_issues': book_issues
    })
