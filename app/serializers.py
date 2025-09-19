from rest_framework import serializers
from app.models import student

# class studentserializer(serializers.Serializer):


#     id = serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     email=serializers.EmailField()
#     contact=serializers.IntegerField()


#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
            
            
#             """
#             Update and return an existing `Snippet` instance, given the validated data.
#             """
#             instance.name = validated_data.get('name', instance.name)
#             instance.email = validated_data.get('email', instance.email)
#             instance.contact = validated_data.get('contact', instance.contact)
#             instance.save()
#             return instance

# class based----------------------------------
class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'
