from django.urls import path
from . import views
from .views import AuthorListView, AuthorDetailView


urlpatterns = [
    path('', views.index, name='index'),

    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
path('authors/', AuthorListView.as_view(), name='author_list'),
path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
]
