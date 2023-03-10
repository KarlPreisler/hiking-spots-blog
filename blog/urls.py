from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post', views.AddPost.as_view(), name='add_post'),
    path('edit/<int:pk>', views.EditPost.as_view(),
         name='edit_post'),
    path('delete/<int:pk>', views.DeletePost.as_view(),
         name='delete_post'),
    path('about', views.About.as_view(), name='about'),
    path('difficulty', views.Difficulty.as_view(), name='difficulty'),
]
