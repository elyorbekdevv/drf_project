from rest_framework import serializers
from .models import Book
from django.core.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title', 'content', 'subtitle', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author  = data.get('author', None)
        if not title.isalpha():
            raise ValidationError(
                {
                    "status":False,
                    "message":"Iltimos, formatga mos ma'lumot kiriting!"
                }
            )
        
        if title == author:
            raise ValidationError(
                {
                    "message":"Kitobning nomi va muallifi bir xil bolmaslikigi kerak"
                }
            )
        return data
    
    def validate_isbn(self, isbn):
        if isbn.isalpha():
            raise ValidationError(
                {
                    "message":"Kitob kodini to\'g\'ri kiriting!"
                }
            )
        return isbn
        
    def validate_price(self, price):
        if price < 0 or price > 999999999:
            raise ValidationError(
                {
                    "message":'Siz noto\'g\'ri narx kiritdingiz!'
                }
            )
        return price