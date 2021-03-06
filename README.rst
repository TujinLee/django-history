NOTE: https://github.com/arteria/django-history is no longer maintained!


Django History
============

django-history is a reusable Django app showing the history of object based events. This is also "known" as timeline.  

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-history

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/arteria/django-history.git#egg=history

TODO: Describe further installation steps (edit / remove the examples below):

In settings.py add ``history`` to your ``INSTALLED_APPS`` and define ``HISTORY_DISPLAY_TYPES``.

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'history',
    )
    
    HISTORY_DISPLAY_TYPES = () 
    # Example: 
    # HISTORY_DISPLAY_TYPES = (('history/hello_world.html', 'Hello World'), 
    #                          ('history/hello_user.html',  'Hello User'), 
    #                         )
	
	
Add the ``history`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^history/', include('history.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load history_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py syncdb


Usage
-----

Follow these steps to set up your history (timeline).

+ Create templates in ``history/<template name>.html`` 
+ Register the templates in ``HISTORY_DISPLAY_TYPES`` defined in your project settings.


History event rendering
~~~~~~~~~~~~~~~~~~~~~~~

The objects is passed as ``obj`` to the template defined in ``HISTORY_DISPLAY_TYPES``. In our "Hello User" template (history/hello_user.html), it's possible to access to the user's username by using ``{{ obj.username }}``. 

Settings
~~~~~~~~
+ HISTORY_USE_UTC = False (default is False), set to True to use datetime.utcnow() instead of datetime.now() in history rendering.
+ HISTORY_ORDER_BY = 'publish_timestamp' (or 'event_timestamp', default is 'publish_timestamp') 

History and change log
----------------------

Development
~~~~~~~~~~


0.1.1
~~~~~

+ ``showAll`` methode showing the past and upcomming events in one stream.
+ Fixed Manifest.in
+ Added ``is_sticky`` a flag that holds events on top of the timeline. Please migrate manually. Thanks.
+ Added ``generic_flag`` a integer attribute for generic 3rd party usage. Please migrate manually. Thanks.
+ UTC support, utcnow vs. now
+ New wrapper to control amount of events through template tag.
+ Stricky in ordering
+ Ordering by publish or event timestamp for past events.
+ showUpcomming, methods for showing upcomming events, templage tag ``showUpcomming``.
+ User ``request| ... :'auto| ... '`` to automatically take the username from the request object.

0.1.0
~~~~~

+ Initial version

TODOs and know issues
----

+ Potect private timelines
+ Allow sticky events (highlight, keep them on top) - seems broken
+ moments.js https://github.com/moment/moment/
+ AJAX loading of next page
+ Settings support (load n events per page)
+ displayHistoryEvent(...)
+ Settings for default amount of events (10 currently)
+ Add template for upcomming events
+ Send signal when a new event is added to the history
+ Ordering on past events (HISTORY_ORDER_BY) in utils.py  fx: showAll()
+ Currently it's anonymous or personalizerd history timelines. Next step should be mixed (place anonyoums events in personalized timelines).

License
-------

Django History is brought to you by arteria GmbH, licensed under the MIT License (MIT). 

Contribute
----------

If you want to contribute to this project, the best way is to send a pull request. Thanks in advance.


