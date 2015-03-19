from django.db import models

class Credentials(models.Model):
    username        = models.CharField(max_length=50)
    password        = models.CharField(max_length=50)
    description     = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.username)

class SnmpCredentials(models.Model):
    snmp_mode       = models.CharField(max_length=20)   # 'snmp1_2c' or 'snmp3'
    description     = models.CharField(max_length=200, blank=True, null=True)
    username        = models.CharField(max_length=50, blank=True, null=True)
    auth_proto      = models.CharField(max_length=30, blank=True, null=True)
    auth_key        = models.CharField(max_length=50, blank=True, null=True)
    encrypt_proto   = models.CharField(max_length=30, blank=True, null=True)
    encrypt_key     = models.CharField(max_length=50, blank=True, null=True)
    community       = models.CharField(max_length=50, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % (self.description)

class NetworkDevice(models.Model):
    device_name     = models.CharField(primary_key=True, max_length=80)
    ip_address      = models.IPAddressField()
    device_class    = models.CharField(max_length=50)
    ssh_port        = models.IntegerField(blank=True, null=True)
    api_port        = models.IntegerField(blank=True, null=True)
    vendor          = models.CharField(max_length=50, blank=True, null=True)
    model           = models.CharField(max_length=50, blank=True, null=True)
    device_type     = models.CharField(max_length=50, blank=True, null=True)
    os_version      = models.CharField(max_length=100, blank=True, null=True)
    serial_number   = models.CharField(max_length=50, blank=True, null=True)
    uptime_seconds  = models.IntegerField(blank=True, null=True)
    credentials     = models.ForeignKey(Credentials, blank=True, null=True)
    snmp_credentials = models.ForeignKey(SnmpCredentials, blank=True, null=True)
    snmp_port       = models.IntegerField(blank=True, null=True)
    cfg_file        = models.CharField(max_length=100, blank=True, null=True)
    # Timestamp when cfg_file was archived
    cfg_archive_time = models.DateTimeField(blank=True, null=True)
    # Uptime when running config last changed (from MIB = ccmHistoryRunningLastChanged)
    cfg_last_changed = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.device_name)
