from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class PartnerOrg(models.Model):
    """
    PartnerOrg model
    """
    id = models.AutoField(primary_key=True, help_text='Unique Id to identify a partner')
    name = models.CharField(max_length=255, help_text='Name of the partner primary org')
    user = models.ManyToManyField(User, help_text='Reference to users table')
    primary_org_id = models.CharField(max_length=255, help_text='Org Id', unique=True)
    is_org_rebranded = models.BooleanField(default=True, help_text='Is Org Rebranded')
    currency = models.CharField(max_length=5, help_text='Fyle Currency', null=True)
    cluster_domain = models.CharField(max_length=255, help_text='Fyle Cluster domain')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at datetime')
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at datetime')

    class Meta:
        db_table = 'partner_orgs'
