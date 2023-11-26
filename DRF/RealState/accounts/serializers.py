from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField({'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        user = User(
            username = self.validated_data['username'],
            username = self.validated_data['username'],
            username = self.validated_data['username'],
            username = self.validated_data['username'],
        )