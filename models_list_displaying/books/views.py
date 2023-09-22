from datetime import datetime

from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book

def books_view(request, raw_date = None):
    template = 'books/books_list.html'
    
    page_number = None
    next_date = None
    prev_date = None

    if raw_date:
        page_number = datetime.strptime(raw_date, '%Y-%m-%d')

    if page_number:
        raw_dates = Book.objects.values('pub_date').order_by('pub_date').distinct().all()
    
        dates = [date['pub_date'] for date in raw_dates]
        print(dates, dates.index(page_number.date()))

        data_index = dates.index(page_number.date())

        if data_index != len(dates)-1:
            next_date = dates[data_index+1].strftime('%Y-%m-%d')
        
        if data_index != 0:
            prev_date = dates[data_index-1].strftime('%Y-%m-%d')

        raw_books = Book.objects.filter(pub_date=page_number).all()
        books = [book for book in raw_books]

        
    else:
        books = Book.objects.all()

    
    context = {'books': books,
                'next_date': next_date,
                'prev_date': prev_date}
    
    print(context)
    return render(request, template, context)
