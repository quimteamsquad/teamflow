---
name: planning
description: "Use when the user needs a technical plan, wants to decide how to build something, or needs architecture decisions before coding. Triggers on: /plan, 'how should we build this', 'technical approach', 'architecture for this feature', 'create the plan'. Also use when there is an approved spec that needs a technical plan."
---

# Planning: De Spec a Plan Tecnico

Convierte un spec aprobado en un plan tecnico con decisiones, estructura de cambios y validacion constitucional.

## Cuando Usar
- Hay un spec aprobado que necesita plan tecnico.
- El usuario invoca `/plan`.
- Se necesita tomar decisiones de arquitectura antes de implementar.

## El Proceso

1. **Leer el spec aprobado.** Abre `.workflow/specs/NNN-feature-name/spec.md`. Verifica que el estado sea `approved`. Si no lo esta, advierte y pregunta si continuar.

2. **Leer contexto del proyecto (solo lo necesario).** Lee:
   - `.workflow/constitution.md` (principios y reglas)
   - `.workflow/components.yaml` — identifica que componentes afecta el feature
   - **Solo las guidelines de componentes afectados.** Lee `.workflow/platform/components/<componente>.md` solo para los componentes que el feature toca. NUNCA cargues todas las guidelines a la vez.
   - Si una guideline excede ~20KB, lee solo las primeras 50 lineas (TOC/overview) y carga secciones relevantes bajo demanda.

3. **Generar el plan.** Crea `.workflow/specs/NNN-feature-name/plan.md` con:
   - **Componentes afectados** (tags de componente, tipo de cambio)
   - **Investigacion tecnica** (IT-001... hallazgos relevantes)
   - **Decisiones tecnicas** (DT-001... con contexto, opciones evaluadas, decision, rationale)
   - **Estructura de cambios** por componente (archivos, tipo, descripcion)
   - **Riesgos y mitigaciones**

4. **Constitutional gate check.** Si existe `.workflow/constitution.md`, verifica que cada principio y regla se respete. Documenta la verificacion en el plan.

5. **Validar trazabilidad.** Cada FR-xxx del spec debe estar cubierto por al menos una entrada en la estructura de cambios. Si falta cobertura, corregir.

6. **Actualizar estado.** Mueve `state.yaml` a fase `planning`, estado `draft`.

7. **Revisar con el usuario.** Presenta el plan y pide aprobacion.

## Template
Busca template en `.workflow/templates/plan.md`. Si no existe, usa la estructura descrita arriba.

## Errores Comunes
- Crear plan sin leer la constitution — puede violar principios del proyecto.
- No validar trazabilidad spec->plan — requisitos se pierden silenciosamente.
- Decisiones tecnicas sin rationale — se olvida el "por que" y se repite el debate.

## Siguiente Paso
Plan aprobado. Invoca `teamflow:tasking` para desglosar en tareas atomicas.
