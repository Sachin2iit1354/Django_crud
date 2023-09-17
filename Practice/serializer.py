from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
    def create(self, validated_data):
        surname=self.context['request'].query_params.get('surname')
        print(surname)
        print(validated_data)
        validated_data['name']=surname
        return super().create(validated_data)