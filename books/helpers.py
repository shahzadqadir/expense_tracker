from books.models import Category, Book
from datetime import datetime
from django.utils import timezone
from decimal import Decimal
import csv


def read_categories(filename):
    categories = []
    category_objs = []
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)    # skip csv file headers
        for row in reader:
            category = row[6].lower().strip()
            if category not in categories and category != "":
                categories.append(category)
    for cat in categories:
        category_objs.append(Category(name=cat))
    return category_objs


def read_books(filename):
    book_objs = []
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)    # skip headers
        for row in reader:
            if len(row) < 8:
                continue
            try:
                published_date=datetime.strptime(row[5], '%m/%d/%Y').date()
            except ValueError:
                published_date=timezone.now()
            if row[6] == "":
                Category.objects.get(id=1)
            else:
                category=Category.objects.get(name=row[6].lower().strip())
            book_objs.append(
            Book(
                serial=row[0],
                title=row[1],
                subtitle=row[2],
                authors=row[3],
                publisher=row[4],
                published_date=published_date,              
                category=category,
                distribution_expense=Decimal(row[7]),
            ))
    return book_objs