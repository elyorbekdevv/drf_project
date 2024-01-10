from django.urls import path
from .views import *
from .views import BookViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewset, basename='books')


urlpatterns = [
    # path('books/', BookAPIView.as_view()),
    # # path('books', book_detail,)
    # path('bookcl/', BookListCreateAPIView.as_view()),
    # path('books/<int:pk>/', BookDetailAPIView.as_view()),
    # # path('bookud/<int:pk>/', BookUpdateDeleteView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateAPIView.as_view()),
    # path('books/create/', BookCreateAPIView.as_view())
]


urlpatterns = urlpatterns + router.urls