from django.db import models

# Create your models here.
employees=[
    {"id":1,"name":"anu","dept":"cs","qualification":"bsc cs"},
    {"id":2,"name":"abi","dept":"ece","qualification":"btech ece"},
    {"id":1,"name":"appu","dept":"eee","qualification":"btech eee"},
    {"id":1,"name":"ramya","dept":"eee","qualification":"btech ece"},
    {"id":1,"name":"rahul","dept":"ce","qualification":"btech ce"},
]

managers=[
    {"id":1,"name":"amal","age":23},
    {"id":2,"name":"anu","age":24},
    {"id":3,"name":"muthu","age":23},
    {"id":4,"name":"shalu","age":22},
    {"id":5,"name":"sanu","age":21},
    {"id":6,"name":"faira","age":24}
]

# crud 
# age_gt=20

class Employee(models.Model):
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    qualiffic=models.CharField(max_length=100)


class Manager(models.Model):
    name=models