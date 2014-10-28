from django.db import models


class Host(models.Model):
	name = models.CharField(max_length=200, blank=True)
	
	def __str__(self):
		return self.name

class VarGroup(models.Model):
	name = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name

class VarKey(models.Model):
	var_group = models.ForeignKey(VarGroup)
	host = models.ForeignKey(Host)

	def __str__(self):
		return self.host.name + ' / ' + self.var_group.name

class VarName(models.Model):
	var_group = models.ForeignKey(VarGroup)
	name = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.var_group.name + ' / ' + self.name

class VarValue(models.Model):
	var_key = models.ForeignKey(VarKey, db_column='var_key')
	var_name = models.ForeignKey(VarName)
	value = models.CharField(max_length=255)

	def __str__(self):
		return self.var_key.host.name + ' / ' + self.var_key.var_group.name + ' / ' + self.var_name.name + ' / ' + self.value
