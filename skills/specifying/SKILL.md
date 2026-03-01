---
name: specifying
description: "Use when the user has a new idea, wants to build a feature, needs to define requirements, or wants to formalize what to build before coding. Triggers on: /spec, 'I want to build X', 'new feature', 'let's add X', 'define requirements for', 'what should we build'. This is the starting point of the TeamFlow workflow."
---

# Specifying: De Idea a Spec

Convierte ideas, tickets o conversaciones en especificaciones tech-agnosticas con requisitos trazables.

## Cuando Usar
- El usuario quiere definir un nuevo feature.
- Hay un ticket externo (Jira, etc.) que necesita formalizarse.
- Se necesita documentar requisitos antes de planificar.

## El Proceso

1. **Identificar fuente.** Pregunta: "De donde viene este feature?" (manual, Jira, otro). Si es externo, extrae la info disponible via MCP. Si es manual, guia conversacionalmente.

2. **Explorar el problema.** Guia al usuario a traves de:
   - Que problema resuelve esto?
   - Quien se beneficia?
   - Como se ve el exito?

3. **Generar el spec.** Crea `.workflow/specs/NNN-feature-name/spec.md` con:
   - **User Stories** con acceptance criteria (Given/When/Then)
   - **Requisitos Funcionales** numerados (FR-001, FR-002...)
   - **Success Criteria** medibles (SC-001...)
   - **Edge Cases** con comportamiento esperado — siempre preguntar "que pasa si...?" para cada flujo principal
   - **Fuera de Alcance** explicito

4. **Numerar secuencialmente.** Busca el ultimo NNN en `.workflow/specs/` e incrementa. Primer spec = 001.

5. **Crear estado del feature.** Crea `.workflow/specs/NNN-feature-name/state.yaml` con lifecycle en fase `specifying`, estado `draft`.

6. **Solo WHAT y WHY.** El spec es tech-agnostico. Nunca incluir HOW (tecnologias, arquitectura, implementacion). Si detectas decisiones tecnicas infiltrandose ("usar Redis", "crear tabla X"), moverlas a notas para el plan.

7. **Cada requisito debe ser verificable.** FR sin criterio de aceptacion medible = FR invalido. Reformula hasta que sea testeable.

8. **Revisar con el usuario.** Presenta el spec y pide aprobacion. El usuario puede iterar.

## Template
Busca template en `.workflow/templates/spec.md`. Si no existe, usa la estructura descrita arriba.

## Siguiente Paso
Spec aprobado. Invoca `teamflow:planning` para crear el plan tecnico.
