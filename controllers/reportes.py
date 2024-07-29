def asistencia():
    titulo = "Asistencia"
    response.view = 'reportes/asistencia.html'
    return dict(titulo=titulo)

def calificacion_estudiante():
    id_estudiante = 0
    titulo = "Calificaciones por Estudiante"
    response.view = 'reportes/calificacion_estudiante.html'
    return dict(titulo=titulo)

def calificacion_curso():
    id_curso = 0
    titulo = "Calificaciones por Curso"
    response.view = 'reportes/calificacion_curso.html'
    return dict(titulo=titulo)

def boletin_trimestral():
    id_trimestre = 0
    titulo = "Boletín Trimestral"
    response.view = 'reportes/boletin_trimestral.html'
    return dict(titulo=titulo)

def boletin_anual():
    gestion = 2024
    titulo = "Boletín Anual"
    response.view = 'reportes/boletin_anual.html'
    return dict(titulo=titulo)
