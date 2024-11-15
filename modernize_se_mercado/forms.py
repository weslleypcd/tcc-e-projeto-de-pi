from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserCadastro, Oferta, Adicionar_oferta

class UserCadastroCreationForm(UserCreationForm):
    nome_mercado = forms.CharField(max_length=110, required=False)
    cnpj = forms.CharField(max_length=15, required=False)
    endereco = forms.CharField(max_length=110, required=False)
    telefone = forms.CharField(max_length=15, required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = UserCadastro
        fields = ['nome_mercado', 'cnpj', 'endereco', 'telefone', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserCadastro.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email
    
    def clean_nome_mercado(self):
        nome_mercado = self.cleaned_data.get('nome_mercado')
        if UserCadastro.objects.filter(nome_mercado=nome_mercado).exists():
            raise forms.ValidationError('Este nome já está em uso')
        return nome_mercado 
    
class LoginForm (forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())


class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = '__all__'
        exclude = ['status']

class Adicionar_OfertaForm(forms.ModelForm):
    class Meta:
        model = Adicionar_oferta
        fields = '__all__'
        exclude = ['status']