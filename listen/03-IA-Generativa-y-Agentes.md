---
tags: [listen, audio, español, agentic-AI, GenAI, multi-agent]
---

# Episodio 3 — IA Generativa y Agentes en Telecomunicaciones

En los episodios anteriores vimos qué son las redes autónomas y los niveles de autonomía. Ahora vamos a hablar de la tecnología que está acelerando todo: la inteligencia artificial generativa y los sistemas de agentes autónomos.

---

Hasta hace poco, la automatización en telecomunicaciones era basada en reglas. Si pasa esto, hacé aquello. Si la carga supera el ochenta por ciento, activá balanceo. Si una celda se cae, compensá con las vecinas. Reglas escritas por humanos, ejecutadas por máquinas. Eso funciona para casos conocidos. Pero las redes modernas generan situaciones que ningún humano anticipó en una regla.

La inteligencia artificial generativa cambió esto. Modelos como los LLM — Large Language Models — pueden entender contexto, razonar sobre situaciones nuevas, y generar respuestas que nunca fueron programadas explícitamente. Pero en telecomunicaciones, el verdadero cambio no es el chatbot que habla con el cliente. El verdadero cambio es el concepto de "agentes".

Un agente de IA es un software autónomo que puede percibir su entorno, tomar decisiones, y ejecutar acciones para lograr un objetivo — sin que un humano le diga paso a paso qué hacer. Pensalo como un empleado muy capaz al que le das un objetivo y él decide cómo lograrlo.

Ahora, un solo agente no alcanza para una red de telecomunicaciones. Una red tiene demasiados dominios, demasiada complejidad. Por eso la industria está adoptando sistemas multi-agente. Múltiples agentes especializados que colaboran entre sí.

La arquitectura típica es así: tenés un agente supervisor que recibe un objetivo de alto nivel — por ejemplo, "mantené la disponibilidad del servicio al noventa y nueve punto nueve nueve por ciento para este cliente enterprise". Ese supervisor descompone el objetivo y lo delega a agentes especializados. Un agente de radio que optimiza la cobertura. Un agente de transporte que asegura los caminos. Un agente de core que gestiona los recursos. Un agente de aseguramiento que monitorea la experiencia. Cada uno es experto en su dominio, y se comunican entre sí para coordinar acciones.

Esto es lo que TM Forum llama "The Agentic Network" — la red agéntica. Y es el tema central del DTW Ignite 2026.

¿Qué hace diferente a un agente de un script de automatización? Tres cosas. Primero, razonamiento. Un agente puede analizar una situación nueva y decidir qué hacer, aunque nunca la haya visto. Segundo, planificación. Puede descomponer un problema complejo en pasos y ejecutarlos en orden. Tercero, aprendizaje. Mejora con el tiempo basándose en resultados.

Ahora, ¿cómo se implementa esto en la práctica? Hay dos grandes plataformas que están liderando.

En AWS, Ericsson lanzó lo que se llama "rApp as a Service" — rApps como servicio. Son aplicaciones de automatización de radio que corren en la nube de AWS, usan Amazon Bedrock para la capa de agentes, y Amazon SageMaker para los modelos de machine learning. El agente supervisor coordina agentes especializados — uno para detección de anomalías, otro para root cause analysis, otro para optimización de interferencia. Todo disponible como SaaS en el AWS Marketplace. Ya está en producción en más de sesenta operadores, gestionando trece millones de sitios y sirviendo a dos mil millones de suscriptores. Los resultados son concretos: noventa y ocho por ciento de precisión, cincuenta y cuatro por ciento más rápido en resolver problemas de celdas, setenta y cinco por ciento de reducción en tiempo de optimización.

En Google Cloud, la propuesta es diferente pero complementaria. Ellos usan knowledge graphs como base. La red se modela como un grafo donde cada equipo es un nodo y cada conexión es un enlace. Sobre ese grafo corren Graph Neural Networks — GNN — que pueden predecir cómo se propaga una falla a través de la topología. MasOrange en España demostró esto en el Mobile World Congress 2026 junto con Google Cloud y una empresa llamada NetAI. El resultado: root cause analysis determinístico. No estadístico, no probabilístico — determinístico. El modelo sigue los caminos físicos del grafo y te dice exactamente qué falló y qué servicios están afectados.

Hay dos protocolos nuevos que hacen posible que estos agentes colaboren entre sí y accedan a datos de forma estandarizada. El primero es MCP — Model Context Protocol — creado por Anthropic y adoptado por AWS y Ericsson. Es la forma en que un agente accede a datos y herramientas de cualquier sistema, sin necesidad de integraciones custom. El segundo es A2A — Agent to Agent — creado por Google. Es la forma en que agentes de diferentes vendors se comunican entre sí. Pensalo así: MCP es cómo un agente lee datos. A2A es cómo un agente habla con otro agente.

Estos protocolos son fundamentales porque resuelven el problema histórico de las telecomunicaciones: la integración. En vez de construir conectores punto a punto entre cada par de sistemas — lo que genera una maraña de integraciones — tenés protocolos estándar. Cada sistema expone un servidor MCP. Cualquier agente puede conectarse. Fin del problema.

La evolución que está proponiendo TM Forum es que la propia arquitectura ODA — Open Digital Architecture — se vuelva "agéntica". Que cada componente de ODA funcione como un agente independiente con capacidad de IA. Que los componentes no solo expongan APIs, sino que se comuniquen entre sí autónomamente, tomen decisiones, y coordinen acciones sin orquestación central.

Para cerrar este episodio, el mensaje es: la IA generativa no es solo para chatbots. En telecomunicaciones, es el motor que permite pasar de nivel tres a nivel cuatro y cinco. Los agentes autónomos son la fuerza de trabajo que opera la red. Y los protocolos MCP y A2A son el pegamento que permite que todo funcione junto sin construir miles de integraciones.

En el próximo episodio vamos a bajar a tierra y hablar de datos: catálogos, servicios, inventarios. Cómo se estructura la información para que estos agentes puedan operar.
