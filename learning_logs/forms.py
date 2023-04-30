from django import forms
from .models import Topic, Entry

# Defining a class 'TopicForm', which inherits from 'forms.ModelForm'
class TopicForm(forms.ModelForm): # ModelForm automatically builds a form using our defined models
    class Meta:
        model = Topic # Building form based on the Topic model
        fields = ['text'] # Include a text field
        labels = {'text': ''} # This specifies not to make a label for the text field

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

