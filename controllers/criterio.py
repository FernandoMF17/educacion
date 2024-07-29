# -*- coding: utf-8 -*-
# intente algo como
# controllers/criterio.py

def index():
    grid = SQLFORM.grid(
        db.criterio,
        details=False,
        csv=False,
        advanced_search=False,
        maxtextlength=2500,
        orderby=[db.criterio.id],
        deletable=False
    )
    titulo = 'Gestión de Criterios'
    response.view = 'criterio/index.html'
    return dict(grid=grid, titulo=titulo)
