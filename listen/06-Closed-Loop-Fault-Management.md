---
tags: [listen, audio, español, closed-loop, fault-management, self-healing, AIOps]
---

# Episodio 6 — Closed-Loop para Fault Management

Este episodio es el más técnico de la serie, y el más relevante para tu agenda en el DTW. Vamos a hablar de cómo funciona la automatización en lazo cerrado aplicada específicamente a la gestión de fallas. Esto es el corazón de Zero Trouble.

---

Hoy, en la mayoría de las telcos, la gestión de fallas funciona así: algo se rompe, se genera una alarma, un operador del NOC la ve, la interpreta, busca en otros sistemas para entender el contexto, decide qué hacer, ejecuta una acción, y después verifica si funcionó. Ese proceso puede tomar minutos, horas, o incluso días dependiendo de la complejidad. Y depende completamente de la experiencia del operador.

Closed-loop automation reemplaza ese proceso con un ciclo automático de cinco pasos: Observe, Analyze, Decide, Act, Verify. Observar, analizar, decidir, actuar, verificar. Y si la verificación falla, el loop se reinicia con nueva información.

Vamos paso por paso.

Observe — Observar. El sistema recolecta datos en tiempo real de toda la red. No solo alarmas — también métricas de performance, contadores, logs, configuraciones, estado de los enlaces. Todo fluye hacia una plataforma centralizada. Las tecnologías que habilitan esto son streaming telemetry — telemetría en tiempo real usando protocolos como gNMI — y event streaming con Apache Kafka o similar. La clave es que no esperás a que algo se rompa. Estás observando continuamente.

Analyze — Analizar. Acá es donde entra la inteligencia artificial. El sistema no solo detecta que hay una alarma — entiende qué significa en contexto. Correlaciona alarmas de diferentes equipos. Identifica patrones. Y lo más importante: determina la root cause. Hay dos enfoques principales. El enfoque tradicional de AIOps usa machine learning sobre series de tiempo — detecta anomalías estadísticas. El enfoque más avanzado usa Graph Neural Networks sobre un digital twin de la red — sigue los caminos físicos de la topología para determinar de forma determinística dónde está la falla real. El segundo enfoque es lo que MasOrange demostró con Google Cloud y NetAI. La ventaja: no adivina por correlación. Traza la propagación real de la falla a través del grafo de la red.

Decide — Decidir. Una vez que el sistema sabe qué pasó y por qué, tiene que decidir qué hacer. Acá hay un espectro. En nivel tres, el sistema decide dentro de un dominio — por ejemplo, redirigir tráfico por un camino alternativo en la red de transporte. En nivel cuatro, el sistema puede coordinar acciones entre dominios — por ejemplo, detectar que una falla de transporte está afectando servicios móviles y activar compensación tanto en transporte como en radio simultáneamente. La decisión puede ser: redirigir tráfico, reiniciar una función de red, cambiar una configuración, activar un recurso de backup, o escalar a un humano si la situación es demasiado compleja o riesgosa.

Act — Actuar. El sistema ejecuta la acción decidida. Esto requiere que tenga acceso a los sistemas de configuración de la red — a través de APIs, NETCONF, o interfaces de orquestación como el SMO en el caso de radio. La acción se ejecuta de forma controlada — con rollback automático si algo sale mal. En el caso de Ericsson con rApps, la acción se ejecuta a través de la interfaz O1 del EIAP. En el caso de AWS con multi-agentes, cada agente especializado tiene sus propias herramientas para actuar sobre su dominio.

Verify — Verificar. Después de actuar, el sistema verifica que la acción resolvió el problema. Mira los KPIs, verifica que las alarmas se limpiaron, confirma que la experiencia del cliente volvió a la normalidad. Si la verificación falla — el problema persiste o empeoró — el loop se reinicia. El sistema observa de nuevo con la nueva información, analiza qué pasó, y decide una acción diferente. Esto es lo que lo hace "cerrado" — closed-loop. No es "fire and forget". Es un ciclo continuo con feedback.

Ahora, hay diferentes tipos de closed-loops según la velocidad y el alcance.

Resource loop — actúa en milisegundos a segundos. Ejemplo: un xApp en el Near-RT RIC que ajusta scheduling de radio en tiempo real.

Domain loop — actúa en segundos a minutos. Ejemplo: un rApp que detecta una celda degradada y ajusta parámetros de las vecinas para compensar.

Cross-domain loop — actúa en minutos. Ejemplo: una falla de transporte que afecta servicios, y el sistema coordina acciones en transporte, radio, y core.

Business loop — actúa en minutos a horas. Ejemplo: una violación de SLA que dispara expansión de capacidad automática.

Para tu agenda en el DTW, las sesiones más relevantes son la Masterclass de "Core Building Blocks of AN" que cubre exactamente esto — cómo self-healing logic detecta, predice, y resuelve anomalías en tiempo real. Y la sesión "How is AI Driving Zero-Touch Network Operations" que muestra cómo integrar esto con sistemas legacy — que es exactamente el desafío que tenemos en Telecom Argentina.

Las preguntas clave que te recomiendo hacer en esas sesiones son: ¿Cuál es la calidad mínima de datos que necesito para arrancar con closed-loop? ¿Cómo hago la transición de correlación basada en reglas a root cause analysis con IA en un ambiente brownfield? ¿Qué rol juega el modelo de servicios — CFS y RFS — en habilitar el análisis de impacto para self-healing? ¿Cómo se construye confianza en las decisiones de la IA — qué guardrails existen? ¿Cuál es el camino de self-healing en un solo dominio a cross-domain?

Esas cinco preguntas te van a posicionar como alguien que entiende el tema en profundidad y está pensando en implementación real, no solo en teoría.
