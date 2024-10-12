from django import forms
from home.models import Product,Category,User
from django.contrib.auth.forms import UserCreationForm
import re


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter The Product Name'
    }))
    description = forms.CharField(label='Product Details', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter The Product Details'
    }))
    image = forms.ImageField(label='Product Image', widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',
    }))
    category = forms.ModelChoiceField(label='Category Name', queryset = Category.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
        
    }))
    price = forms.IntegerField(label='Rate', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Rate of Product'
    }))
    stock = forms.IntegerField(label='Quantity Available', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Quantity of Product'
    }))
    class Meta:
        model =  Product
        fields ='__all__'
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if(len(name) < 10 ):
            return self.add_error('name','Name should have atleast 10 Characters')

        if not re.search(r'[0-9]',name):
            return self.add_error('name','Name should atleast 1 Number')

        if not re.search(r'[a-z]',name):
            return self.add_error('name','name should atleast 1 small letter')

        if not re.search(r'[A-Z]',name):
            return self.add_error('name','name should atleast 1 Capital letter')
        return name


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Category Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter The Category Name'
    }))
    class Meta:
        model = Category
        fields ='__all__'


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your First Name'
    }))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Last Name'
    }))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Username'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your email address'
    }))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your password'
    }))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Re-enter Your password'
    }))
    class Meta:
        model = User
        fields =['first_name','last_name','username','email','password1','password2']

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if(len(password) < 8 ):
            return self.add_error('password1','Password should have atleast 8 Characters')

        if not re.search(r'[a-z]',password):
            return self.add_error('password1','Password should atleast 1 small letter')

        if not re.search(r'[A-Z]',password):
            return self.add_error('password1','Password should atleast 1 Capital letter')

        if not re.search(r'[0-9]',password):
            return self.add_error('password1','Password should atleast 1 Number')

        if not re.search(r'[!@#$%^&*()_+=-]',password):
            return self.add_error('password1','Password should atleast 1 Special Character')
        return password


class LoginForm(forms.Form):
    username = forms.CharField(label = 'Usename',
                               max_length = 100,
                               required = True,
                               widget = forms.TextInput(attrs={
        'class':'form-control','placeholder':'Enter Your Username'
    }))
    password = forms.CharField(label = 'Password',
                               max_length = 100,
                               required = True,
                               widget = forms.PasswordInput(attrs={
        'class':'form-control','placeholder':'Enter Password'
    }))