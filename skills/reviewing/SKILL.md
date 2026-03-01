---
name: reviewing
description: "Use when implementation is complete and code needs adversarial review against the spec, or when invoked via /review"
---

# Reviewing: Code Review Adversarial

## Overview
Despacha un reviewer adversarial que verifica el codigo contra el spec y el plan. El reviewer NO confia en lo que el implementador dice que hizo.

## El Proceso

1. **Cargar contexto:** Lee el `spec.md`, `plan.md` y `tasks.md` del feature activo.

2. **Obtener diff:** Ejecuta `git diff` para capturar todos los cambios del feature. Si el feature tiene multiples commits, usa `git log` para identificar el rango y `git diff` sobre ese rango.

3. **Despachar tf-reviewer:** Usa el Task tool con `subagent_type: "general-purpose"` y nombre `tf-reviewer`. Pasa inline:
   - Spec completo (success criteria y acceptance criteria)
   - Plan (decisiones tecnicas)
   - Diff del codigo
   - **Framing adversarial:** "El implementador termino sospechosamente rapido. NO confies en su reporte. Verifica TODO contra el codigo real. Verifica CADA acceptance criteria contra el codigo REAL, no contra lo que el implementador dice que hizo."
   - **Checklist de shortcuts:** Busca activamente: logica simplificada sin edge cases, valores hardcodeados, tests que no testean (asserts triviales, mocks auto-replicantes), TODOs/placeholders, error handling ausente o generico, codigo muerto.

4. **Evaluar veredicto:**
   - **PASS** — Codigo cumple spec. Proceder a producing.
   - **PASS_WITH_NOTES** — Cumple pero con observaciones menores. Proceder con las notas registradas.
   - **NEEDS_CHANGES** — Hallazgos que requieren correccion. Volver a executing con los hallazgos como nuevas tareas.

5. **Escribir review:** Crea `review.md` en el directorio del feature con hallazgos, severidad y veredicto.

6. **Si NEEDS_CHANGES:** Agrega los hallazgos como tareas nuevas al final de `tasks.md` y actualiza `state.md` para volver a fase executing.

## Errores Comunes
- Revisar sin el spec — el review pierde su ancla objetiva
- Confiar en el reporte del implementador sin verificar el codigo real

## Siguiente Paso
"Review aprobado. Invoca teamflow:producing para finalizar."
