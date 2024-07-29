# -*- coding: utf-8 -*-
# intente algo como
# controllers/nivel.py

def index():
    grid = SQLFORM.grid(
        db.nivel,
        details=False,
        csv=False,
        advanced_search=False,
        maxtextlength=2500,
        orderby=[db.nivel.id],
        deletable=False
    )
    titulo = 'Gestión de Niveles'
    response.view = 'nivel/index.html'
    return dict(grid=grid, titulo=titulo)
