---
tags: [listen, audio, español, Level-4, GenAI, clarification]
---

# Episodio 7 — ¿Se Puede Llegar a Level 4 Sin GenAI?

Este episodio es corto pero importante. Porque en el DTW vas a escuchar a muchos vendors decir que necesitás GenAI para todo. Y la realidad es más matizada.

---

La pregunta es simple: ¿se puede lograr Level 4 de Autonomous Networks sin usar inteligencia artificial generativa? Sin LLMs, sin agentes basados en lenguaje natural, sin ChatGPT ni Amazon Bedrock ni nada de eso.

La respuesta es sí. Absolutamente sí.

Y no es una opinión — es un hecho. Los criterios de Level 4 fueron definidos por TM Forum entre 2019 y 2020. ChatGPT salió a fines de 2022. Los operadores que están logrando Level 4 hoy empezaron a planificar su camino en 2022 y 2023, cuando GenAI todavía no era un factor en sus roadmaps.

¿Qué pide Level 4? Decisiones autónomas cross-domain. Mínima intervención humana. Operaciones predictivas y proactivas. Closed-loop automation entre dominios. Ninguno de estos requisitos dice "necesitás un Large Language Model".

¿Con qué tecnología se logra Level 4 sin GenAI? Con machine learning clásico. Random forests para clasificación de alarmas. LSTM y autoencoders para detección de anomalías. Modelos de series de tiempo como ARIMA o Prophet para predicción de fallas. Reinforcement learning para optimización de parámetros de radio. Graph Neural Networks para root cause analysis — que es lo que usa MasOrange con NetAI y Google Cloud. Policy engines para decisiones basadas en reglas inteligentes. Orquestadores para coordinar acciones cross-domain.

Miremos los casos reales. MasOrange obtuvo Level 4 en mayo de 2026. ¿Qué usaron? GNN para root cause analysis — eso no es GenAI, es machine learning sobre grafos. rApps de Ericsson con modelos de detección de anomalías — eso es supervised learning clásico. Orquestación basada en políticas. El componente de GenAI — el partnership con Google Cloud y NetAI — es un Proof of Concept para agregar explicabilidad. No es lo que les dio la certificación.

Ericsson reporta noventa y ocho por ciento de precisión en detección de anomalías con sus rApps. Eso es machine learning clásico entrenado con datos de trece millones de sitios. No es un LLM.

Ooredoo Kuwait logró Level 4 en 2025 con AIOps, analytics, y plataformas de automatización. Sin mención pública de GenAI como requisito.

Entonces, ¿para qué sirve GenAI en este contexto? Es un acelerador. No un habilitador.

Sin GenAI podés llegar a Level 4, pero necesitás escribir más código custom, más reglas, más playbooks específicos. Con GenAI, podés usar lenguaje natural para definir intenciones. Podés tener agentes que razonan sobre situaciones nuevas que nunca vieron. Podés reducir el tiempo de desarrollo de nuevos use cases. Podés manejar edge cases que ninguna regla anticipó.

Pensalo así. Machine learning clásico es como tener un equipo de especialistas muy buenos en tareas específicas. Cada uno sabe hacer una cosa muy bien — detectar anomalías, predecir fallas, optimizar parámetros. GenAI es como agregar un gerente inteligente que coordina a esos especialistas, entiende el contexto general, y puede improvisar cuando pasa algo inesperado.

Para Level 5 — autonomía total — ahí sí probablemente necesitás GenAI. Porque Level 5 implica tomar decisiones de negocio, manejar situaciones completamente nuevas, y operar sin ninguna intervención humana en ningún escenario. Eso requiere razonamiento general, no solo pattern matching. Pero Level 5 todavía no existe en producción.

El mensaje para llevar al DTW es este: no dejes que te vendan GenAI como prerequisito para empezar el camino a Level 4. Lo que necesitás primero es buena calidad de datos, un modelo de servicios limpio — CFS, RFS, inventarios conectados — y closed-loops bien diseñados. Con eso y machine learning clásico, podés llegar a Level 4. GenAI te va a hacer el camino más rápido y más fácil, pero no es la puerta de entrada.

Y cuando un vendor te diga "necesitás nuestra plataforma de GenAI para autonomous networks", preguntale: "¿Qué operadores lograron Level 4 sin GenAI y con qué tecnología?" La respuesta te va a dar perspectiva.
