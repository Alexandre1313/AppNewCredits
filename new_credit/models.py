from django.db import models


class Base(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Usuario(Base):
    usuario = models.CharField('Nome', max_length=50)
    senha = models.CharField('Password', max_length=15)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.usuario


class Divida(Base):
    usuario = models.ForeignKey(Usuario, related_name='Dívidas', on_delete=models.CASCADE)
    data_vencimento = models.DateField('Vencimento')
    divida = models.DecimalField('Saldo devedor', max_digits=15, decimal_places=2)

    class Meta:
        verbose_name = 'Dívida'
        verbose_name_plural = 'Dividas'

    def __str__(self):
        return f'A dívida de {self.usuario} é de {self.divida}'


class Consulta(Base):
    id_usuario = models.ForeignKey(Usuario, related_name='Consultas', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return self.id_usuario
