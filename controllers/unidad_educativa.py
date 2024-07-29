# -*- coding: utf-8 -*-
# intente algo como
# controllers/unidad_educativa.py

def index():
    grid = SQLFORM.grid(
        db.unidad_educativa,
        details=False,
        csv=False,
        advanced_search=False,
        maxtextlength=2500,
        orderby=[db.unidad_educativa.id],
        deletable=False
    )
    titulo = 'Gestión de Unidades Educativas'
    response.view = 'unidad_educativa/index.html'
    return dict(grid=grid, titulo=titulo)
