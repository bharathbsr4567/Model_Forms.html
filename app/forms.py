from django import forms

from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'

class AccessrecordsForm(forms.ModelForm):
    class Meta:
        model=Accessrecords
        fields='__all__'