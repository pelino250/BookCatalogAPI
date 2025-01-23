from rest_framework import serializers

from api.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'image']
        # extra_kwargs = {
        #     'bio': {'write_only': True},
        # }


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'author', 'year', 'genre', 'publisher', 'isbn', 'image', 'description']

