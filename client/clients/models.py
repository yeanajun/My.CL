from djongo import models

class Category_log(models.Model):
    _id = models.ObjectIdField()
    user_id = models.IntegerField(null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(null=True, max_length=20)
    subject = models.CharField(null=True, max_length=20)
    achievement = models.CharField(null=True, max_length=20)
    site = models.CharField(null=True, max_length=20)
    jobdam = models.CharField(null=True, max_length=20)
    pilgi = models.CharField(null=True, max_length=20)
    jindo = models.CharField(null=True, max_length=20)

    objects = models.DjongoManager()