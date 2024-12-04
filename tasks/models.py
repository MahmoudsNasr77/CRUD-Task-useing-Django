from django.db import models
categories =[
    ('عمل','عمل'),
    ('دراسة','دراسة'),
    ('شخصي','شخصي'),
    ('غير محدد','غير محدد'),
]
class task(models.Model):
    title=models.CharField(max_length=250)
    descrption=models.TextField(max_length=5000)
    category=models.CharField(max_length=100,choices=categories)
    isCompleted=models.BooleanField(default=False)
    dueDate=models.DateField(blank=True,null=False)
    
    
    def __str__(self):
        return self.title