---
name: specifying
description: "Use when the user has a new idea, wants to build a feature, needs to define requirements, or wants to formalize what to build before coding. Triggers on: /spec, 'I want to build X', 'new feature', 'let's add X', 'define requirements for', 'what should we build'. This is the starting point of the TeamFlow workflow."
---

# Specifying: De Idea a Spec

Convierte ideas, tickets o conversaciones en specs formales de reglas de negocio. Una spec = un concepto. Compacta (~100 lineas), verificable, sin implementacion.

## Cuando Usar
- El usuario quiere definir un nuevo feature o regla de negocio.
- Hay un ticket externo (Jira, etc.) que necesita formalizarse.
- Se necesita documentar requisitos antes de planificar.

## Principios

- **Una spec = un concepto.** Si la idea mezcla funcionalidades independientes, separar en specs distintas. Prueba: si puedes implementar A sin tocar B, son specs distintas.
- **Reglas de negocio, no implementacion.** La spec define QUE y POR QUE con logica formal. Nunca HOW (tecnologias, archivos, arquitectura). Si detectas "usar Redis" o "crear tabla X", moverlo a notas para el plan.
- **Compacta y formal.** Target: ~100 lineas. Inputs como tabla, reglas como logica formal, invariantes explicitas, matriz de estados completa, BDD exhaustivo.
- **Verificable.** Cada regla debe poder probarse con la matriz de estados. Si no puedes escribir la matriz completa, la spec no esta clara.

## El Proceso

1. **Identificar fuente.** "De donde viene este feature?" (manual, Jira, otro). Si es externo, extrae la info via MCP.

2. **Explorar y descomponer.** Guia al usuario:
   - Que problema resuelve?
   - Es un concepto o varios? Si son varios, separar.
   - Cuales son los inputs y outputs?
   - Cuales son las reglas de negocio?

3. **Ubicar por dominio.** Las specs se organizan por dominio de negocio:
   ```
   .workflow/specs/
     compliance/
       age-verification.md
       camlist-sfw.md
     payments/
       payout-rules.md
     auth/
       session-management.md
   ```
   Pregunta al usuario: "A que dominio pertenece esta spec?" Si el dominio no existe, crearlo.

4. **Generar la spec.** Usa el template `spec.md`. Asegurar que incluye:
   - **Dominio formal:** inputs como tabla, constantes del sistema
   - **Reglas de negocio:** logica formal (R1, R2... con notacion clara)
   - **Invariantes:** condiciones que SIEMPRE se cumplen + que NO afecta a esta spec
   - **Matriz completa de estados:** todas las combinaciones posibles de inputs → outputs
   - **BDD exhaustivo:** escenarios que cubren cada fila de la matriz
   - **Contrato API** (solo si la spec define/modifica un endpoint)

5. **Crear estado.** Crea `state.yaml` en el directorio de la spec con lifecycle en fase `specifying`, estado `draft`.

6. **Si hay detalles de implementacion valiosos** (flows, archivos existentes, bugs conocidos), guardarlos en `_references/` junto a la spec. No mezclar con la spec formal.

7. **Revisar con el usuario.** Presenta la spec. Verificar: "La matriz de estados cubre TODOS los casos?" El usuario itera hasta aprobar.

## Template
Busca template en `.workflow/templates/spec.md`. Si no existe, usa la estructura descrita arriba.

## Siguiente Paso
Spec aprobado. Invoca `teamflow:planning` para crear el plan tecnico.
