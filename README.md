When developing a web app in Python, it is often to use a framework. A framework "is a code library that makes a developer's life easier when building reliable, scalable, and maintainable web applications" by providing reusable code or extensions for common operations. There are a number of frameworks for Python, including Flask, Tornado, Pyramid, and Django.

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

https://flask.palletsprojects.com/en/1.1.x/

Typical tasks involved might include:
1. Flask startup and configuration

   from flask import Flask, request, render_template, url_for, redirect, session, flash, g
   
   import os
   host = os.getenv("IP", "127.0.0.1")
   port = int(os.getenv("PORT", "5000"))

2. Designing requests

   @app.route('/o_rpt', methods=['POST', 'GET'])
   if request.method == 'GET':
   if request.method == 'POST':	

3. Connecting the database in Flask (useing sqlite3 as example)

   import sqlite3 as db
   import pandas as pd
   import pandas.io.sql as pd_sql
   conn=db.connect(db_str, timeout=10)
   dataframe=pd_sql.read_sql(query, conn)
   conn.close()
 
4. Rendering html page 

   dataframe_html= dataframe.to_html()   
   return render_template('o_rpt.html', dataframe_html= dataframe_html)
 
5. templates design (Jinja2 is a modern day templating language for Python developers)
  https://jinja.palletsprojects.com/en/2.11.x/

   {% extends 'base.html' %} {% block content %}
   -- REPORT_VIEW -
   {% for key in tables_dict %}
   {{key}}
   {{ tables_dict[key]|safe }} {% endfor %}
   {% endblock %}
