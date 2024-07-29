# controllers/calificacion.py

def index():
    grid = SQLFORM.grid(
        db.calificacion,
        details=False,
        csv=False,
        advanced_search=False,
        maxtextlength=2500,
        orderby=[db.calificacion.id],
        deletable=False
    )
    titulo = 'Gestión de Calificaciones'
    response.view = 'calificacion/index.html'
    return dict(grid=grid, titulo=titulo)
