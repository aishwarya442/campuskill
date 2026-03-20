from django.db import models
from users.models import CompanyProfile

class Role(models.Model): # Corresponds to Job
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='roles')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    package = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    form_url = models.URLField(blank=True, null=True) # If they apply externally
    
    def __str__(self):
        return f"{self.title} at {self.company.name}"

class SelectionCriteria(models.Model):
    role = models.OneToOneField(Role, on_delete=models.CASCADE, related_name='criteria')
    min_cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    allowed_departments = models.CharField(max_length=255, blank=True, null=True) # e.g. "CSE, ECE"
    other_requirements = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Criteria for {self.role.title}"
