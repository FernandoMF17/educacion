# -*- coding: utf-8 -*-
# intente algo como
# controllers/curso.py

def index():
    grid = SQLFORM.grid(
        db.curso,
        details=False,
        csv=False,
        advanced_search=False,
        maxtextlength=2500,
        orderby=[db.curso.nombre, db.curso.paralelo],
        deletable=False
    )
    titulo = 'Gestión de Cursos'
    response.view = 'curso/index.html'
    return dict(grid=grid, titulo=titulo)
