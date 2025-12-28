from django.db import models

# Create your models here.

"""
Courses:
    Title
    Description
    Image
    Access
        anyone
        email required
        purchase required 
        user required
    Status:
        published
        draft
        coming soon

"""

"""
Lessons:
        Title
        Description
        Video
        Status:same as course
"""

class PublishedStatus(models.TextChoices):
    PUBLISHED = "publish",  "Published"
    COMING_SOON = "soon" , "Coming Soon"
    DRAFT = "draft" , "Draft"

class AccessRequirement(models.TextChoices):
    ANYONE = "any" , "Anyone"
    EMAIL_REQUIRED = "email",  "Email required"

def handle_upload(instance, filename):
    return f"{filename}"
class Course(models.Model):
    pass
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=300,blank = True,null = True)
    image = models.ImageField(
        upload_to= handle_upload,
        blank=True,
        null=True
    )
    access = models.CharField(
        max_length= 5,
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length= 10,
        choices=PublishedStatus.choices,
        default=PublishedStatus.DRAFT
    )

    @property
    def is_published(self):
        return self.status == PublishedStatus.PUBLISHED