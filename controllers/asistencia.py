# -*- coding: utf-8 -*-
# intente algo como
# controllers/asistencia.py

def index():
    grid = SQLFORM.grid(
        db.asistencia,
        details=False,
        csv=False,
        advanced_search=False,
        maxtextlength=2500,
        orderby=[db.asistencia.id],
        deletable=False
    )
    titulo = 'Gestión de Asistencias'
    response.view = 'asistencia/index.html'
    return dict(grid=grid, titulo=titulo)
