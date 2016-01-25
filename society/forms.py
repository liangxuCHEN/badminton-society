 #-*- coding: utf-8 -*-
from django import forms
from society.models import Member, Personal_bill, Bill_table
from django.utils import timezone

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['phone', 'name', 'sexual','balance']

    def clean(self):
        cleaned_data = self.cleaned_data
        phone = cleaned_data.get('phone')

        if Member.objects.filter(phone=phone).exists():
            self._errors['phone'] = self.error_class(['this phone exists'])  

        return cleaned_data

class BillTableForm(forms.ModelForm):
    class Meta:
        model = Bill_table

    def save(self): # create new table
        new_table=Bill_table.objects.create(
            created_at=timezone.now(),
            total_price=0,
            comment=self.data['comment'],
        )

class PersonalBillForm(forms.ModelForm):
    class Meta:
        model = Personal_bill

    def save(self): # create new bill
        new_table=Personal_bill.objects.create(
            member=Member.objects.get(phone=self.data['member_phone']),
            bill_table=Bill_table.objects.get(id=self.data['bill_table']),
            created_at=timezone.now(),
            price=self.data['price'],
            bill_comment=self.data['bill_comment'],
        )
      
class AuthenticationForm(forms.Form):

            username = forms.CharField(widget=forms.TextInput())
            password = forms.CharField(widget=forms.PasswordInput())

            class Meta:
                fields = ['username', 'password']

