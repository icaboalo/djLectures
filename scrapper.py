import os
import sys
import django

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), 'lectures/')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'lectures.settings'
django.setup()

import requests
from bs4 import BeautifulSoup
from datetime import date
import datetime
from lectura.models import *

def get_lectures():
	fecha = date(2016, 1, 1)
	day = datetime.timedelta(days=1)

	fecha_final=date(2016, 12, 31)

	while fecha < fecha_final:

		url = requests.get('http://www.ciudadredonda.org/calendario-lecturas/evangelio-del-dia/?f=%s' % fecha)

		html = url.text
		status_code = url.status_code

		soup = BeautifulSoup(html, 'html.parser')
		section = soup.findAll('section')

		for lecture in section:
			type = lecture.h2.text
			text = lecture.div.text

			print(type)
			print(text)
			Lecture.objects.update_or_create(date=fecha, type=type, lecture=text)

		print(fecha)
		fecha += day

get_lectures()