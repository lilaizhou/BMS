from django.contrib import admin

# Register your models here.
from library.models import *

admin.site.register(Book)
admin.site.register(Publish)
admin.site.register(Author)
admin.site.register(AuthorDetail)


