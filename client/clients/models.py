from djongo import models

class Category(models.Model):
    grade = models.CharField(blank=True, max_length=20)
    subject = models.CharField(blank=True, max_length=20)
    achievement = models.CharField(blank=True, max_length=20)
    site = models.CharField(blank=True, max_length=20)
    tag_jobdam = models.CharField(blank=True, max_length=20)
    tag_pilgi = models.CharField(blank=True, max_length=20)
    tag_jindo = models.CharField(blank=True, max_length=20)

    class Meta:
        abstract = True

class Recommendation(models.Model):
    lecture_id = models.CharField(max_length=20)
    lecture_name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class CategoryLog(models.Model):
    _id = models.ObjectIdField()
    user_id = models.IntegerField(blank=True)
    add_date = models.DateTimeField(auto_now_add=True)
    
    category = models.ArrayField(
        model_container=Category
    )
    
    objects = models.DjongoManager()

class RecommendationLog(models.Model):
    _id = models.ObjectIdField()
    user_id = models.IntegerField(blank=True)
    add_date = models.DateTimeField(auto_now_add=True)

    rec_lecture = models.ArrayField(
        model_container=Recommendation
    )

    objects = models.DjongoManager()