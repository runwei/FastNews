from django.contrib import admin
from blog.models import NewsList
from blog.models import KeyWordsList
from blog.models import UserInfo


admin.site.register(NewsList)
admin.site.register(KeyWordsList)
admin.site.register(UserInfo)


# class AdminBlog(admin.ModelAdmin):
#     pass

# admin.site.register(Blog, AdminBlog)

