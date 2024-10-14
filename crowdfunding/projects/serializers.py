from rest_framework import serializers
from django.apps import apps
from .models import Pledge
from .models import CustomUserSerializer



class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    
    #specify which model to serialize and which fields to include.
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'
        
    #defines a list of fields that will be included in the serialization process
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']
    
    #create a new Pledge instance using data that has already been validated by the serializer
    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)
        
    #update an existing Pledge instance and validate data
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.project = validated_data.get('project', instance.project)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.save()
        return instance
        
class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = apps.get_model('projects.Project')
        fields = '__all__'

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    liked_by = CustomUserSerializer(many=True, read_only=True)
    
    
    #update and apply changes to an existing instance
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.data_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance






# class ProjectSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField(max_length=None)
#     goal = serializers.IntegerField()
#     cause = serializers.ChoiceField(choices= Project.Project_type)
#     total_likes = serializers.IntegerField(read_only=True)
#     total_pledges = serializers.IntegerField(read_only=True)
#     image = serializers.URLField()
#     is_open = serializers.BooleanField()
#     is_active = serializers.BooleanField()
#     date_created = serializers.DateTimeField(read_only=True)
#     # date_end = serializers.DateTimeField()
#     owner = serializers.ReadOnlyField(source='owner.id')
#     # pledges = PledgeSerializer(many=True, read_only=True)

#     def create(self, validated_data):
#         return Project.objects.create(**validated_data)

