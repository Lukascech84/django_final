from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Uzivatel(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name='Jméno uživatele', help_text='Zadejte své jméno')
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení uživatele', help_text='Zadejte své příjmení')
    nickname = models.CharField(max_length=50, verbose_name='Přezdívka uživatele', help_text='Zadejte svou přezdívku')
    telefon = PhoneNumberField(null=False, blank=False, unique=True, region='CZ')
    email = models.EmailField(max_length=254, verbose_name='Email uživatele', help_text='Zadejte svůj email', unique=True)
    datum_narozeni = models.DateField(verbose_name='Datum narození', help_text='Zadejte své datum narození')
    fotka = models.ImageField(upload_to='img/users/', default='img/users/default.png')
    bio = models.CharField(max_length=300, verbose_name='Bio', help_text='Napište něco o sobě', null=False, blank=False, default="")

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Uživatel'
        verbose_name_plural = 'Uživatelé'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'

class Zanr(models.Model):
    nazev = models.CharField(max_length=20, verbose_name='Název žánru', help_text='Zadejte název žánru')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Žánr'
        verbose_name_plural = 'Žánry'

    def __str__(self):
        return self.nazev

class Vydavatel(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název vydavatele', help_text='Zadejte název vydavatele')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Vydavatel'
        verbose_name_plural = 'Vydavatelé'

    def __str__(self):
        return self.nazev

class Vyvojar(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název vývojáře', help_text='Zadejte název vývojáře')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Vývojář'
        verbose_name_plural = 'Vývojáři'

    def __str__(self):
        return self.nazev

class Hra(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název hry', help_text='Zadejte název hry')
    zanry = models.ManyToManyField(Zanr, verbose_name='Žánry')
    vyvojar = models.ManyToManyField(Vyvojar, verbose_name='Vývojáři')
    vydavatel = models.ManyToManyField(Vydavatel, verbose_name='Vydavatelé')
    fotka = models.ImageField(upload_to='img/games/', default='img/games/default.png')
    datum_vydani = models.DateField(verbose_name='Datum vydání', help_text='Zadejte datum vydání hry')
    cena = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Cena')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Hra'
        verbose_name_plural = 'Hry'

    def __str__(self):
        return self.nazev
