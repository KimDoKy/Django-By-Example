from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<year>/<month>/<day>/<post>/', views.post_detail, name='post_detail'),
    ]
