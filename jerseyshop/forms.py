from django.forms import ModelForm, forms
from .models import OrderItem

class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'
        exclude =['order', 'club_jersey', 'national_jersey', 'added_date']
