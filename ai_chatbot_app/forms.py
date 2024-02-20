from django import forms
from ai_chatbot_app.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']

class AskQuestionForm(forms.Form):
    question=forms.CharField(max_length=64)        
