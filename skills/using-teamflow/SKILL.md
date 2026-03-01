---
name: using-teamflow
description: "Use when starting a session in a project with TeamFlow, when the user wants to begin any development workflow, or when unsure which TeamFlow skill to invoke"
---

# TeamFlow: Workflow Spec-Driven

TeamFlow guia el desarrollo de features a traves de un ciclo:
spec -> plan -> tasks -> work -> review -> production.

## Skills Disponibles

| Comando | Skill | Cuando |
|---------|-------|--------|
| /init | init | Inicializar TeamFlow en un proyecto nuevo |
| /spec | specifying | Definir un nuevo feature o requisitos |
| /plan | planning | Crear plan tecnico desde un spec aprobado |
| /tasks | tasking | Desglosar plan en tareas atomicas |
| /work | executing | Implementar la siguiente tarea |
| /review | reviewing | Code review post-implementacion |
| /done | producing | Finalizar feature, archivar, actualizar platform |
| /status | — | Ver estado actual del proyecto |
| /resume | resuming | Restaurar contexto de sesion previa |
| /quick | — | Bug fix o cambio menor sin spec formal |

## Flujo
1. **Detectar proyecto inicializado.** Verifica si `.workflow/` existe. Si NO existe, invoca `teamflow:init` para configurar el proyecto primero.
2. Lee `.workflow/state.md` para saber donde estamos.
3. Si hay feature activo, sugiere la siguiente accion segun la fase.
4. Si no hay feature activo, sugiere /spec o /quick.

## Regla
Si un skill aplica a la situacion, invocalo. No resumas, no tomes atajos.
