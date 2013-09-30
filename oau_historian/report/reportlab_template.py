#!/usr/bin/env python
# -*- coding: utf8 -*-

from reportlab.platypus import BaseDocTemplate, Paragraph, Spacer, Frame, PageTemplate, PageBreak, NextPageTemplate
from reportlab.platypus import Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.graphics.shapes import Rect
from reportlab.lib.colors import tan

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

import os
import time
from sys import modules as modules
from PIL import Image

#~                                                  D A T O S   G E N E R A L E S
#~                                                  V A R I A B L E S

PAGE_HEIGHT=29.7*cm
PAGE_WIDTH=21*cm
fuente='DejaVu'
est_=''
 
modulo_actual = modules[__name__]
 
#~ DIA DE HOY Y CONVERTIRLO A ESPAÑOL
dia=time.localtime()
mes=dia.tm_mon
mes_sp=['Enero', 'Febrero', 'Marzo',
        'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre',
        'Octubre', 'Noviembre', 'Diciembre']

hoy='%s %d' % (mes_sp[mes-1], dia.tm_year)
nombrefichero='/home/django/reportes/monobotblog.pdf'

#~                                 C O N F I G U R A N D O    L A S   F U E N T E S

pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBd', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBdIt', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-BoldOblique.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuIt', '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Oblique.ttf'))
registerFontFamily('Dejavu', normal = 'DejaVu', bold = 'DejaVuBd', italic = 'DejaVuIt', boldItalic = 'DejaVuBdIt')
 
#~                                  E S T A B L E C I E N D O   L O S   E S T I L O S
#~                                                  P A R R A F O S

est_1 = ParagraphStyle('',
                              fontName = 'DejaVu',
                              fontSize = 12,
                              alignment = 0,
                            )
 
est_2 = ParagraphStyle('',
                              fontName = 'DejaVu',
                              fontSize = 8,
                              alignment = 0,
                            )
 
est_3 = ParagraphStyle('',
                              fontName = 'DejaVu',
                              fontSize = 6,
                              alignment = 0,
                              leftIndent=cm,
                              bulletIndent=0.5*cm
                            )

#~                                                  T A B L A S
tipoTabla_moderno = TableStyle([
                ('BOTTOMPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 1),
                ('LEFTPADDING', (0,0), (-1,-1), 3),
                ('RIGHTPADDING', (0,0), (-1,-1), 3),
                ('FONT', (0,0), (-1,-1), fuente, 8),
                ('GRID', (0,0), (-1,-1), 0.01*cm, 'Black'),
                ('FONT', (0,0), (0,-1), fuente, 15),
                ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                ('ALIGN', (0,0), (0,-1), 'RIGHT'),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('SPAN',(0,0),(0,-1)),
                ('REPEAROWS', (0,0), (1,-1))
                ])
 
tipoTabla_limpia = TableStyle([
                ('BOTTOMPADDING', (0,0), (-1,-1), 0),
                ('TOPPADDING', (0,0), (-1,-1), 1),
                ('LEFTPADDING', (0,0), (-1,-1), 3),
                ('RIGHTPADDING', (0,0), (-1,-1), 3),
                ('TEXTCOLOR', (0,0), (-1,-1), 'Grey'),
                ('FONT', (0,0), (-1,-1), fuente, 10),
                ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                ('ALIGN', (-1,0), (-1,-1), 'RIGHT'),
                ('ALIGN', (1,0), (1,-1), 'CENTER')
])

#~                                                  F R A M E S
frameA4=Frame(x1=1*cm,y1=1*cm, width=PAGE_WIDTH-2*cm, height=PAGE_HEIGHT-4*cm)
frameA4_corto=Frame(x1=1*cm,y1=1*cm, width=PAGE_WIDTH-2*cm, height=PAGE_HEIGHT-10*cm)

#~                                                  C A N V A S
 
def paginaCab(canvas, hoja_moderna):
    canvas.saveState()
##    Textos
##    Cabecera
    canvas.setFont(fuente,5)
    canvas.drawRightString(PAGE_WIDTH-1*cm, PAGE_HEIGHT-1*cm, 'impresion: %s' % hoy)
    canvas.drawRightString(PAGE_WIDTH-1*cm, PAGE_HEIGHT-1.2*cm, 'monobotblog.alvarezalonso.es')
    canvas.setFont(fuente,15)
    canvas.drawString(4.7*cm, PAGE_HEIGHT-1.5*cm, 'Prueba Report Lab Hoja Primera')
    canvas.restoreState()
 
def restoPag(canvas, hoja_moderna):
    canvas.saveState()
##    Textos
##    Cabecera
    canvas.setFont(fuente,5)
    canvas.drawRightString(PAGE_WIDTH-1*cm, PAGE_HEIGHT-1*cm, 'impresion: %s' % hoy)
    canvas.drawRightString(PAGE_WIDTH-1*cm, PAGE_HEIGHT-1.2*cm, 'monobotblog.alvarezalonso.es')
    canvas.setFont(fuente,15)
    canvas.drawString(4.7*cm, PAGE_HEIGHT-1.5*cm, 'Prueba Report Lab Hoja Segunda')
    canvas.restoreState()

#~                                                  P A G I N A S

primeraPag=PageTemplate(id='1era_pag', frames=frameA4_corto, onPage = paginaCab)
siguientesPag=PageTemplate(id='resto',frames=frameA4, onPage = restoPag)
 
#~ estilos DE DOCUMENTOS

hoja_moderna=BaseDocTemplate(
        nombrefichero,
        pagesize=A4,
        pageTemplates=[primeraPag, siguientesPag],
        showBoundary=0,
        leftMargin=1*cm,
        rightMargin=-3*cm,
        topMargin=1*cm,
        bottomMargin=1*cm,
        allowSplitting=1,
        tittle=None,
        author=None,
        _pageBreakQuick=1,
        encrypt=None)

#~                      C R E A M O S   E L   C U E R P O   D E L   M E N S A J E
#~                  Y   A Ñ A D I M O S  T R E S   P A R R A F O S  Y   D O S   T A B L A S

Cuerpo=[]
p=Paragraph('Este es el texto del parrafo 1'*50, est_1)
p2=Paragraph('Este es el texto del parrafo 2'*50, est_2)
p3=Paragraph('Este es el texto del parrafo 3'*50, est_3)
 
Cuerpo.append(p)
Cuerpo.append(Spacer(0,1*cm))
Cuerpo.append(p2)
Cuerpo.append(NextPageTemplate('resto'))
Cuerpo.append(PageBreak())
Cuerpo.append(p3)
Cuerpo.append(Spacer(0,2*cm))

l_t1=[['00','10','20','30','...'],
        ['01','11','21','...','...'],
        ['02','12','...','...','-1-4'],
        ['03','...','...','-2-3','-1-3'],
        ['...','...','-3-2','-2-2','-1-2'],
        ['...','-4-1','-3-1','-2-1','-1-1']]
t1=Table(l_t1, style=tipoTabla_limpia)
Cuerpo.append (t1)
Cuerpo.append(Spacer(0,2*cm))
 
l_t2=[['Hola','Hola','Hola','Hola','Hola','Hola','Hola'],
      ['Hola','Hola','Hola','Hola','Hola','Hola','Hola'],
      ['Hola','Hola','Hola','Hola','Hola','Hola','Hola'],
      ['Hola','Hola','Hola','Hola','Hola','Hola','Hola'],
      ['Hola','Hola','Hola','Hola','Hola','Hola','Hola'],
      ['Hola','Hola','Hola','Hola','Hola','Hola','Hola']]

t2=Table(l_t2, style=tipoTabla_moderno)
Cuerpo.append (t2)

def go():
    hoja_moderna.build(Cuerpo)

if __name__ == '__main__':
    go()
