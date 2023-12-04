from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'image']
        labels = {'text': 'Name', 'image': 'Image'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'document']
        labels = {'text': 'Content', 'document': 'Document'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80, 'rows': 2})}
