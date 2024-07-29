# -*- coding: utf-8 -*-
# intente algo como
# controllers/dimensiones.py

def index():
    grid = SQLFORM.grid(
        db.dimensiones,
        details=False,
        csv=False,
        advanced_search=False,
        maxtextlength=2500,
        orderby=[db.dimensiones.id],
        deletable=False
    )
    titulo = 'Gestión de Dimensiones'
    response.view = 'dimensiones/index.html'
    return dict(grid=grid, titulo=titulo)
