---
name: tasking
description: "Use when a plan needs to be broken into implementable tasks, when the user wants a task breakdown, or wants to organize work. Triggers on: /tasks, 'break this down', 'create tasks', 'task list', 'what are the steps'. Also use when there is an approved plan ready for decomposition."
---

# Tasking: De Plan a Tareas Atomicas

Desglosa un plan tecnico aprobado en tareas atomicas, con dependencias, paralelismo y trazabilidad a requisitos.

## Cuando Usar
- Hay un plan aprobado que necesita desglose en tareas.
- El usuario invoca `/tasks`.
- Se necesita organizar el trabajo de implementacion.

## El Proceso

1. **Leer plan y spec.** Abre `.workflow/specs/NNN-feature-name/plan.md` y `spec.md`. Verifica que el plan este aprobado.

2. **Desglosar en tareas atomicas.** Cada tarea sigue el formato:

   ```
   ### T-001: [titulo descriptivo] [@componente]
   - **Archivos:** lista de archivos a crear/modificar
   - **Depende de:** T-xxx o ninguna
   - **Acceptance Criteria:** Linked a FR-xxx
     - [ ] [criterio verificable 1]
     - [ ] [criterio verificable 2]
   - **Status:** pending
   ```

3. **Marcar paralelismo.** Tareas sin dependencias mutuas se agrupan:
   - `<!-- PARALLEL-A -->` antes del grupo A
   - `<!-- PARALLEL-B -->` antes del grupo B
   - Tareas dentro del mismo grupo pueden ejecutarse simultaneamente.

4. **Validar cobertura.** Cada FR-xxx del spec debe tener al menos una tarea con acceptance criteria vinculado. Lista los FR no cubiertos y crea tareas faltantes.

5. **Validar dependencias.** No debe haber ciclos. Si T-003 depende de T-001, y T-001 depende de T-003, hay un error. Resolver reordenando o fusionando.

6. **Crear el archivo.** Escribe `.workflow/specs/NNN-feature-name/tasks.md`.

7. **Actualizar estado.** Mueve `state.yaml` a fase `tasking`, estado `draft`.

8. **Revisar con el usuario.** Presenta el desglose y pide aprobacion. El usuario puede reordenar, fusionar o dividir tareas.

## Template
Busca template en `.workflow/templates/tasks.md`. Si no existe, usa la estructura descrita arriba.

## Errores Comunes
- Tareas demasiado grandes (>1 commit) — dividir hasta que cada una sea un commit atomico.
- FR sin tarea asociada — la validacion de cobertura debe detectar esto.
- Dependencias circulares — siempre verificar el grafo antes de finalizar.

## Siguiente Paso
Tareas listas. Invoca `teamflow:executing` para implementar.
