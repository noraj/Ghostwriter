# Generated by Django 2.2.3 on 2019-07-26 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ghostwriter.reporting.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rolodex', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FindingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finding_type', models.CharField(help_text='Type of finding (e.g. network)', max_length=100, unique=True, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Finding type',
                'verbose_name_plural': 'Finding types',
                'ordering': ['finding_type'],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Report', help_text='Provide a meaningful title for this report - this is only seen in Ghostwriter', max_length=200, verbose_name='Title')),
                ('creation', models.DateField(auto_now_add=True, help_text='Date the report was created', verbose_name='Creation Date')),
                ('last_update', models.DateField(auto_now=True, help_text='Date the report was last touched', verbose_name='Creation Date')),
                ('complete', models.BooleanField(default=False, help_text='Mark the report as complete', verbose_name='Completed')),
                ('archived', models.BooleanField(default=False, help_text='Mark the report as archived', verbose_name='Archived')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rolodex.Project')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
                'ordering': ['-creation', '-last_update', 'project'],
            },
        ),
        migrations.CreateModel(
            name='Severity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.CharField(help_text='Severity rating (e.g. High, Low)', max_length=100, unique=True, verbose_name='Severity')),
                ('weight', models.IntegerField(default=1, help_text='Used for custom sorting in reports. Lower numbers are more severe.', verbose_name='Severity Weight')),
            ],
            options={
                'verbose_name': 'Severity rating',
                'verbose_name_plural': 'Severity ratings',
                'ordering': ['severity'],
            },
        ),
        migrations.CreateModel(
            name='ReportFindingLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a title for this finding that will appear in the reports', max_length=200, verbose_name='Title')),
                ('position', models.IntegerField(default=1, help_text='Set this findings weight to adjust where it appears in the report compared to other findings with the same Severity rating', verbose_name='Report Position')),
                ('affected_entities', models.TextField(blank=True, help_text='Provide a list of the affected entities (e.g. domains, hostnames, IP addresses)', null=True, verbose_name='Affected Entities')),
                ('description', models.TextField(blank=True, help_text='Provide a description for this finding that introduces it', null=True, verbose_name='Description')),
                ('impact', models.TextField(blank=True, help_text='Describe the impact of this finding on the affected entities', null=True, verbose_name='Impact')),
                ('mitigation', models.TextField(blank=True, help_text='Describe how this finding can be resolved or addressed', null=True, verbose_name='Mitigation')),
                ('replication_steps', models.TextField(blank=True, help_text='Provide an explanation for how the reader may reproduce this finding', null=True, verbose_name='Replication Steps')),
                ('host_detection_techniques', models.TextField(blank=True, help_text='Describe how this finding can be detected on an endpoint - leave blank if this does not apply', null=True, verbose_name='Host Detection Techniques')),
                ('network_detection_techniques', models.TextField(blank=True, help_text='Describe how this finding can be detected on a network - leave blank if this does not apply', null=True, verbose_name='Network Detection Techniques')),
                ('references', models.TextField(blank=True, help_text='Provide solid references for this finding, such as links to reference materials, tooling, and white papers', null=True, verbose_name='References')),
                ('complete', models.BooleanField(default=False, help_text='Is the finding ready for review', verbose_name='Completed')),
                ('assigned_to', models.ForeignKey(blank=True, help_text='Assign the task of editing this finding to a specific operator - defaults to the operator that added it to the report', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('finding_type', models.ForeignKey(help_text='Select a finding category that fits', null=True, on_delete=django.db.models.deletion.PROTECT, to='reporting.FindingType')),
                ('report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reporting.Report')),
                ('severity', models.ForeignKey(help_text='Select a severity rating for this finding that reflects its role in a system compromise', null=True, on_delete=django.db.models.deletion.PROTECT, to='reporting.Severity')),
            ],
            options={
                'verbose_name': 'Report link',
                'verbose_name_plural': 'Report links',
                'ordering': ['report', 'severity__weight', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Finding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a title for this finding that will appear in the reports', max_length=200, unique=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, help_text='Provide a description for this finding that introduces it', null=True, verbose_name='Description')),
                ('impact', models.TextField(blank=True, help_text='Describe the impact of this finding on the affected entities', null=True, verbose_name='Impact')),
                ('mitigation', models.TextField(blank=True, help_text='Describe how this finding can be resolved or addressed', null=True, verbose_name='Mitigation')),
                ('replication_steps', models.TextField(blank=True, help_text='Provide an explanation for how the reader may reproduce this finding', null=True, verbose_name='Replication Steps')),
                ('host_detection_techniques', models.TextField(blank=True, help_text='Describe how this finding can be detected on an endpoint - leave blank if this does not apply', null=True, verbose_name='Host Detection Techniques')),
                ('network_detection_techniques', models.TextField(blank=True, help_text='Describe how this finding can be detected on a network - leave blank if this does not apply', null=True, verbose_name='Network Detection Techniques')),
                ('references', models.TextField(blank=True, help_text='Provide solid references for this finding, such as links to reference materials, tooling, and white papers', null=True, verbose_name='References')),
                ('finding_guidance', models.TextField(blank=True, help_text='Provide notes for your team that describes how the finding is intended to be used and any details that should be provided during editing', null=True, verbose_name='Finding Guidance')),
                ('finding_type', models.ForeignKey(help_text='Select a finding category that fits', null=True, on_delete=django.db.models.deletion.PROTECT, to='reporting.FindingType')),
                ('severity', models.ForeignKey(help_text='Select a severity rating for this finding that reflects its role in a system compromise', null=True, on_delete=django.db.models.deletion.PROTECT, to='reporting.Severity')),
            ],
            options={
                'verbose_name': 'Finding',
                'verbose_name_plural': 'Findings',
                'ordering': ['severity', 'finding_type', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, upload_to=ghostwriter.reporting.models.Evidence.set_upload_destination)),
                ('friendly_name', models.CharField(help_text='Provide a simple name to be used for displaying this file in the interface and for use as a keyword for placing the file within the report', max_length=100, null=True, verbose_name='Friendly Name')),
                ('upload_date', models.DateField(auto_now=True, help_text='Date and time the evidence was uploaded', verbose_name='Upload Date')),
                ('caption', models.CharField(blank=True, help_text='Provide a caption to be used in the report output - keep it brief', max_length=200, verbose_name='Caption')),
                ('description', models.TextField(blank=True, help_text='Provide a description/explanation of the evidence that other users can see to help them understand the purpose of this evidence', max_length=500, verbose_name='Description')),
                ('finding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.ReportFindingLink')),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Evidence',
                'verbose_name_plural': 'Evidence',
                'ordering': ['finding', 'document'],
            },
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_archive', models.FileField(upload_to='')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rolodex.Project')),
            ],
            options={
                'verbose_name': 'Archived report',
                'verbose_name_plural': 'Archived reports',
                'ordering': ['project'],
            },
        ),
    ]