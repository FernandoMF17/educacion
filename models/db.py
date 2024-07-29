# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth
import datetime

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.extra_fields['auth_user'] = []
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')

# -------------------------------------------------------------------------
# your http://google.com/analytics id                                      
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'))

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)
# Función para convertir el texto a mayúsculas
def to_upper_case(string):
    return string.upper()


# UnidadEducativa
db.define_table('unidad_educativa',
    Field('departamento', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Departamento'),
    Field('distrito_educativo', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Distrito Educativo'),
    Field('nombre', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Nombre'),
    Field('nombre_director', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Nombre del Director'),
    Field('nombre_docente', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Nombre del Docente'),
    Field('campo', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Campo'),
    Field('area', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Área'),
    Field('gestion', 'integer', requires=IS_INT_IN_RANGE(2000, 3000), label='Gestión'),
    format="%(nombre)s - %(gestion)s"
)

# Nivel
db.define_table('nivel',
    Field('descripcion', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Descripción'),
    format="%(descripcion)s"
)

# Curso
db.define_table('curso',
    Field('nombre', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Nombre'),
    Field('paralelo', 'string', length=1, requires=[IS_NOT_EMPTY(), IS_LENGTH(1)], label='Paralelo'),
    Field('id_nivel', 'reference nivel', requires=IS_IN_DB(db, db.nivel.id, '%(descripcion)s'), label='Nivel'),
    format="%(nombre)s - %(paralelo)s"
)

# Trimestre
db.define_table('trimestre',
    Field('nombre', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Nombre'),
    Field('fecha_inicio', 'date', requires=IS_DATE_IN_RANGE(format='%Y-%m-%d', minimum=datetime.date(2000, 1, 1), error_message='Ingrese una fecha válida (YYYY-MM-DD)'), label='Fecha de Inicio'),
    Field('fecha_fin', 'date', requires=IS_DATE_IN_RANGE(format='%Y-%m-%d', minimum=datetime.date(2000, 1, 1), error_message='Ingrese una fecha válida (YYYY-MM-DD)'), label='Fecha de Fin'),
    Field('gestion', 'integer', requires=IS_INT_IN_RANGE(2000, 3000), label='Gestión'),
    format="%(nombre)s"
)

# Dimensiones
db.define_table('dimensiones',
    Field('nombre', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Nombre'),
    Field('porcentaje', 'double', requires=IS_FLOAT_IN_RANGE(0, 100), label='Porcentaje'),
    Field('gestion', 'integer', requires=IS_INT_IN_RANGE(2000, 3000), label='Gestión'),
    format="%(nombre)s - %(porcentaje)s"
)

# Criterio
db.define_table('criterio',
    Field('nombre', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Nombre'),
    Field('id_parametro', 'reference dimensiones', requires=IS_IN_DB(db, db.dimensiones.id, '%(nombre)s'), label='Dimensión', zero="Seleccione Una Dimensión", error_message="Seleccione Una Dimensión"),    
    Field('id_trimestre', 'reference trimestre', requires=IS_IN_DB(db, db.trimestre.id, '%(nombre)s'), label='Trimestre'),
    format="%(nombre)s"
)

# Estudiante
db.define_table('estudiante',
    Field('nombres', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Nombres'),
    Field('apellido_paterno', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Apellido Paterno'),
    Field('apellido_materno', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Apellido Materno'),
    Field('genero', 'string', length=1, requires=IS_IN_SET(['M', 'F']), label='Género'),
    Field('ci', 'string', length=15, requires=IS_NOT_EMPTY(), label='CI'),
    Field('fecha_nacimiento', 'date', requires=IS_DATE_IN_RANGE(format='%Y-%m-%d', minimum=datetime.date(1900, 1, 1), error_message='Ingrese una fecha válida (YYYY-MM-DD)'), label='Fecha de Nacimiento'),
    Field('edad', 'integer', requires=IS_INT_IN_RANGE(0, 150), label='Edad'),
    Field('curso_id', 'reference curso', requires=IS_IN_DB(db, db.curso.id, '%(nombre)s %(paralelo)s'), label='Curso'),
    format = "%(nombres)s %(apellido_paterno)s %(apellido_materno)s"
)

# Tutor
db.define_table('tutor',
    Field('nombre', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Nombre'),
    Field('apellido_paterno', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Apellido Paterno'),
    Field('apellido_materno', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Apellido Materno'),
    Field('telefono', 'string', length=15, requires=IS_MATCH('^[67][0-9]{7}$', error_message='Ingrese un número de teléfono válido (8 dígitos que inicie con 6 o 7)'), label='Teléfono'),
    Field('direccion', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Dirección'),
    Field('parentesco', 'string', length=128, requires=[IS_NOT_EMPTY(), IS_LENGTH(128)], label='Parentesco'),
    Field('estudiante_id', 'reference estudiante', requires=IS_IN_DB(db, db.estudiante.id, '%(nombres)s %(apellido_paterno)s %(apellido_materno)s'), label='Estudiante'),
    format="%(nombre)s %(apellido_paterno)s %(apellido_materno)s"
)

# Asistencia
db.define_table('asistencia',
    Field('estudiante_id', 'reference estudiante', requires=IS_IN_DB(db, db.estudiante.id, '%(nombres)s %(apellido_paterno)s %(apellido_materno)s'), label='Estudiante'),
    Field('fecha', 'date', requires=IS_DATE_IN_RANGE(format='%Y-%m-%d', minimum=datetime.date(1900, 1, 1), error_message='Ingrese una fecha válida (YYYY-MM-DD)'), label='Fecha'),
    Field('presente', 'string', requires=IS_IN_SET(['Presente', 'Falta', 'Licencia', 'Retraso']), default='Presente', label='Estado de Asistencia')
)

# Calificacion
db.define_table('calificacion',
    Field('estudiante_id', 'reference estudiante', requires=IS_IN_DB(db, db.estudiante.id, '%(nombres)s %(apellido_paterno)s %(apellido_materno)s'), label='Estudiante'),
    Field('curso_id', 'reference curso', requires=IS_IN_DB(db, db.curso.id, '%(nombre)s %(paralelo)s'), label='Curso'),
    Field('calificacion', 'double', requires=IS_FLOAT_IN_RANGE(0, 100), label='Calificación'),
    Field('id_criterio', 'reference criterio', requires=IS_IN_DB(db, db.criterio.id, '%(nombre)s'), label='Criterio')
)