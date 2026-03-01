# SPEC — [titulo]

| Campo | Valor |
|-------|-------|
| Version | 1.0.0 |
| Owner | [dominio / equipo] |
| Scope | [una frase: que determina esta spec] |
| Estado | draft / approved |

---

## 1. Dominio Formal

### 1.1 Inputs

| Variable | Tipo | Descripcion |
|----------|------|-------------|
| [var] | [tipo] | [que representa] |

### 1.2 Constantes del sistema

```
[CONSTANTE] = [valores]
```

---

## 2. Reglas de Negocio (Source of Truth)

### R1 — [nombre de la regla]

```
[expresion formal de la regla]
```

### R2 — [nombre]

```
[expresion formal]
```

---

## 3. Invariantes

- [Condicion que SIEMPRE debe cumplirse]
- [Variable o concepto que NO afecta a esta spec]

---

## 4. Matriz Completa de Estados

| [Input A] | [Input B] | [Output] |
|-----------|-----------|----------|
| true | true | [valor] |
| true | false | [valor] |
| false | true | [valor] |
| false | false | [valor] |

No existen mas combinaciones posibles en esta spec.

---

## 5. BDD — Escenarios Exhaustivos

### Scenario: [titulo descriptivo]

Given [contexto]
And [condicion]
When [accion]
Then [resultado esperado]

---

## 6. Contrato API (si aplica)

<!-- Solo si la spec define o modifica un endpoint. Formato OpenAPI simplificado. -->

```yaml
POST /api/[recurso]:
  request:
    [campo]: [tipo]
  response:
    [campo]: [tipo]
  errors:
    [codigo]: [descripcion]
```

---

## Fuera de Alcance

- [Exclusion explicita y por que]
