---
name: verifying
description: "Use when about to claim work is complete, when verifying test results, or when ensuring implementation meets acceptance criteria"
---

# Verifying

Disciplina de verificacion antes de declarar que algo esta completo. Aplica en todas las phases.

## Regla Base

**Evidencia antes de afirmaciones. SIEMPRE.**

No digas "los tests pasan" sin haberlos corrido. No digas "el archivo existe" sin haberlo leido. No digas "cumple el criterio" sin haberlo verificado contra el codigo real.

## El Proceso

1. **Correr tests.** Ejecutar, leer el output completo. Si fallan, reportar el fallo exacto — no reintentar en silencio.

2. **Leer archivos.** Verificar que existen y contienen lo esperado. No asumir que un write anterior funciono.

3. **Verificar acceptance criteria.** Revisar cada criterio de la task (AC) uno por uno contra el codigo o comportamiento real. Marcar cada uno como cumplido o no cumplido con evidencia.

4. **Reportar honestamente.**
   - Test falla → reportar el error exacto
   - No hay tests → declararlo explicitamente
   - Tests no cubren un caso → documentar el gap
   - Algo no funciona → decirlo antes de que se descubra despues

5. **NUNCA mentir sobre resultados.** (Constitution R4: Honestidad Radical)

## Cuando Aplicar

- Antes de marcar una task como `[x] done`
- Antes de transicionar de implementation a review
- Antes de declarar un veredicto en review
- Antes de afirmar "listo", "funciona", o "completo"

## Anti-Patterns

- "Los tests pasan" sin haberlos ejecutado
- Marcar `[x]` sin verificar el criterio
- Omitir fallos para no alarmar
- Asumir que el codigo hace lo que el plan dice
