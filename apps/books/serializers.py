from rest_framework import serializers
from apps.books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book;
        fields = ('id','bookName','bookAuthor','bookISBN','bookType','bookPress','bookPublishDate','bookPrice','bookNumbers','bookImageUrl','bookAuthorIntroduction','bookIntroduction')