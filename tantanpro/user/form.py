from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    def distance_data_clearn(self):
        max_distance = self.cleaned_data.get("max_distance")
        min_distance = self.cleaned_data.get("min_distance")

        if max_distance < min_distance:
            raise forms.ValidationError('最大距离错误')

        return max_distance

    def age_distance_clearn(self):
        max_dating_age = self.cleaned_data.get('max_dating_age')
        min_dating_age = self.cleaned_data.get('min_dating_age')

        if max_dating_age < min_dating_age:
            raise forms.ValidationError('最大年龄错误')
        return max_dating_age

    class Meta:
        model = Profile
        fields = [
            'location',
            'min_distance',
            'max_distance',
            'min_dating_age',
            'max_dating_age',
            'dating_sex'
        ]