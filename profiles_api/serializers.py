from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serilize the Hello passed input data"""

    name = serializers.CharField(max_length=10)
