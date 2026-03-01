---
name: init
description: "Use when a project needs TeamFlow setup, when .workflow/ directory doesn't exist, or when the user wants to initialize TeamFlow in a new project"
---

# Init: Onboarding de Proyecto

Configura TeamFlow en un proyecto nuevo con una conversacion guiada. Genera la estructura minima para empezar a trabajar.

## Cuando Usar
- El proyecto no tiene `.workflow/` (redirigido desde using-teamflow).
- El usuario quiere inicializar TeamFlow en un proyecto existente.
- El usuario invoca `/init`.

## El Proceso

1. **Preguntar nombre del proyecto.** Usa el nombre del directorio como sugerencia.

2. **Preguntar modo de componentes:**
   - **Single** — Un solo componente (monolito, CLI, plugin).
   - **Multi** — Multiples componentes (frontend + backend, microservicios). Si multi, pide nombre y path de cada uno.

3. **Preguntar reglas no-negociables.** "Tienes 1-3 reglas que SIEMPRE deben respetarse? (ej: 'nunca borrar datos de produccion', 'siempre TDD'). Si no, di 'ninguna por ahora'."

4. **Detectar contexto existente.** Busca:
   - `CLAUDE.md` en la raiz — ofrecer integrar con TeamFlow
   - `.workflow/` parcial — ofrecer completar
   - Guidelines grandes (>20KB) — listar como candidatos a skill: "Estos archivos son grandes. Considera convertirlos a skills con `/create-skill` para mejor manejo de contexto."

5. **Preguntar dominios de negocio.** "Cuales son los dominios principales de tu proyecto? (ej: auth, payments, compliance, content). Estos organizan tus specs." Si no sabe, sugerir empezar con uno generico y refinar despues.

6. **Generar estructura:**
   ```
   .workflow/
     constitution.md      # Reglas del usuario + principios base
     components.yaml      # Modo single/multi con stacks
     state.md             # Estado global (vacio, listo para /spec)
     platform/
       architecture.md    # Placeholder: "Actualizar tras primer /done"
       decisions.md       # Vacio, listo para ADRs
     templates/           # Copiar templates del plugin
     specs/               # Organizado por dominio de negocio
       [dominio]/         # Un directorio por dominio (auth/, payments/, etc.)
   ```

7. **Generar/actualizar CLAUDE.md.** Si no existe, crear uno minimo:
   ```markdown
   # [Nombre del Proyecto]

   [Reglas no-negociables del usuario]

   ## Workflow
   Este proyecto usa TeamFlow para desarrollo spec-driven.
   Todo feature pasa por: spec -> plan -> tasks -> work -> review -> production.
   Para orientarte, usa el skill teamflow:using-teamflow.
   ```
   Si ya existe, agregar solo la seccion de workflow al final.

8. **Confirmar.** Muestra resumen de lo generado y sugiere: "Proyecto listo. Usa `/spec` para definir tu primer feature."

## Lo Que NO Hace
- No pregunta stack tecnologico en detalle (eso va en components.yaml, refinado durante /plan).
- No genera constitution larga — empieza con las reglas del usuario y crece con /done.
- No bloquea — todo lo no respondido queda como placeholder.
