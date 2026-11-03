"""
Configuración institucional por defecto de PerfilEgreso 360.
Estos valores son de ejemplo/demostración: cada carrera debe poder
sobrescribirlos desde el módulo de Configuración de la app.
"""

APP_TITLE = "PerfilEgreso 360"
APP_SUBTITLE = "Sistema de seguimiento y aseguramiento del logro del Perfil de Egreso"

META_INSTITUCIONAL_DEFAULT = 85
ESCALA_NOTA_MIN = 1.0
ESCALA_NOTA_MAX = 7.0
NOTA_APROBACION = 4.0

NIVELES_DESEMPENO = [
    (90, "Desempeño Estratégico"),
    (80, "Integrado Alto"),
    (70, "En Desarrollo"),
    (0, "Crítico"),
]

BRECHA_CRITICA = 20
BRECHA_MEDIA = 10

LINEAS_FORMATIVAS_DEMO = [
    "Evaluación y diagnóstico",
    "Prescripción del ejercicio",
    "Intervención profesional",
    "Investigación aplicada",
    "Gestión",
    "Comunicación y liderazgo",
]

PONDERACIONES_DEMO = {
    "Evaluación académica": 40,
    "Actividad práctica": 30,
    "Evaluación interciclo": 20,
    "Evaluación externa/nacional": 10,
}

TIPOS_REPORTE = [
    "Alerta temprana",
    "Competencias",
    "Líneas formativas",
    "Total líneas",
    "Total competencias",
]


def clasificar_nivel(logro_pct: float) -> str:
    for umbral, etiqueta in NIVELES_DESEMPENO:
        if logro_pct >= umbral:
            return etiqueta
    return NIVELES_DESEMPENO[-1][1]


def clasificar_prioridad(brecha_pts: float) -> str:
    if brecha_pts >= BRECHA_CRITICA:
        return "Crítica"
    if brecha_pts >= BRECHA_MEDIA:
        return "Media"
    return "Baja"
