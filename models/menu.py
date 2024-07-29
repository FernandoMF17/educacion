# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [        
        (T('Registro Pedagogico'), False, '#', [
            (T('Unidad Educativa'), False, URL(_app, 'unidad_educativa', 'index')),
            (T('Nivel'), False, URL(_app, 'nivel', 'index')),
            (T('Curso'), False, URL(_app, 'curso', 'index')),
            (T('Trimestre'), False, URL(_app, 'trimestre', 'index')),
            (T('Dimensiones'), False, URL(_app, 'dimensiones', 'index')),
            (T('Criterio'), False, URL(_app, 'criterio', 'index'))
        ]),        
        (T('Filiacion'), False, '#', [
            (T('Estudiante'), False, URL(_app, 'estudiante', 'index')),
            (T('Tutor'), False, URL(_app, 'tutor', 'index'))
        ]),
        (T('Calificaciones'), False, '#', [
            (T('Asistencia'), False, URL(_app, 'asistencia', 'index')),
            (T('Calificacion'), False, URL(_app, 'calificacion', 'index'))
        ])
    ]
