# Argoth Trading — Plan maestro de aprendizaje y construcción

> Propósito: construir Argoth Trading como un proyecto educativo real de trading algorítmico, aprendiendo programación, mercados, backtesting, gestión de riesgo, automatización y machine learning paso a paso.
>
> Aviso: este proyecto es educativo. Ninguna lección, estrategia o ejemplo debe interpretarse como asesoría financiera ni como recomendación de inversión.


## 0. Por dónde empiezas hoy

Empiezas por la **Lección 1**, no por instalar brokers, APIs ni machine learning. Tu primera tarea es entender el flujo mental del sistema antes de escribir código.

### Qué tienes que hacer ahora

1. Lee la sección **Primera lección — Qué es un sistema de trading algorítmico**.
2. Copia en tu cuaderno o archivo de notas estas cuatro palabras: `datos`, `estrategia`, `backtesting`, `riesgo`.
3. Escribe una explicación de una frase para cada palabra, usando tus propias palabras.
4. Haz el ejercicio de la primera lección y responde las cuatro preguntas.
5. No instales nada todavía y no conectes ningún broker. Primero confirmaremos que entiendes el mapa básico.

### Tiempo estimado

Dedica entre 20 y 30 minutos. Si tardas más, no pasa nada: aprender trading algorítmico bien es mejor que avanzar rápido sin entender.

### Entregable de esta primera tarea

Respóndeme con este formato:

```text
1. Señal vs orden:
2. Por qué no usar broker real todavía:
3. Qué hace un backtest:
4. Por qué el riesgo va primero:
5. Mi duda principal ahora mismo:
```

Con tus respuestas haré tres cosas:

- corregir conceptos equivocados,
- reforzar lo que ya entendiste,
- y decidir si estamos listos para crear el primer archivo de Python de Argoth Trading.

### Qué NO debes hacer todavía

- No operar con dinero real.
- No usar apalancamiento.
- No comprar cursos, señales ni bots.
- No optimizar estrategias.
- No empezar por machine learning.
- No copiar código sin entenderlo.

La prioridad ahora es construir criterio. El código viene después.

## 1. Principios del proyecto

Argoth Trading se construirá con estas reglas:

1. Aprender antes de automatizar: ningún componente se programa sin entender primero el concepto.
2. Avanzar por versiones pequeñas: cada versión debe funcionar, aunque sea simple.
3. Separar responsabilidades: cada módulo tendrá una tarea clara para que el sistema pueda crecer.
4. Medir antes de confiar: toda estrategia debe probarse con datos históricos antes de ejecutarse.
5. Proteger el capital: la gestión de riesgo tiene prioridad sobre la búsqueda de beneficios.
6. Registrar todo: los datos, señales, decisiones, errores y operaciones deben poder auditarse.
7. Evitar promesas irreales: el objetivo es aprender a construir sistemas robustos, no garantizar ganancias.

## 2. Qué aprenderemos en orden

### Fase 0 — Fundamentos absolutos

Objetivo: entender el lenguaje básico antes de escribir el sistema.

Aprenderemos:

- Qué es Python y por qué se usa en trading algorítmico.
- Qué es un mercado financiero.
- Qué son precio, volumen, vela, spread, liquidez y volatilidad.
- Qué es una estrategia de trading.
- Qué significa comprar, vender, estar en efectivo y mantener una posición.
- Qué es el riesgo y por qué puede destruir una cuenta aunque una estrategia acierte muchas veces.

Resultado esperado:

- Un glosario propio de Argoth Trading.
- Primeros scripts pequeños de Python sin conexión a brokers reales.

### Fase 1 — Versión mínima funcional local

Objetivo: crear una aplicación simple que lea datos históricos y pruebe una estrategia básica.

Componentes:

- Cargador de datos históricos desde archivos CSV.
- Representación simple de velas de mercado.
- Estrategia inicial de cruce de medias móviles.
- Motor de backtesting básico.
- Métricas simples: beneficio total, número de operaciones, operaciones ganadoras y operaciones perdedoras.

Resultado esperado:

- Ejecutar un backtest local sin dinero real.
- Entender cada línea de código del flujo completo.

### Fase 2 — Arquitectura profesional inicial

Objetivo: ordenar el proyecto como una base escalable.

Módulos propuestos:

- `argoth/data`: descarga, validación y almacenamiento de datos.
- `argoth/strategies`: reglas que generan señales de compra, venta o espera.
- `argoth/backtesting`: simulación histórica de estrategias.
- `argoth/risk`: límites de pérdida, tamaño de posición y exposición máxima.
- `argoth/execution`: interfaz futura con brokers o exchanges.
- `argoth/portfolio`: estado de capital, posiciones y resultados.
- `argoth/config`: parámetros del sistema por entorno.
- `argoth/logging`: registros técnicos y operativos.
- `tests`: pruebas automatizadas.

Resultado esperado:

- Código modular.
- Pruebas pequeñas para validar comportamiento.
- Separación clara entre simulación y ejecución real.

### Fase 3 — Backtesting más realista

Objetivo: evitar conclusiones falsas por simulaciones demasiado optimistas.

Mejoras:

- Comisiones.
- Slippage.
- Spread.
- Tamaño de posición.
- Control de capital disponible.
- Curva de equity.
- Drawdown máximo.
- Comparación contra comprar y mantener.

Resultado esperado:

- Reportes más honestos sobre el rendimiento histórico.

### Fase 4 — Gestión de riesgo

Objetivo: convertir el riesgo en una parte explícita del sistema.

Aprenderemos:

- Riesgo por operación.
- Stop loss y take profit.
- Tamaño de posición.
- Drawdown diario, semanal y total.
- Correlación entre activos.
- Por qué una estrategia rentable puede quebrar si arriesga demasiado.

Resultado esperado:

- Un módulo de riesgo que pueda bloquear operaciones peligrosas.

### Fase 5 — Datos de mercado reales

Objetivo: conectar fuentes de datos externas sin ejecutar operaciones reales todavía.

Aprenderemos:

- APIs.
- Rate limits.
- Autenticación.
- Datos OHLCV.
- Calidad de datos.
- Diferencia entre datos históricos, retrasados y en tiempo real.

Resultado esperado:

- Descarga reproducible de datos.
- Caché local para no depender siempre de la red.

### Fase 6 — Paper trading

Objetivo: simular operaciones en condiciones cercanas al mercado real sin usar dinero real.

Aprenderemos:

- Órdenes de mercado y limitadas.
- Estado de una orden.
- Reintentos y fallos de conexión.
- Diferencia entre señal, orden y ejecución.

Resultado esperado:

- Un ejecutor simulado que registre operaciones como si fueran reales.

### Fase 7 — Ejecución automática controlada

Objetivo: preparar una integración con broker o exchange de forma segura.

Reglas mínimas:

- Modo real desactivado por defecto.
- Confirmación explícita antes de operar con dinero real.
- Límites de pérdida obligatorios.
- Logs completos.
- Pruebas previas en paper trading.

Resultado esperado:

- Capacidad técnica para operar, con controles de seguridad antes de activar dinero real.

### Fase 8 — Machine learning futuro

Objetivo: incorporar ML solo cuando entendamos datos, backtesting y riesgo.

Aprenderemos:

- Qué es una variable o feature.
- Qué es una etiqueta o target.
- Entrenamiento, validación y prueba.
- Overfitting.
- Walk-forward validation.
- Por qué predecir precios es distinto de construir una estrategia rentable.

Resultado esperado:

- Modelos experimentales evaluados con rigor, no como cajas mágicas.

## 3. Arquitectura objetivo simplificada

Flujo principal:

1. `data` obtiene o carga datos.
2. `strategy` transforma datos en señales.
3. `risk` acepta, ajusta o rechaza señales.
4. `backtesting` simula qué habría pasado históricamente.
5. `portfolio` calcula posiciones, capital y resultados.
6. `execution` ejecuta órdenes solo en paper trading o, más adelante, en broker real.
7. `logging` registra lo ocurrido para auditoría y aprendizaje.

Separación clave:

- Una señal dice: “creo que conviene comprar, vender o esperar”.
- Una orden dice: “intenta ejecutar esta acción en el mercado”.
- Una operación ejecutada dice: “el mercado aceptó y completó la orden a este precio”.

Esta separación evita uno de los errores más comunes de principiantes: confundir una idea de trading con una ejecución real.

## 4. Versión mínima funcional propuesta

La primera versión de Argoth Trading no usará dinero real, APIs ni machine learning.

Alcance inicial:

- Un archivo CSV con datos históricos.
- Una estrategia de medias móviles.
- Un backtest sencillo.
- Un reporte por consola.
- Pruebas básicas.

No incluirá todavía:

- Trading en vivo.
- Broker real.
- Apalancamiento.
- Criptomonedas en tiempo real.
- Machine learning.
- Optimización automática de parámetros.

Esta restricción es intencional: reduce el riesgo y permite aprender los fundamentos.

## 5. Primera lección — Qué es un sistema de trading algorítmico

Un sistema de trading algorítmico es un programa que sigue reglas explícitas para analizar datos de mercado y decidir si debe comprar, vender o esperar.

Tiene cuatro piezas mínimas:

1. Datos: información del mercado, como precios históricos.
2. Estrategia: reglas que convierten datos en señales.
3. Backtesting: simulación para comprobar cómo habría funcionado la estrategia en el pasado.
4. Riesgo: reglas que limitan cuánto se puede perder.

Ejemplo conceptual:

- Si el precio promedio corto sube por encima del precio promedio largo, la estrategia genera una señal de compra.
- Si el precio promedio corto cae por debajo del precio promedio largo, la estrategia genera una señal de venta.
- El módulo de riesgo decide si esa señal es aceptable según el capital y la pérdida máxima permitida.

## 6. Ejercicio de la primera lección

Antes de programar, responde con tus propias palabras:

1. ¿Cuál es la diferencia entre una señal y una orden?
2. ¿Por qué no debemos conectar un broker real en la primera versión?
3. ¿Qué crees que hace un backtest?
4. ¿Por qué el riesgo debe existir incluso antes de buscar ganancias?

Cuando respondas, revisaremos tus respuestas, corregiremos conceptos y recién después escribiremos el primer código de Argoth Trading.

## 7. Criterio para avanzar

No avanzaremos a la siguiente lección hasta que puedas explicar:

- Qué datos necesita una estrategia básica.
- Qué decisión produce una estrategia.
- Qué problema resuelve el backtesting.
- Qué problema resuelve la gestión de riesgo.
