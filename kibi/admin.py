from django.contrib import admin
from kibi.models import Post


class PostAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist post. """
    list_display = ('title', 'slug', 'author', 'created', 'modified')


admin.site.register(Post, PostAdmin)
