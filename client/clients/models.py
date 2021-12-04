from djongo import models

class Category(models.Model):
    grade = models.CharField(null=True, max_length=20)
    subject = models.CharField(null=True, max_length=20)
    achievement = models.CharField(null=True, max_length=20)
    site = models.CharField(null=True, max_length=20)
    tag_jobdam = models.CharField(null=True, max_length=20)
    tag_pilgi = models.CharField(null=True, max_length=20)
    tag_jindo = models.CharField(null=True, max_length=20)
    tag_achivement = models.CharField(null=True, max_length=20)

    class Meta:
        abstract = True

class Category_log(models.Model):
    _id = models.ObjectIdField()
    user_id = models.IntegerField(null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    
    category = models.ArrayField(
        model_container=Category
    )
    
    objects = models.DjongoManager()

class Recommendation_log(models.Model):
    _id = models.ObjectIdField()
    user_id = models.IntegerField(null=True)
    