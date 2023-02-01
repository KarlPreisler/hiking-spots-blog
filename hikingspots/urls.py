from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'), name='blog-urls'),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
]

handler403 = 'blog.views.handler403'
handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'
handler405 = 'blog.views.handler405'
