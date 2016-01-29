# djangogeo-website
This is a simple GeoDjango project. The admin interface is ready to use. The source code is based on [geodjango tutorial](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/tutorial/). Before to start:

* be sure to know [django](https://docs.djangoproject.com/en/1.8/intro/) and [geodjango](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/tutorial/) fundamentals.
* This webapp is built with a PostgreSQL database and the PostGis extension; be sure to check the [requirements](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/install/postgis/).
* This Django project is powered by [OpenShift](www.openshift.com), using a modified version of this [guide](http://stackoverflow.com/questions/26871381/deploying-a-local-django-app-using-openshift).
* You could modify the `SECRET_KEY` variable from the file `secrets.txt`.
* Before to deploy in production remember to check security issues: `python manage.py check --deploy` (see also the [related docs](https://docs.djangoproject.com/en/1.8/ref/django-admin/#check-appname-appname)).

For a quick-start and some tips about installation, see also my [wiki](https://github.com/trincadev/djangogeo-website/wiki) repo.
