from rest_framework import serializers


class NewSerializer(serializers.Serializer):
    headline = serializers.CharField()
    link = serializers.CharField()
    source = serializers.CharField()
