---
tags: [listen, audio, español, an-levels, maturity]
---

# Episodio 2 — Los Niveles de Autonomía (L0 a L5)

En el episodio anterior hablamos de qué son las redes autónomas. Ahora vamos a recorrer los seis niveles que define TM Forum para medir qué tan autónoma es una red. Pensalo como los niveles de conducción autónoma de los autos — del cero al cinco.

---

Nivel cero. Operaciones manuales. Todo lo hace un humano. Cada configuración, cada diagnóstico, cada cambio. El sistema no ayuda en nada. Esto ya casi no existe en su forma pura, pero hay dominios de la red donde todavía se opera así — especialmente en redes legacy o equipos viejos que no tienen APIs.

Nivel uno. Operaciones asistidas. El sistema te da información — dashboards, alertas, reportes — pero vos tomás todas las decisiones y ejecutás todas las acciones. Es como tener un GPS que te muestra el mapa pero no te dice por dónde ir. Ejemplos típicos: monitoreo con Grafana, alertas por SNMP, Zero Touch Provisioning básico donde el equipo se registra solo pero vos activás el servicio manualmente.

Nivel dos. Autonomía parcial. Acá el sistema empieza a ejecutar tareas bajo tu supervisión. Vos definís las reglas y las políticas, y el sistema las ejecuta. Pero vos seguís decidiendo. Es como un piloto automático que mantiene la altitud, pero vos decidís cuándo girar. Ejemplos: SON — Self-Organizing Networks — que ajusta parámetros de radio automáticamente dentro de límites que vos definiste. Orquestadores que ejecutan workflows de provisioning de punta a punta. Playbooks de Ansible que se disparan ante ciertas alarmas. La mayoría de los operadores del mundo están acá hoy.

Nivel tres. Autonomía condicional. Este es un salto importante. El sistema empieza a tomar decisiones por sí solo, pero dentro de un dominio específico. Ya no solo ejecuta reglas — usa inteligencia artificial para decidir qué hacer en situaciones que las reglas no cubren. El humano supervisa y puede intervenir, pero no está en cada decisión. Ejemplos: rApps con machine learning que optimizan la red de radio en tiempo real. Modelos predictivos que detectan que una celda va a fallar dos horas antes y activan compensación automática. Gestión dinámica de energía que apaga capas de capacidad cuando no hay tráfico. La diferencia clave con nivel dos: en nivel dos el sistema sigue reglas fijas. En nivel tres, el sistema aprende y decide cosas nuevas.

Nivel cuatro. Alta autonomía. Acá es donde la industria está poniendo toda la energía ahora. El sistema opera autónomamente a través de múltiples dominios sin pedir permiso. No solo optimiza la radio — coordina radio, transporte, core y servicios de forma integrada. El humano pasa de "supervisor" a "manejador de excepciones". Solo interviene cuando algo realmente inusual pasa. Ejemplos reales: MasOrange en España logró la certificación de nivel cuatro en mayo de 2026. Su red puede anticipar fallas y proteger la experiencia del cliente ante cualquier anomalía. Ooredoo en Kuwait también lo logró. Ericsson y KDDI demostraron optimización autónoma de uplink en un cluster de mil quinientas celdas 5G. La clave del nivel cuatro es la palabra "cross-domain" — cruzar dominios. Ya no es autonomía dentro de una caja. Es autonomía de punta a punta.

Nivel cinco. Autonomía total. La red opera completamente sola. No necesita intervención humana para nada. Toma decisiones de negocio, no solo técnicas. Se auto-evoluciona. Nadie llegó acá todavía. Es el horizonte. Algunos Catalysts del TM Forum están explorando cómo sería — por ejemplo, el proyecto "Evolving to Full Network Autonomy" que usa AIOps, digital twins y GenAI para demostrar autonomía completa en un ambiente controlado.

Ahora, algo importante. La certificación de niveles no es "toda la red es nivel X". Es por dominio. Podés tener nivel cuatro en gestión de fallas de radio, pero nivel dos en provisioning de servicios fijos. Por eso TM Forum usa una herramienta llamada ANLET — Autonomous Network Levels Evaluation Tool — que evalúa cada dominio por separado.

¿Y cómo se mide? Se evalúan cinco dimensiones: awareness — qué tan bien el sistema percibe lo que pasa. Analysis — qué tan bien procesa y entiende. Decision — si puede decidir solo. Execution — si puede actuar solo. Y learning — si mejora con el tiempo.

Para darte números concretos de la industria: según TM Forum, alcanzar madurez en redes autónomas puede generar hasta un cincuenta y cinco por ciento de reducción en costos de operación y mantenimiento, un setenta y uno por ciento de mejora en satisfacción del cliente, y un veintiuno por ciento de ahorro en energía.

El mensaje clave es este: no es un salto de cero a cinco. Es un viaje progresivo. Y cada nivel tiene valor. Pasar de nivel dos a nivel tres ya genera impacto enorme en eficiencia. No necesitás llegar a nivel cinco para ver resultados.

En el próximo episodio vamos a hablar de la tecnología que está acelerando todo esto: la inteligencia artificial generativa y los agentes autónomos. Cómo cambiaron las reglas del juego y por qué todos en la industria están hablando de "agentic AI".
