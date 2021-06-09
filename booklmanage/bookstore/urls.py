from django.urls import path
from bookstore import views

urlpatterns = [
    path('publisher_list/', views.publisher),
    # path('add_publisher/', views.add_publisher),
    path('add_publisher/', views.AddPublisher.as_view()),
    path('del_publisher/', views.del_publisher),
    path('edit_publisher/<int:pk>/', views.edit_publisher),
    path('book_list/', views.book_list),
    path('book_add/', views.book_add),
    path('book_del/', views.book_del),
    path('book_edit/', views.book_edit),
    path('author_list/', views.author_list),
    path('author_add/', views.author_add),
    path('author_del/', views.author_del),
    path('author_edit/', views.author_edit),
    path('get_json/', views.get_json),
]
