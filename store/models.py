from django.db import models


class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'lecturers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    credits = models.PositiveIntegerField(default=3)

    # ბევრი ერთთან კავშირი:
    lecturer = models.ForeignKey(
        Lecturer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses'
    )

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)

    # ბევრი ბევრთან კავშირი (Many-to-Many):
    courses = models.ManyToManyField(
        Course,
        related_name='students',
        blank=True
    )

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"