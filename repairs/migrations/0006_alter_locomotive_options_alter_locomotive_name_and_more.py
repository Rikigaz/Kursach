# Generated by Django 4.1.3 on 2022-12-18 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0005_add_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locomotive',
            options={'verbose_name': 'Марка', 'verbose_name_plural': 'Марки'},
        ),
        migrations.AlterField(
            model_name='locomotive',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Наименование Марки Авто'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='locomotive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='locomotive_repairs', to='repairs.locomotive', verbose_name='Марка Автомобиля'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='status',
            field=models.CharField(choices=[('CREATED', 'Новая заявка от клиента'), ('CONFIRMED', 'Подтверждена автотехником'), ('READY_TO_WORK', 'Готова к работе'), ('PROGRESS', 'В работе'), ('VERIFICATION', 'Ремонт выполнен'), ('TESTS', 'На тестировании'), ('RE_REPAIR', 'На доработку')], default='CREATED', max_length=20),
        ),
    ]
