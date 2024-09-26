from django.forms import ModelForm
from .models import Topic

class TopicForms(ModelForm):
    class Meta:
        model = Topic
        exclude = []
        fields = '__all__'



