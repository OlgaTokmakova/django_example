from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from blog.models import Message


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text='Пароль не должен быть маленьким и простым',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторно введите пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']


class ContactForm(forms.ModelForm):
    subject = forms.CharField(
        label='Тема письма*',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Форма отправки сообщений'}),
        max_length=50)
    email_address = forms.EmailField(
        label='Ваша почта*',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'}))
    message = forms.CharField(
        label='Текст сообщения*',
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст Вашего сообщения'}),
        max_length=2000)

    class Meta:
        model = Message
        fields = ['subject', 'email_address', 'message']

