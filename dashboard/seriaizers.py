from rest_framework import serializers
from .models import Search


class SearchSerializer(serializers.Serializer):
    # user = serializers.ForeignKey(User, on_delete=models.CASCADE)
    city = serializers.CharField()
    temperature = serializers.CharField()
    desc = serializers.CharField()
    humidity = serializers.CharField()
    icon = serializers.CharField()
    wind = serializers.CharField()
    timestamp= serializers.DateTimeField()
    class Meta:
        model = Search
        fields="__all__"

    def create(self, validated_data):
        """
        Create and return a new instance of YourModel using the validated data.
        """
        return Search.objects.create(**validated_data)