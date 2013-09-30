#encoding:utf-8

from django.shortcuts import render_to_response, render
from django.shortcuts import get_object_or_404
from django.template import Context, loader
from django.template import RequestContext

from hist.models import Controller, Connection, Tag, Snapshot, History, Trendconfig, Mensaje

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import Http404

from django.views.defaults import page_not_found as default_page_not_found 
from django.views.defaults import server_error as default_server_error

import datetime

from django.db import models
from django import forms
from django.forms import ModelForm, Textarea, Select
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


class ConnectForm(ModelForm):
	class Meta:
		model = Connection
		fields = ('id', 'connect', 'gate', 'host', 'server', 'channel', 'device', 'sampletime')
        widget = {'gate': Textarea(attrs={'cols': 80, 'rows': 20}),}

class EditConnectForm(ModelForm):
	class Meta:
		model = Connection

class TagForm(ModelForm):
	class Meta:
		model = Tag

class EditTagForm(ModelForm):
	class Meta:
		model = Tag

class TrendForm(ModelForm):
	class Meta:
		model = Trendconfig

class EditTrendForm(ModelForm):
	class Meta:
		model = Trendconfig


def page_not_found(request, template='404.html'):
	return default_page_not_found(request, template=template)

def server_error(request, template='500.html'):
	return default_server_error(request, template=template)

def home(request):
    if request.user.is_anonymous():
        user = 'AnonymousUser'
    else:
        user = request.user.username
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def index(request):
	qs = User.objects.all().order_by('username','first_name','last_name')
	return render_to_response('hist/index.html', locals(), context_instance=RequestContext(request))

def user_signin(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/user/private/')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            user = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=user, password=password)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return HttpResponseRedirect('/user/private/')
                else:
                    return render_to_response('user_noactive.html', context_instance=RequestContext(request))
            else:
                return render_to_response('user_nouser.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('user_signin.html',{'formulario':formulario}, context_instance=RequestContext(request))

def user_createaccount(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('user_createaccount.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/user/signin/')
def user_private(request):
    user = request.user
    return render_to_response('user_private.html',{'user':user}, context_instance=RequestContext(request))

@login_required(login_url='/user/signin/')
def user_signout(request):
    logout(request)
    return HttpResponseRedirect('/')

def controller_index(request):
	qs = Controller.objects.all().order_by('status', 'scan_cycle', 'pid', 'pub_date')
	return render_to_response('hist/controller.html', locals(), context_instance=RequestContext(request))






def connect_index(request):
	qs = Connection.objects.all().order_by('id','connect','gate','host','server','channel','device','sampletime')
	return render_to_response('hist/connect.html', locals(), context_instance=RequestContext(request))

def connect_add(request):
	if request.method == 'POST':
		connect_form = ConnectForm(request.POST, request.FILES)
		if connect_form.is_valid():
			connect_form.save()
			return HttpResponseRedirect('/hist/connect/')
	else:
		connect_form = ConnectForm()
	return render_to_response("hist/connect_add.html", {'connect_form': connect_form}, context_instance=RequestContext(request))

def connect_edt(request, id):
	connect_edit = get_object_or_404(Connection, pk=id)
	if request.method == 'POST':
		edit_connect_form = EditConnectForm(request.POST, instance=connect_edit)
		if edit_connect_form.is_valid():
			edit_connect_form.save()
			return HttpResponseRedirect(reverse('hist.views.connect_index'))
	else:
		edit_connect_form = EditConnectForm(instance=connect_edit)
	return render_to_response("hist/connect_edit.html", {'edit_connect_form': edit_connect_form}, context_instance=RequestContext(request))

def connect_rem(request, id):
	connect_remove = get_object_or_404(Connection, pk=id)
	connect_remove.delete()
	return HttpResponseRedirect(reverse('hist.views.connect_index'))

def tag_index(request):
	qs = Tag.objects.all().order_by('id','connect','name','datatype','snapshot','history','source','prefix','history_table')
	return render_to_response('hist/tag.html', locals(), context_instance=RequestContext(request))

def tag_add(request):
	if request.method == 'POST':
		tag_form = TagForm(request.POST)
		if tag_form.is_valid():
			tag_form.save()
			return HttpResponseRedirect('/hist/tag/')
	else:
		tag_form = TagForm()
	return render_to_response("hist/tag_add.html", {'tag_form': tag_form}, context_instance=RequestContext(request))

def tag_edt(request, id):
	tag_edit = get_object_or_404(Tag, pk=id)
	if request.method == 'POST':
		edit_tag_form = EditTagForm(request.POST, instance=tag_edit)
		if edit_tag_form.is_valid():
			edit_tag_form.save()
			return HttpResponseRedirect(reverse('hist.views.tag_index'))
	else:
		edit_tag_form = EditTagForm(instance=tag_edit)
	return render_to_response("hist/tag_edit.html", {'edit_tag_form': edit_tag_form}, context_instance=RequestContext(request))

def tag_rem(request, id):
	tag_remove = get_object_or_404(Tag, pk=id)
	tag_remove.delete()
	return HttpResponseRedirect(reverse('hist.views.tag_index'))

def snapshot_index(request):
	qs = Snapshot.objects.all().order_by('id','name','value','quality','pub_date','history')
	return render_to_response('hist/snapshot.html', locals(), context_instance=RequestContext(request))

def ObjectoNoExiste(request):
	qs = Mensaje.objects.all().order_by('msg','href_add','href_add_enable')
	return render_to_response('Object-Does-NotExist.html', locals(), context_instance=RequestContext(request))

def trend_index(request, id):
	GOOGLE_API_KEY = 'ABQIAAAAx8EDhBKqhHVdSgf-TKpFDhTiR8xSyr-fbOquv0bi5tyHH-IasRSbnq-T_qzo1sSpERPweyk465UsIw'
	today = datetime.datetime.today()

	try:
		qsx = Trendconfig.objects.get(pk=id)
	except ObjectDoesNotExist:
		p = get_object_or_404(Mensaje, pk=1)   #si no hay mensaje por primera vez, falla
		p.msg = 'No Existe Definicion Carta Historica'
		p.href_add = ('/hist/trend/add/%s' %id)
		p.href_add_enable = True
		p.save()
		return HttpResponseRedirect('/hist/objects/')

	if qsx.sel_range == 'Date':
		start_date = qsx.start_date
		end_date = qsx.end_date
		
	elif qsx.sel_range == 'Range':
		date_range = qsx.date_range
		unit_date = qsx.unit_date
		last = today - datetime.timedelta(days = date_range)	#no se puede reemplazar el argumento days por unit_date
		start_date = last
		end_date = today

	snapshot = Snapshot.objects.get(pk = id)
	name = snapshot.name
	qs = History.objects.filter(name=name, pub_date__range = (start_date, end_date)).order_by('pub_date', 'value')
		
	return render_to_response('hist/trend_index.html', locals(), context_instance=RequestContext(request))


def trend_add(request, id):
	if request.method == 'POST':
		trend_form = TrendForm(request.POST)
		if trend_form.is_valid():
			trend_id = trend_form.save(commit=False)
			trend_id.id = id
			trend_id.save()
			return HttpResponseRedirect('/hist/snapshot/')
	else:
		trend_form = TrendForm()
	return render_to_response("hist/trend_add.html", {'trend_form': trend_form}, context_instance=RequestContext(request))


def trend_edt(request, id):
	try:
		trend_edit = Trendconfig.objects.get(pk=id)
	except ObjectDoesNotExist:
		p = get_object_or_404(Mensaje, pk=1)
		p.msg = 'No Existe Definicion Carta Historica'
		p.href_add = ('/hist/trend/add/%s' %id)
		p.href_add_enable = True
		p.save()#update_field=['msg']
		return HttpResponseRedirect('/hist/objects/')

	if request.method == 'POST':
		edit_trend_form = EditTrendForm(request.POST, instance=trend_edit)
		if edit_trend_form.is_valid():
			edit_trend_form.save()
			return HttpResponseRedirect('/hist/snapshot/%s' % trend_edit.id)
	else:
		edit_trend_form = EditTrendForm(instance=trend_edit)

	return render_to_response("hist/trend_edit.html", {'edit_trend_form': edit_trend_form}, context_instance=RequestContext(request))


def trend_rem(request, id):
	trend_remove = get_object_or_404(Trendconfig, pk=id)
	trend_remove.delete()
	return HttpResponseRedirect('/hist/snapshot/')












