from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.Serializer):
#     firt_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     number = serializers.IntegerField()
#     age = serializers.IntegerField()
    
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.firt_name = validated_data.get('firt_name', instance.firt_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields = "__all__" # tüm field kısımlarını alıyor
        # fields = ["firt_name","last_name"] # sadece istediğimiz filed ksımları alınıyor
        # exclude = ["number"]  # belirtilen field hariç geri kalanlar