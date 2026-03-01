---
name: resuming
description: "Use when restoring context from a previous session, when the user starts a new session with active work, or wants to continue where they left off. Triggers on: /resume, 'where were we', 'continue', 'what was I doing', 'pick up where we left off'."
---

# Resuming

Restaura contexto de trabajo previo sin perder tiempo ni repetir trabajo. Aplica en cualquier fase del workflow.

## Cuando Usar

- Al inicio de una nueva sesion con trabajo activo
- Cuando el usuario dice "donde estabamos?" o "continuar"
- Despues de un crash o interrupcion
- Invocado via `/resume`

## El Proceso: 5-Question Reboot Test

### Paso 1: Leer estado global

Lee `.workflow/state.md` para obtener la posicion general: feature activo, phase, blockers.

### Paso 2: Leer estado de la feature

Lee el `state.yaml` de la feature activa (ruta en state.md). Obtener: phase, tasks_progress, sesiones previas, decisiones.

### Paso 3: Cargar artefactos relevantes

Lee SOLO los artefactos necesarios para la phase actual:
- **spec/plan phase:** `spec.md`
- **tasks phase:** `spec.md` + `plan.md`
- **implementation:** `tasks.md` (buscar la task actual)
- **review:** `tasks.md` + archivos modificados
- **done:** `summary.md`

NO leer todo. Lazy-load segun la phase.

### Paso 4: Presentar resumen estructurado

Responder estas 5 preguntas al usuario:

1. **Donde estoy?** Feature + phase + task actual (si aplica)
2. **A donde voy?** Tasks pendientes o siguiente phase
3. **Cual es el objetivo?** Success criteria de la spec
4. **Que he aprendido?** Decisiones clave tomadas (DT-NNN)
5. **Que he hecho?** Tasks completadas y sesiones previas

Formato: tabla o lista compacta. No parrafos largos.

### Paso 5: Sugerir accion

Basado en la phase actual, sugerir la siguiente accion concreta:
- Si hay task in-progress: continuarla
- Si hay task blocked: resolver el blocker
- Si todas las tasks de un grupo estan done: avanzar al siguiente grupo
- Si la phase esta completa: transicionar a la siguiente

## Errores Comunes

- **Leer todos los artefactos de golpe.** Solo cargar lo necesario para la phase actual. El resto se lazy-load cuando se necesite.
- **Saltarse el resumen.** SIEMPRE presentar las 5 preguntas antes de actuar. El usuario necesita validar el contexto.
- **Asumir estado.** Leer archivos reales, no recordar de memoria. Los archivos son la fuente de verdad.
