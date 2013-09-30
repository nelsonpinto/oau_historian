from django.db import models

class Controller(models.Model):
	pid = models.CharField(max_length=128)
	scan_cycle = models.IntegerField()
	status = models.CharField(max_length=128)
	pub_date = models.DateTimeField()
	
	def __unicode__(self):
		return self.pid

class Connection(models.Model):
	connect = models.CharField(max_length=128)
	gate = models.IPAddressField()
	host = models.IPAddressField()
	server = models.CharField(max_length=128)
	channel = models.CharField(max_length=128)
	device = models.CharField(max_length=128)
	sampletime = models.IntegerField()
	
	def __unicode__(self):
		return self.connect

class Tag(models.Model):
	connect = models.ForeignKey(Connection)
	name = models.CharField(max_length=128)
	datatype = models.CharField(max_length=128)
	snapshot = models.CharField(max_length=128)
	history = models.CharField(max_length=128)
	source = models.CharField(max_length=128)
	prefix = models.CharField(max_length=128)
	history_table = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.name

class Snapshot(models.Model):
	name = models.CharField(max_length=128)
	value = models.CharField(max_length=128)
	quality = models.CharField(max_length=128)
	pub_date = models.DateTimeField()
	history = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.name

class History(models.Model):
	name = models.CharField(max_length=128)
	value = models.CharField(max_length=128)
	quality = models.CharField(max_length=128)
	pub_date = models.DateTimeField()
	
	def __unicode__(self):
		return self.name

class Trendconfig(models.Model):

   	SEL_RANGE = (("Date", "Fecha"),("Range", "Rango"))
   	DATE_CHOICES = (("Day", "Dia"),("Month", "Mes"))
	
	sel_range = models.CharField(max_length=128, choices=SEL_RANGE, default="Fecha", help_text="Seleccione Modo Carta")	
	start_date = models.DateTimeField(help_text="Fecha Inicio Carta")
	end_date = models.DateTimeField(help_text="Fecha Termino Carta")	
	unit_date = models.CharField(max_length=128, choices=DATE_CHOICES, default="Dia", help_text="Rango Seleccione Periodo")
	date_range = models.IntegerField(help_text="Rango Unidad")	

	#def __unicode__(self):
    #    return u"%s" % (self.sel_range)

class Mensaje(models.Model):
	msg = models.CharField(max_length=128)
	href_add = models.CharField(max_length=128)
	href_add_enable = models.BooleanField(default=False)

	def __unicode__(self):
		return self.msg
