from rest_framework import serializers
from .models import Skill, SkillOf, TopicHeadings, TopicSubHeadings, Topic


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [ 'name', 'status' ]
        # exclude = ['id', 'slug', 'slugs', 'skillsof']
        # fields = '__all__'
        
class SkillOfSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = SkillOf
        fields = '__all__'

class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicHeadings
        fields = '__all__'

class SubheadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicSubHeadings
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'