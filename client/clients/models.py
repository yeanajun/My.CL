from djongo import models

class Recommendation(models.Model):
    lecture_id = models.CharField(max_length=20)
    lecture_name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class CategoryLog(models.Model):
    _id = models.ObjectIdField()
    user_id = models.IntegerField(blank=True)
    add_date = models.DateTimeField(auto_now_add=True)
    
    grade = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    achivement = models.CharField(max_length=20)
    site = models.CharField(max_length=20)
    tag_jobdam = models.CharField(max_length=20)
    tag_pilgi = models.CharField(max_length=20)
    tag_jindo = models.CharField(max_length=20)

    objects = models.DjongoManager()

class Lecture(models.Model) :
    title = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    link = models.CharField(max_length=200)

class ReviewLog(models.Model):
    _id = models.ObjectIdField()
    user_id = models.IntegerField(blank=True)
    lecture_id = models.CharField(blank=True, max_length=30)
    lecture_title = models.CharField(blank=True, max_length=30)
    add_date = models.DateTimeField(auto_now_add=True)
    achivement = models.CharField(max_length=20)
    tag_jobdam = models.CharField(max_length=20)
    tag_pilgi = models.CharField(max_length=20)
    tag_jindo = models.CharField(max_length=20)
    lec_comment = models.CharField(max_length = 1000)

    objects = models.DjongoManager()