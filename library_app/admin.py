from django.contrib import admin
from library_app.models import Book, Author, Publisher, Subject, Borrow

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)
    fields = ['title','author', 'subject', 'date_added',]
    # author and subject can't be displayed with for loop
    # fields = [field.name for field in Book._meta.fields if field.name != "id"]
    list_display = ['title','date_added']

    #display author for list_display
    def author_list(self, obj):
        return "\n".join([p.author for p in obj.author.all()])

class BorrowAdmin(admin.ModelAdmin):
    fields = (
        'book',
        'user',
        'request_date', 
        'start_date', 
        'finish_date',
        'approval_status',
        'notes'
    )
    list_display = [
        'book',
        'user', 
        'request_date', 
        'start_date', 
        'finish_date', 
        'approval_status'
    ]
    list_filter = [
        'book',
        'user',
        'approval_status',
    ]
    #search fields refer to related field name
    search_fields = ['book__title','user__username']

admin.site.register(Book, BookAdmin)
admin.site.register(Borrow, BorrowAdmin)
admin.site.register([
    Author,
    Publisher,
    Subject,    
])
