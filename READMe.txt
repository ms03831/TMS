pip install django (v 2.2)
pip install phonenumbers
pip install django-phonenumber-field
pip install django-location-field
pip install django-crispy-forms
pip install django-bootstrap3-datetimepicker
pip install bootstrap3_datetime
pip install django-location-field


pip install -U channels
** If installation of channels fails due to twisted, download the correct .whl file from https://www.lfd.uci.edu/~gohlke/pythonlibs/ for twisted and install it and then install channels, for futher instructions refer to this page https://stackoverflow.com/questions/29846087/microsoft-visual-c-14-0-is-required-unable-to-find-vcvarsall-bat **

pip install pypiwin32


** You might not require the following two, install other things then if it doesnt work try installing these two **
pip install docker
pip install redis

** Run redis-server from redis folder here **
pip install channels_redis

** run the following to verify redis is working with channels **
>python manage.py shell
Python 3.7.2 (default, Feb 21 2019, 17:35:59) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> import channels.layers
>>> channel_layer = channels.layers.get_channel_layer()
>>> from asgiref.sync import async_to_sync
>>> async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
>>> async_to_sync(channel_layer.receive)('test_channel')
{'type': 'hello'} <-- should be output


Good to go
