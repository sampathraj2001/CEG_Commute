from django.contrib.auth.models import User
from django.db import models

CHOICE_AREA = (
    ('Arumbakkam', 'Arumbakkam'),
    ('AnnaNagar', 'AnnaNagar'),
    ('Adyar', 'Adyar'),
    ('Alwarpet', 'Alwarpet'),
    ('Alappakkam', 'Alappakkam'),
    ('AlwarThiruNagar', 'AlwarThiruNagar'),
    ('Ayyanambakkam', 'Ayyanambakkam'),
    ('BesantNagar', 'BesantNagar'),
    ('CMBT', 'CMBT'),
    ('Chrompet', 'Chrompet'),
    ('Egmore', 'Egmore'),
    ('Guindy', 'Guindy'),
    ('Iyyapanthangal', 'Iyyapanthangal'),
    ('KKNagar', 'KKNagar'),
    ('Kattupakkam', 'Kattupakkam'),
    ('Kodambakkam', 'Kodambakkam'),
    ('Kundrathur', 'Kundrathur'),
    ('Meenambakkam', 'Meenambakkam'),
    ('Maduravayal', 'Maduravayal'),
    ('Mylapore', 'Mylapore'),
    ('Mogappair', 'Mogappair'),
    ('Nandanam', 'Nandanam'),
    ('Nungambakkam', 'Nungambakkam'),
    ('Nandambakkam', 'Nandambakkam'),
    ('Nasaratpet', 'Nasaratpet'),
    ('Porur', 'Porur'),
    ('Poonamallee', 'Poonamallee'),
    ('Purasaiwalkam', 'Purasaiwalkam'),
    ('Pudupet', 'Pudupet'),
    ('Royapuram', 'Royapuram'),
    ('Ramapuram', 'Ramapuram'),
    ('Saidapet', 'Saidapet'),
    ('TNagar', 'TNagar'),
    ('Teynampet', 'Teynampet'),
    ('Thiruvanmiyur', 'Thiruvanmiyur'),
    ('Virugambakkam', 'Virugambakkam'),
    ('Vadapalani', 'Vadapalani'),
    ('Velachery', 'Velachery'),
    ('Valasaravakkam', 'Valasaravakkam'),

)
CHOICES_VEHICLE_TYPE = (
    ('Car', 'Car'),
    ('Bike', 'Bike'),
)

CHOICES_SEATS_AVAILABLE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)
CHOICES_BRANCH = (
    ('MSc_Integrated', 'MSc_Integrated'),
    ('BE_Civil', 'BE_Civil'),
    ('BE_Mechanical', 'BE_Mechanical'),
    ('BE_Biotech', 'Biotech'),
    ('BE_EEE', 'BE_EEE'),
    ('BE_ECE', 'BE_ECE'),
    ('BE_CS', 'BE_CS'),
    ('BE_IT', 'BE_IT'),
    ('BE_Industrial', 'BE_Industrial'),
    ('BE_Manufacturing', 'BE_Manufacturing'),
    ('BE_Material_Science', 'BE_Material_Science')
)
CHOICES_CAMPUS = (
    ('CEG', 'CEG'),
    ('ACT', 'ACT'),
    ('SAP', 'SAP'),
)
CHOICES_BLOOD_GROUP = (
    ('B+', 'B+'),
    ('A+', 'A+'),
    ('O+', 'O+'),
    ('AB+', 'AB+'),
    ('A1B+', 'A1B+'),
    ('B-', 'B-'),
    ('A-', 'A-'),
    ('O-', 'O-'),
    ('AB-', 'AB-'),
    ('A1B-', 'A1B-'),
)


class Details(models.Model):
    Name = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100, choices=CHOICES_BRANCH)
    RollNumber = models.CharField(max_length=10)
    Campus = models.CharField(max_length=3, choices=CHOICES_CAMPUS)
    BloodGroup = models.CharField(max_length=7, choices=CHOICES_BLOOD_GROUP)
    PhoneNumber = models.CharField(max_length=13)
    Address = models.CharField(max_length=255, choices=CHOICE_AREA)
    ReferenceID = models.CharField(max_length=15)
    Email = models.EmailField()
    ValidUntil = models.DateField()
    User1 = models.ForeignKey(User, on_delete=models.CASCADE)
    # Gender = models.CharField(max_length=5)

    def __str__(self):
        return str(self.Name)


class VolunteerArea(models.Model):
    Area = models.CharField(max_length=50, choices=CHOICE_AREA)

    def __str__(self):
        return str(self.Area)


class Volunteer(models.Model):
    RollNumber = models.ForeignKey(Details, on_delete=models.CASCADE)
    VehicleNumber = models.CharField(max_length=10)
    VehicleType = models.CharField(max_length=5, choices=CHOICES_VEHICLE_TYPE)
    SeatsAvailable = models.CharField(max_length=1, choices=CHOICES_SEATS_AVAILABLE)
    Status = models.BooleanField()
    HomeArea = models.ForeignKey(VolunteerArea, on_delete=models.CASCADE)
    User1 = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.RollNumber)


class StudentArea(models.Model):
    Area = models.CharField(max_length=50, choices=CHOICE_AREA)

    def __str__(self):
        return str(self.Area)


class Student(models.Model):
    RollNumber = models.ForeignKey(Details, on_delete=models.CASCADE)
    # Gender = models.CharField(max_length=5)
    HomeArea = models.ForeignKey(StudentArea, on_delete=models.CASCADE)
    User1 = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.RollNumber)


class AvailableVolunteer(models.Model):
    Volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    ts = models.TimeField(auto_now_add=True)
    PickupArea = models.CharField(max_length=50, choices=CHOICE_AREA)
    Note = models.CharField(max_length=100)
    User1 = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Volunteer)


class Request(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    StudentArea = models.ForeignKey(StudentArea, on_delete=models.CASCADE)
    Volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    StudentUser1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='StudentUser1')
    VolunteerUser1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='VolunteerUser1')

    def __str__(self):
        return str(self.Student)
