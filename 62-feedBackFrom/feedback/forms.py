from django import forms


class FeedBackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'hello',
        'placeholder': 'Full Name'
    }))
    rollno = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': '4 digits number'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'only gmail'
        
    }), required=False, label='Email Address')
    feedback = forms.CharField(widget=forms.Textarea)

    def clean_feedback(self):
        feedback = self.cleaned_data['feedback']
        
        num_words = len(feedback.split())
        if num_words < 5:
            raise forms.ValidationError('Not Enough Words, at least 6')
        
        return feedback

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) < 4:
            raise forms.ValidationError('Name Must be at least 5 characters')
        return name

