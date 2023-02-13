from django.db import models


class AppSetting(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='uploa11ds/')
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)


    def __str__(self):
        return self.name

class AboutUs(models.Model):

    name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    discription = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class FactFigure(models.Model):
    name = models.CharField(max_length=100)
    total_students = models.CharField(max_length=100, null=True)
    total_courses = models.CharField(max_length=100, null=True)
    total_project = models.CharField(max_length=100, null=True)
    total_teacher = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class MessageForm(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True)
    image = models.ImageField (upload_to='uploads/',null=True)

    def __str__(self):
        return self.name

class ChooseUs(models.Model):
    name = models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=100,null=True)
    icon_class = models.CharField(max_length=100,null=True)
    is_active = models.BooleanField(max_length=55, null=True, blank=True)

    def __str__(self):
        return self.name

class Collaboration(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField (upload_to='uploads/',null=True)
    link = models.URLField(max_length=200, null=True)


    def __str__(self):
        return self.name

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField (upload_to='uploads/',null=True)

    def __str__(self):
        return self.name
class Slider(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField (upload_to='uploads/',null=True)
    button_text = models.TextField(max_length=50, null=True)

    def __str__(self):
        return self.title

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField (upload_to='uploads/',null=True)
    display_order = models.IntegerField(max_length=10)
    is_active = models.BooleanField(max_length=55, null=True, blank=True)



    def __str__(self):
        return self.title


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField (upload_to='uploads/',null=True)
    views = models.IntegerField(max_length=10, null=True)
    is_active = models.BooleanField(max_length=55, null=True, blank=True)

    def __str__(self):
        return self.title


class FAQCategories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(max_length=55, null=True, blank=True)
    display_order = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=250, null=True)
    answer = models.CharField(max_length=250, null=True)
    catagory = models.ForeignKey(FAQCategories, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.question

class SocialLinks(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=200, null=True)
    link = models.URLField(max_length=200, null=True)
    is_activate = models.BooleanField(max_length=55, null=True, blank=True)

    def __str__(self):
        return self.name

class UseFullLink(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=200, null=True)
    link = models.URLField(max_length=200, null=True)
    is_activate = models.BooleanField(max_length=55, null=True, blank=True)

    def __str__(self):
        return self.name
class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=50, null=True)
    phone_number = models.CharField(max_length=20 ,null=True)
    subject = models.CharField(max_length=25, null=True)
    feedback = models.TextField(max_length=250, null=True)


    def __str__(self):
        return self.name
