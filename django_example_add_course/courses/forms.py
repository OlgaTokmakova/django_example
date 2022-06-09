from django import forms
from .models import Course


class CourseAddForm(forms.ModelForm):
    slug = forms.SlugField(
        label='Название URL*',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите URL'})
    )
    title = forms.CharField(
        label='Название курса*',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название курса'})
    )
    description = forms.CharField(
        label='Описание курса*',
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите подробное описание'}),
        max_length=2000
    )
    img = forms.ImageField(
        label='Изображение профиля',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Course
        fields = ['slug', 'title', 'description', 'img']
