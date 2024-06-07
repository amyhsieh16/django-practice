from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee
from django.db import transaction

class RegisterSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(max_length=255, write_only=True, required=True)
    
    password = serializers.CharField(max_length=255, write_only=True, required=True)
    password2 = serializers.CharField(max_length=255, write_only=True, required=True)

    employee_no = serializers.IntegerField(required=True)
    
    class Meta:
        model = Employee
        fields = ('id', 'employee_name', 'email', 'password', 'password2', 'employee_no')
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "XXXXXXXX fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create(
                username=validated_data['employee_name'], 
                email=validated_data['email'], 
                password=validated_data['password']
            )

            employee=Employee.objects.create(
                user=user, 
                employee_name=validated_data['employee_name'],
                employee_no=validated_data['employee_no']
            )
        serializers = EmployeeSerializer(employee)
        return serializers.data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Employee
        fields = '__all__'

