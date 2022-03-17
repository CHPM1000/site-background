from django.db import migrations, models

class Migration(migrations.migration):
    initial = True

    class Produto(models.model):
        nome = models.CharField('Nome', max_length=40)
        preço = models.DecimalField('Preço', decimal_places=2, max_digits=8)
        estoque = models.IntegerField('Quantidade em estoque')