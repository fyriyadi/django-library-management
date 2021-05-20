from rest_framework import serializers
from library_app.models import *

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)
    subject = serializers.StringRelatedField(many=True)
    

    class Meta:
        model = Book
        fields = '__all__'

        # depth = 1




