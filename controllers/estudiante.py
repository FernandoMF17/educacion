# -*- coding: utf-8 -*-
# intente algo como
# controllers/estudiante.py

def index():
    grid = SQLFORM.grid(
        db.estudiante,
        details=False,
        csv=False,
        advanced_search=False,
        maxtextlength=2500,
        orderby=[db.estudiante.id],
        deletable=False
    )
    titulo = 'Gestión de Estudiantes'
    response.view = 'estudiante/index.html'
    return dict(grid=grid, titulo=titulo)
