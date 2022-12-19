from django import forms

from repairs.models import PlacesToWork, Repair, Status, TypeRepair


class TechnicianForm(forms.ModelForm):

    description = forms.CharField(
        label="Описание поломки",
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    time_to_work = forms.DateTimeField(
        label="(ГГГГ-ММ-ДД чч:мм:сс) Дата и время начала работы",
        widget=forms.DateTimeInput(attrs={'class': 'form-control'})
    )
    places_to_work = forms.ModelChoiceField(
        label="Место проведения работ",
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=PlacesToWork.objects.all()
    )
    type_repair = forms.ModelChoiceField(
        label="Тип работ",
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=TypeRepair.objects.all()
    )
    status = forms.ChoiceField(
        label="Статус",
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
        choices=[
            item for item in Status.choices if item[0] == 'CONFIRMED'
        ]
    )

    class Meta:
        model = Repair
        fields = (
            'description',
            'time_to_work',
            'places_to_work',
            'type_repair',
            'status',
        )
