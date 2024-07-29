# -*- coding: utf-8 -*-
# intente algo como
# controllers/tutor.py

def index():
    grid = SQLFORM.grid(
        db.tutor,
        details=False,
        csv=False,
        advanced_search=False,
        maxtextlength=2500,
        orderby=[db.tutor.id],
        deletable=False
    )
    titulo = 'Gestión de Tutores'
    response.view = 'tutor/index.html'
    return dict(grid=grid, titulo=titulo)
