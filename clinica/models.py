from django.db import models
from django.core.validators import RegexValidator

class Medico(models.Model):
    ESCPECIALIDADES = [
        ('PED', 'Pediatra'),
        ('CAR', 'Cardiologista'),
        ('NEU', 'Neurologista'),
        ('CLG', 'Clínico Geral'),
    ]
    nome = models.CharField(max_length=255)
    especialidade = models.CharField(max_length=3, choices=ESCPECIALIDADES)
    crm = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{2}/\d{5}$', message='Formato do CRM inválido. Use XX/XXXXX')])
    email = models.EmailField(max_length=255, blank=True, null=True )

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"

class Consulta(models.Model):
    STATUS = [
        ('AGE', 'Agendado'),
        ('REA', 'Realizado'),
        ('CAN', 'Cancelado'),
    ]
    paciente = models.CharField(max_length=255)
    data = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS)

    def __str__(self):
        return f"{self.paciente}: {self.medico} - {self.status}: {self.data}"