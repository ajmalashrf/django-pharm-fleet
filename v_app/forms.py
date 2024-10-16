from django import forms
from .models import ContactMessage,Order

class DateInput(forms.DateInput):
    input_type = 'date'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'order_date': DateInput()
        }
        labels = {
            'cus_name': "Name",
            'cus_phone': "Phone",
            'cus_email': "Email",
            'cat_name' :"category",
            'pro_name' :"Mention your product for verify",
            'order_date':"Enter the delivery date you want"
        }
        

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'

        widgets = {
            'order_date': DateInput()
        }
        labels = {
            'name': "Name:",
            'last_name': "Last Name",
            'email': "Email",
            'phone_number' :"Phone",
            'subject' :"Subject",
            'message':"Message",
            'image' :"Upload"
        }
        