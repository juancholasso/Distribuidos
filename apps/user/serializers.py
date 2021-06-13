from rest_framework import serializers
from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):

    document = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('name', 'lastname', 'document_type', 'document', 'city')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance