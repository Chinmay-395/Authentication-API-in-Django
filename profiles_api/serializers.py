""" 
Converts data inputs to python objects just like forms.py also,
checks if the data types of the input wrt to the input given by the user
also take care of validation
"""
from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

# class HelloSerializer(serializers.Serializer):
#     """ Serilizes a name field for testing our APIView """
#     name = serializers.CharField(max_length=10)
