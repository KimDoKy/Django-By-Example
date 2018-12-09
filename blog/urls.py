from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
#    path('', views.PostListView.as_view(), name='post_list'),
    path('', views.post_list, name='post_list'),
    path('tag/<tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<year>/<month>/<day>/<post>/', views.post_detail, name='post_detail'),
    path('<post_id>/share/', views.post_share, name='post_share'),
    ]
