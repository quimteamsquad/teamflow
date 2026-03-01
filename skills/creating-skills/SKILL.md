---
name: creating-skills
description: "Use when converting a large guideline to a skill, when the user wants to create a new skill for their project, or when invoked via /create-skill"
---

# Creating Skills: Wrapper para skill-creator

Verifica que `skill-creator` este disponible e invocalo con contexto TeamFlow.

## Cuando Usar
- Un guideline grande (>20KB) fue flaggeado como candidato a skill.
- El usuario quiere crear un skill nuevo para su proyecto.
- Se invoca `/create-skill`.

## El Proceso

1. **Verificar skill-creator.** Intenta invocar `skill-creator:skill-creator`. Si no esta disponible, informa: "Necesitas instalar el plugin skill-creator. Ejecuta: `/plugin marketplace add anthropics/skill-creator` y luego `/plugin install skill-creator`."

2. **Preparar contexto.** Reune para pasar a skill-creator:
   - **Source:** El archivo guideline o la descripcion del skill deseado
   - **Destino:** Skills del proyecto van en `.claude/skills/` (NO en el plugin TeamFlow)
   - **Convenciones TeamFlow:**
     - Skills en espanol (si el proyecto esta en espanol)
     - Frontmatter con `name` y `description` (triggering claro)
     - Estructura: Cuando Usar → El Proceso → Errores Comunes → Siguiente Paso
     - Progressive disclosure: instruccion concreta primero, detalle solo si necesario

3. **Invocar skill-creator.** Usa el Skill tool con `skill-creator:skill-creator` pasando el contexto preparado.

4. **Validar resultado.** Verifica que el skill generado:
   - Tiene description de triggering que activara correctamente
   - No excede ~200 lineas (si es mas largo, dividir)
   - Sigue la estructura TeamFlow

5. **Registrar.** Si el skill reemplaza un guideline grande, actualiza el guideline original con una nota: "Este guideline tiene un skill complementario en `.claude/skills/[nombre]`."
