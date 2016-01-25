 #-*- coding: utf-8 -*-
from django import forms
from socitey.models import Member, Personal_bill, Bill_table
from django.utils import timezone

class MemberForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['phone', 'name', 'sexual','balance']

    def clean(self):
        cleaned_data = self.cleaned_data
        code = cleaned_data.get('phone')

        if Item.objects.filter(phone=phone).exists():
            self._errors['phone'] = self.error_class(['this phone exists'])  

        return cleaned_data
"""
class BillTableForm(forms.ModelForm):
    class Meta:
        model = Bill_table

    def save(self): # create new table
        new_table=Bill_table.objects.create(
            created_at=timezone.now(),
            total_price=0,
            comment=self.data['comment'],
        )

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill

    def save(self): # create new bill
        new_table=Bill.objects.create(
            item_code=Item.objects.get(code=self.data['item_code']),
            bill_table=Bill_table.objects.get(id=self.data['bill_table']),
            created_at=timezone.now(),
            number=self.data['number'],
            bill_comment=self.data['bill_comment'],
        )
        
class AuthenticationForm(forms.Form):

            username = forms.CharField(widget=forms.TextInput())
            password = forms.CharField(widget=forms.PasswordInput())

            class Meta:
                fields = ['username', 'password']

"""