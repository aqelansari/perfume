from django.contrib.auth.models import User
from rest_framework import serializers
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage
from user_management.models import Profile


USER_TYPE = [('AD', 'Admin'), ('LI', 'Lab Incharge'), ('SI', 'Shift Incharge'), ('WK', 'Worker')]

class AppUserSerializer(serializers.ModelSerializer):
    profile_pic_image = serializers.ImageField(allow_null=False,required=True)
    user_type = serializers.ChoiceField(choices=USER_TYPE,default='WK')

    class Meta:
        model = User
        exclude = ('is_staff', 'date_joined', 'user_permissions', 'groups', 'last_login', 'is_superuser','email')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user_type = validated_data['user_type']
        if user_type == 'AD':
            validated_data['is_superuser'] = True
            validated_data['is_staff'] = True
            validated_data['is_active'] = True
        else:
            validated_data['is_active'] = True
            validated_data['is_staff'] = True
        
        profile_pic = validated_data['profile_pic_image']
        user_type = validated_data['user_type']
        del validated_data['profile_pic_image']
        del validated_data['user_type']
        user = User.objects.create_user(**validated_data)
        profile_pic_path = os.path.join(settings.MEDIA_ROOT,'profile_pic')
        
        
        file_path = profile_pic_path.split('media')
        image_path = 'media/'+str(user.id)+file_path[1]
        os.makedirs(image_path, exist_ok=True)
        fs = FileSystemStorage(image_path)
        file_name = fs.save(profile_pic.name,profile_pic)
        image_url = image_path+'/' + file_name
        
        Profile.objects.create(i_user=user,profile_pic=image_url,user_type=user_type)
        validated_data['profile_pic_image'] = image_url
        validated_data['user_type'] = user_type
        return validated_data

    
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Employee ID already taken')
        else:
            if value.isdigit():
                if len(value) == 5:
                    return value
                else:
                    raise serializers.ValidationError('Please enter 5 digit Employee ID')
            else:
                raise serializers.ValidationError('Please enter Numeratic Employee ID only')
    
    def validate_password(self, value):
        if value.isdigit():
            if len(value) == 5:
                return value
            else:
                raise serializers.ValidationError('Please enter 5 digit password')
        else:
            raise serializers.ValidationError('Please enter Numeratic password only')
            

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        
    def validate_username(self, value):
        if value.isdigit():
            if len(value) == 5:
                if User.objects.filter(username=value).exists():
                    return value
                raise serializers.ValidationError('No Employee ID found')
            else:
                raise serializers.ValidationError('Please enter 5 digit Employee ID')
        else:
            raise serializers.ValidationError('Please enter Numeratic Employee ID only')

       
class AllUsersSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','last_login']

class AllUsersPicsSerializer(serializers.ModelSerializer):
    i_user = AllUsersSerializer()
    class Meta:
        model = Profile
        fields = ['profile_pic', 'user_type', 'i_user']


class ChangePasswordSerializer(serializers.Serializer):
    username = serializers.IntegerField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.get(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            return value
        raise serializers.ValidationError('No username exist')


