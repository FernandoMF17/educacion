# -*- coding: utf-8 -*-
# intente algo como
# controllers/trimestre.py

def index():
    grid = SQLFORM.grid(
        db.trimestre,
        details=False,
        csv=False,
        advanced_search=False,
        maxtextlength=2500,
        orderby=[db.trimestre.id],
        deletable=False
    )
    titulo = 'Gestión de Trimestres'
    response.view = 'trimestre/index.html'
    return dict(grid=grid, titulo=titulo)
