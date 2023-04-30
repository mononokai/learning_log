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
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # Widgets are HTML form elements like text boxes and drop downs
        # The widgets attribute lets us alter Django's default widget values
        # By supplying a value of 80 to the 'cols' key, we are making the text area 80 columns wide
        # whereas the default is only 40
