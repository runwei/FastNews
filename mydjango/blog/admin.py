from django.contrib import admin
from blog.models import NewsList
from blog.models import KeyWordsList


admin.site.register(NewsList)
admin.site.register(KeyWordsList)


# class AdminBlog(admin.ModelAdmin):
#     pass

# admin.site.register(Blog, AdminBlog)

