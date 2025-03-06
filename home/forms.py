from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'platform', 'release_date', 'genre', 'publisher', 'developer', 'status', 'image',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'platform': forms.TextInput(attrs={'class': 'form-control'}),
            'release_date': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'developer': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['platform'].widget.attrs.update({'class': 'form-control unknown-text', 'placeholder': 'Unknown'})
        self.fields['release_date'].widget.attrs.update({'class': 'form-control unknown-text', 'placeholder': 'Unknown'})
        self.fields['genre'].widget.attrs.update({'class': 'form-control unknown-text', 'placeholder': 'Unknown'})
        self.fields['publisher'].widget.attrs.update({'class': 'form-control unknown-text', 'placeholder': 'Unknown'})
        self.fields['developer'].widget.attrs.update({'class': 'form-control unknown-text', 'placeholder': 'Unknown'})
        self.fields['status'].widget.attrs.update({'class': 'form-control unknown-text', 'placeholder': 'Unknown'})