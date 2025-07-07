from ckeditor.widgets import CKEditorWidget
from Blog.models import Post
from django import forms


class PostAdminForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    content = forms.CharField(widget=CKEditorWidget())