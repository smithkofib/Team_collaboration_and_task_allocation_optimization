# team_task_allocation_proj/mainApp/models.py
#-------------------------------------------#

# Create your models here. 
from django.db import models
from django.contrib.auth.admin import User

class Person(User):
    class Meta:
        proxy = True
        ordering = ("")

class Candidate(models.Model):
    """Model to store candidate information."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    #linkedin_profile = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    certificate = models.FileField(upload_to="certificates/", blank=True, null=True)
    
    GENDER_LIST = [ 
        ("Male" ,"Male"),
        ("Female" , "Female"),
    ]
    

    gender = models.CharField(max_length=50, choices=GENDER_LIST, default="Male")
    approval = models.CharField(max_length=20, default='not_approved')
    role = models.CharField(max_length=50, default='no_role')
    date_applied = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SkillCategory(models.Model):
    """Model to categorize skills (e.g., Technical, Soft Skills)."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
class Skill(models.Model):
    """Model to store different skills and qualities of a candidate."""
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
class CandidateSkill(models.Model):
    """Model to associate candidates with skills and rate their proficiency."""
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="candidate_skills")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="candidate_skills")
    
    PROFICIENCY_LEVELS = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
        ("Expert", "Expert"),
    ]
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_LEVELS, default="Beginner")
    
    def __str__(self):
        return f"{self.candidate} - {self.skill} ({self.proficiency})"
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


class WorkExperience(models.Model):
    """Model to store candidate's work experience."""
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="work_experience")
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


class Education(models.Model):
    """Model to store candidate's education background."""
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="education")
    institution_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        #return self.institution_name
        return f"{self.degree} at {self.institution_name}"


class CulturalFit(models.Model):
    """Model to evaluate if a candidate aligns with company values."""
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="cultural_fit")
    adaptability = models.BooleanField(default=False)
    teamwork = models.BooleanField(default=False)
    ethical_standards = models.BooleanField(default=False)
    leadership_potential = models.BooleanField(default=False)
    professional_attitude = models.BooleanField(default=False)

    def __str__(self):
        return f"Cultural Fit for {self.candidate}"


class CandidateAssessment(models.Model):
    """Model to store assessments based on different qualities."""
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="assessments")
    communication_skills = models.IntegerField(help_text="Rating from 1 to 10")
    problem_solving = models.IntegerField(help_text="Rating from 1 to 10")
    teamwork = models.IntegerField(help_text="Rating from 1 to 10")
    leadership = models.IntegerField(help_text="Rating from 1 to 10")
    professionalism = models.IntegerField(help_text="Rating from 1 to 10")
    emotional_intelligence = models.IntegerField(help_text="Rating from 1 to 10")
    overall_score = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Automatically calculate the overall score before saving."""
        self.overall_score = (
            self.communication_skills +
            self.problem_solving +
            self.teamwork +
            self.leadership +
            self.professionalism +
            self.emotional_intelligence
        ) / 6
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Assessment for {self.candidate}"


class CandidateFeedback(models.Model):
    """Model to store feedback from interviewers or HR."""
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="feedback")
    reviewer = models.CharField(max_length=255)
    comments = models.TextField()
    date_given = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.candidate} by {self.reviewer}"
    
class Job(models.Model):
    name = models.CharField(max_length=100)
    job_description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Departement(models.Model):
    departement_name = models.CharField(max_length=255, blank=True, null=False)
    departement_phone = models.CharField(max_length=100, blank=True, null=True)
    departement_room_number = models.IntegerField()

    def __str__(self):
        return self.departement_name
    
class Staff(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="candidate")
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='staff')
    dob = models.DateField()


    def __str__(self):
        return f"{self.candidate.first_name} {self.candidate.last_name}"
    
class StaffDepartement(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_departement')
    Departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='staff_departement')
    manager = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='departement_manager')

    def __str__(self):
        return f"{self.staff} is at the {self.Departement}"

       
class CandidateStaff(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidate_staff')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='candidate_staff')

    def __str__(self):
        return f"{self.candidate} is a staff at this {self.staff.departement.departement_name}"






