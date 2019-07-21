from django import forms
from .models import Post, Comment


#########################################################################################################
#####   PostForm is a form of Post Model
#########################################################################################################

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text',)

        # widgets is used for CSS styling
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


#########################################################################################################
#####   CommentForm is a form of Comment Model
#########################################################################################################

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        # widgets is used for CSS styling
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }

