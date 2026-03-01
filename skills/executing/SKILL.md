---
name: executing
description: "Use when the user wants to start coding, implement tasks, build a feature, or continue development work. Triggers on: /work, 'let's start building', 'implement the next task', 'continue coding', 'start working on this'. Also use when there are approved tasks ready for implementation."
---

# Executing: Implementacion de Tareas

## Overview
Despacha tareas atomicas a un subagent implementador, una por una, actualizando estado tras cada una.

## El Proceso

1. **Cargar contexto:** Lee `.workflow/state.md` para identificar el feature activo. Lee el `tasks.md`, `plan.md` y `spec.md` del feature. Lee `.workflow/components.yaml` para identificar componentes — carga solo las guidelines de los componentes que la tarea actual afecta.

2. **Seleccionar tarea:** Encuentra la siguiente tarea disponible (no completada `[ ]`, sin dependencias bloqueantes). Si todas las dependencias estan bloqueadas, informa al usuario y sugiere resolver el bloqueante primero.

3. **Preparar contexto para tf-implementer.** El subagent arranca con contexto vacio — solo ve lo que le pasas. Reune inline en un solo prompt:
   - La tarea completa con cada acceptance criterion
   - Decisiones tecnicas del plan que afectan esta tarea (DT-NNN relevantes)
   - Guidelines del componente afectado (leidas en paso 1)
   - Notas dejadas por tareas anteriores (si existen)
   - Paths concretos de archivos a crear/modificar

4. **Despachar subagent:** Usa el Agent tool con `subagent_type: "general-purpose"` y nombre `tf-implementer`. Pasa todo en el prompt.

5. **Procesar resultado:** Al retornar el subagent:
   - Marca la tarea como `[x]` en `tasks.md`
   - Actualiza `state.yaml` (progreso, files_changed)
   - Actualiza `state.md` con el avance
   - Si el subagent reporto `notes`, guardalas para la siguiente tarea

6. **Continuar o transicionar:**
   - Si hay mas tareas disponibles, ofrece continuar con la siguiente
   - Si todas las tareas estan completas, anuncia la transicion

7. **3-Strike Protocol** (si una tarea falla):
   - Strike 1: Diagnostica el error, intenta fix directo
   - Strike 2: Intenta un approach diferente
   - Strike 3: Replantea la tarea desde cero
   - Despues de 3 strikes: Escala al humano con diagnostico completo

## Errores Comunes
- Despachar sin pasar acceptance criteria — el subagent no sabra que verificar
- No guardar las notas entre tareas — se pierde contexto valioso
- Intentar ejecutar tareas con dependencias bloqueantes

## Siguiente Paso
"Todas las tareas completas. Invoca teamflow:reviewing para code review."
