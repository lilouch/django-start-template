from django import forms
from pathlib import Path
from .models import *

'''
class RecogForm(forms.Form):
    user_file = forms.FileField()

    def clean_user_file(self, *args, **kwargs):
        cleaned_data = super(RecogForm, self).clean()
        user_file = cleaned_data.get("user_file")
        if user_file:
            if user_file.size > 5 * 1024 * 1024:
                raise forms.ValidationError("File is too big.")
            if not Path(user_file).suffix.strip().lower() in ['.jpg', '.png', '.gif', '.jpeg']:
                raise forms.ValidationError(
                    "File does not look like as picture.")
'''


class RecogForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['title', 'img']
