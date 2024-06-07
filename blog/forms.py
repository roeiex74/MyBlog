from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        # Django automatically infers labels from the field names from the model
        labels = {"user_name": "Name", "user_email": "Email", "text": "Comment"}
