from django.urls import path
from bookstore import views

urlpatterns = [
    path('publisher/', views.publisher),
    path('add_publisher/', views.add_publisher),
    path('del_publisher/', views.del_publisher),
    path('edit_publisher/', views.edit_publisher),
    path('book_list/', views.book_list),
    path('book_add/', views.book_add),
    path('book_del/', views.book_del),
    path('book_edit/', views.book_edit),
    path('author_list/', views.author_list),
    path('author_add/', views.author_add),
    path('author_del/', views.author_del),
    path('author_edit/', views.author_edit),
]
