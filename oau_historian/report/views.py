from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader
from django.template import RequestContext

from hist.models import History, Snapshot, Tag

from django.http import HttpResponse
from django.http import Http404

import datetime

from django.views.defaults import page_not_found as default_page_not_found 
from django.views.defaults import server_error as default_server_error

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4, letter

def report_index(request):
	qs = Tag.objects.all().order_by('name','datatype','source','id')
	return render_to_response('report/reporte.html', locals(), context_instance=RequestContext(request))

def pdf_response(nombre):
	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'inline; filename={0}'.format(nombre) #attachment para guardar directamente
	return response
	
def genera_pdf(respuesta, data_model):
	p = canvas.Canvas(respuesta)
	p.setPageSize(letter)
	p.setFont('Helvetica-Bold',16)
	p.drawString( 90, 750, 'OpenAutomation')
	
	p.setFont('Helvetica-Bold',14)
	p.drawString( 90, 730, 'Tag:')

	p.setFont('Helvetica-Bold',14)
	p.drawString( 90, 710, 'Operador: Nelson Pinto')

	p.setFont('Helvetica-Bold',14)
	p.drawString( 90, 690, 'Rango de Fecha: 01-03-13-->01-06-13')
	
	x = 100
	y = 680
	pos = 0
	
	for data_models in data_model:
		p.setFont('Helvetica',11)
		pos = pos + 1
		diff_x = 10
		diff_y = pos*12
		p.drawString( x + (2*diff_x), y - diff_y, str(data_models.name))
		p.drawString( x + (10*diff_x), y - diff_y, data_models.value)
		p.drawString( x + (14*diff_x), y - diff_y, data_models.quality)
		p.drawString( x + (18*diff_x), y - diff_y, str(data_models.pub_date))
	p.showPage()
	p.save()

def report_generar(request,id):
	tag_instance = Tag.objects.get(pk = id)
	name = tag_instance.name
	history_tag = History.objects.filter(name=name).order_by('name','value','quality','pub_date')
	respuesta = pdf_response('reporte_history_tag.pdf')
	genera_pdf(respuesta, history_tag)
	return respuesta






