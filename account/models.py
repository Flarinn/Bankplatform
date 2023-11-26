from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Person(models.Model):
    Fam = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Rank = models.CharField(null=True, max_length=200)
    Birthday = models.DateField()
    PassportSeria = models.CharField(max_length=15)
    PassportCode = models.IntegerField()
    Kem_Vid = models.CharField(max_length=140)
    Date_Vid = models.DateField()

    def __str__(self):
        return self.Fam + ' ' + self.Name + ' ' + self.LastName


class Company(models.Model):
    Name = models.CharField(max_length=200, primary_key=True)
    INN = models.IntegerField()
    OGRN = models.IntegerField(null=True)

    def __str__(self):
        return self.Name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100, null=True)
    LastName = models.CharField(max_length=100, null=True)
    Fam = models.CharField(max_length=100, null=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True)
    ROLE_CHOICES = (
        ("BANK", "BANK"),
        ("AGENT", "AGENT"),
        ("PLATFORM", "PLATFORM"),
    )
    role = models.CharField(max_length=9,
                            choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        if (self.Fam==None) and (self.LastName==None) and  (self.Name==None):
            return self.user.username
        return self.Fam + ' ' + self.Name + ' ' + self.LastName + ' ' + self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class BeneficiarCompany(models.Model):
    Name = models.CharField(max_length=200, primary_key=True)
    INN = models.IntegerField()
    OGRN = models.IntegerField(null=True,blank=True)
    Vlad = models.ForeignKey(Person, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.Name


class PrincipalCompany(models.Model):
    Name = models.CharField(max_length=200, primary_key=True)
    INN = models.IntegerField()
    OGRN = models.IntegerField(null=True)
    Vlad = models.ForeignKey(Person, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.Name


class Application(models.Model):
    ProductType = models.CharField(max_length=400,default='bg',blank=True)
    Description = models.CharField(max_length=800,null=True,blank=True)
    Sum = models.CharField(max_length=200)
    Percent = models.IntegerField(null=True, default=4,blank=True)
    Months = models.IntegerField()
    Link = models.CharField(max_length=200)  # ссылка на госзакупку
    PrincipalCompany = models.ForeignKey(PrincipalCompany, on_delete=models.CASCADE)
    BeneficiarCompany = models.ForeignKey(BeneficiarCompany, on_delete=models.CASCADE)
    WorkerId = models.ManyToManyField(Profile, related_name="applications",blank=True)
    STATUS_CHOICES = (
        ("Отказано", "Отказано"),
        ("На заполнении у агента", "На заполнении у агента"),
        ("На проверке у сотрудника платформы", "На проверке у сотрудника платформы"),
        ("На рассмотрении у банка", "На рассмотрении у банка"),
        ("На согласовании у агента", "На согласовании у агента"),
        ("Выдано", "Выдано")
    )
    Status = models.CharField(max_length=50, null=True,choices=STATUS_CHOICES)
    #UstavDoc = models.FileField(upload_to='files', null=True,blank=True)
    #Buhotch = models.FileField(upload_to='filess', null=True, blank= True)
    def __str__(self):
        return  ' Сумма: ' + str(self.Sum) + ' Кол-во месяцев: ' + str(
            self.Months) + ' Принципал: ' + str(self.PrincipalCompany) + ' Бенефициар: ' + str(self.BeneficiarCompany)

