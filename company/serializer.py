
from rest_framework import serializers
from company.models import Company, WorkStation


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        validated_data['status'] = True
        company = Company.objects.create(**validated_data)
        return company
    
    


class AllCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'status']


class WorkstationSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkStation
        fields = '__all__'

    def create(self, validated_data):
        validated_data['status'] = True
        workstation = WorkStation.objects.create(**validated_data)
        return workstation
    
    def validate_company(self, data):
        obj = Company.objects.filter(status = True,id = data.id).exists()
        if obj:
            return data
        else:
            raise serializers.ValidationError("Company not found")


        
class AllWorkstationSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    
    class Meta:
        model = WorkStation
        fields = ['id', 'name', 'production_capacity','company']