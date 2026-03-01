---
name: producing
description: "Use when a feature has passed review and needs to be finalized, archived, and its knowledge extracted to platform specs"
---

# Producing: Finalizacion y Archivado

## Overview
Verifica goal-backward contra el spec, archiva el feature y extrae conocimiento a platform specs.

## El Proceso

1. **Verificacion goal-backward:** Despacha `tf-verifier` via Task tool (`subagent_type: "general-purpose"`, nombre `tf-verifier`). Pasa inline los success criteria del spec y la lista de archivos modificados. El verifier aplica 3 niveles: Exists → Substantive → Wired (ver skill `teamflow:verifying` para detalle).

2. **Si verificacion falla:** Genera gap report. NO archiva. Regresa a executing con los gaps como tareas.

3. **Si verificacion pasa — Archivar:**
   - Mueve el directorio del spec a `specs/_archive/`
   - Genera resumen en `history/summaries/` usando template `summary.md`

4. **Extraer conocimiento:** Revisa si el feature produjo:
   - Nuevas decisiones arquitectonicas → actualiza platform specs
   - Nuevos patrones o convenciones → agrega a platform specs
   - Platform specs son archivos en `.workflow/platform/` — NUNCA se eliminan, solo se actualizan
   - **Guidelines grandes:** Si un guideline generado o actualizado excede ~20KB, sugiere al usuario convertirlo a skill con `/create-skill` para mejor manejo de contexto.

5. **Limpiar estado:** Remueve el feature activo de `state.md`. Resetea `state.yaml` del feature a `phase: archived`.

## Siguiente Paso
"Feature archivado y conocimiento extraido. Usa /spec para el siguiente feature o /status para ver el estado."
