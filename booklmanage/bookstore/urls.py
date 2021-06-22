from django.urls import path
from bookstore import views

urlpatterns = [
    path('publisher_list/', views.publisher, name="publisher"),
    # path('add_publisher/', views.add_publisher),
    path('add_publisher/', views.AddPublisher.as_view(), name="add_publisher"),
    # path('del_publisher/', views.del_publisher, name="del_publisher"),
    path('edit_publisher/<int:pk>/', views.edit_publisher, name="edit_publisher"),
    path('book_list/', views.book_list, name="book"),
    path('book_add/', views.book_add, name="add_book"),
    # path('book_del/', views.book_del, name="del_book"),
    path('book_edit/', views.book_edit, name="edit_book"),
    path('author_list/', views.author_list, name="author"),
    path('author_add/', views.author_add, name="add_author"),
    # path('author_del/', views.author_del, name="del_author"),
    path('author_edit/', views.author_edit, name="edit_author"),
    path('get_json/', views.get_json),
    path('<str:name>/<int:pk>/', views.delete, name="delete")
]

