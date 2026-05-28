---
tags: [listen, audio, español, vendors, use-cases, production, MasOrange, AWS, Ericsson]
---

# Episodio 98 — Casos Reales: Vendors y Logros

Este es el último episodio. Vamos a recorrer casos concretos de operadores que están implementando redes autónomas en producción. Quiénes son, con qué tecnología lo hacen, y qué resultados obtuvieron. Esto es lo que vas a ver en vivo en el DTW Ignite.

---

Empecemos con MasOrange en España. MasOrange nació de la fusión de Orange España y MASMOVIL en 2024. Es el operador más grande de España por cantidad de clientes — cuarenta y un millones de líneas. Y en mayo de 2026 se convirtió en el primer operador de España en obtener la certificación de nivel cuatro del TM Forum. ¿Qué significa eso en la práctica? Que su red puede anticipar fallas y proteger la experiencia del cliente ante cualquier anomalía, sin intervención humana.

MasOrange no usó una sola tecnología. Combinó tres enfoques diferentes para distintos dominios de la red.

Para la red de radio, trabaja con Ericsson. Desplegaron la plataforma EIAP — Ericsson Intelligent Automation Platform — con su capa de SMO y rApps. Las rApps son aplicaciones de inteligencia artificial que optimizan la radio automáticamente. Tienen una que detecta anomalías en celdas de forma proactiva, y otra que optimiza el consumo de energía sin impactar el servicio. Esto está en producción desde diciembre de 2025. Un tercio de su red 5G ya es compatible con O-RAN, lo que permite integrar rApps de múltiples vendors.

Para la capa de observabilidad y root cause analysis, trabaja con Google Cloud y una empresa llamada NetAI. Acá la tecnología es diferente: usan Graph Neural Networks sobre un digital twin de la red construido con Google Spanner Graph. La idea es que la red se modela como un grafo, y cuando hay una falla, el modelo de IA sigue los caminos físicos del grafo para determinar la root cause de forma determinística. No adivina por correlación estadística — traza el camino real de la falla. Esto lo demostraron en el Mobile World Congress 2026 en Barcelona.

Para la red de transporte, MasOrange está usando inteligencia artificial para predecir fallas, optimizar rutas, y gestionar energía de forma autónoma. Lograron dos terabits por segundo de capacidad en su red de transmisión en Madrid. Y la directora de transmisión de MasOrange dijo algo clave: "La inteligencia artificial nos está obligando a repensar los fundamentos de cómo funciona nuestra red".

Ahora pasemos a lo que está pasando en AWS. Ericsson y AWS lanzaron juntos lo que se llama "Agentic rApp as a Service". Es una solución SaaS — Software as a Service — disponible en el AWS Marketplace. Básicamente, es la inteligencia de optimización de radio de Ericsson corriendo en la nube de AWS, con agentes de IA coordinados por Amazon Bedrock.

Los números son impresionantes. Está desplegado en más de sesenta operadores. Gestiona trece millones de sitios. Sirve a dos mil millones de suscriptores. Genera más de cien millones de inferencias de IA por día. Y los resultados medidos en campo son: noventa y ocho por ciento de precisión en detección de anomalías. Cincuenta y cuatro por ciento más rápido en resolver problemas de celdas. Setenta y cinco por ciento de reducción en tiempo y esfuerzo de optimización. Cuarenta y tres por ciento de mejora en throughput de downlink en celdas con problemas. Y cuatro por ciento de ganancia en eficiencia espectral.

La arquitectura usa un agente supervisor que coordina agentes especializados — uno para detección de anomalías, otro para root cause analysis, otro para optimización de interferencia, otro para cell shaping. Se comunican a través de interfaces estándar O-RAN — R1 y O1 — y soportan los protocolos MCP y A2A para integración con otros sistemas del operador.

AWS también publicó una arquitectura de referencia open source para operaciones de red con multi-agentes. Usa Amazon Bedrock con modelos Nova, funciones Lambda, y está disponible en GitHub para que cualquiera lo despliegue. La idea es un asistente de operaciones de red donde un agente supervisor coordina tres agentes especializados: uno de mantenimiento, uno de alarmas, y uno de KPIs. El operador pregunta en lenguaje natural "¿cuál es el estado del sitio Dallas uno?" y el sistema consulta los tres agentes en paralelo y te da una respuesta integrada.

BT Group en el Reino Unido es otro caso interesante. Están construyendo una red 5G Standalone con capacidad de self-healing usando agentes de IA sobre AWS. Sirven a treinta millones de suscriptores. Su visión es una red intent-based — donde declarás lo que querés y la red se configura sola.

Telkomsel en Indonesia desarrolló un sistema llamado CELYNA — un sistema de análisis de incidentes potenciado por IA generativa usando Amazon Nova Pro. Transformó sus operaciones de IT de reactivas a proactivas. Lo que antes tomaba horas ahora toma minutos.

NEC en Japón demostró orquestación autónoma de funciones de red del core — específicamente UPF, la función de plano de usuario — usando agentes de IA sobre AWS. Lo mostraron en el MWC 2026.

Del lado de Google Cloud, además de MasOrange, están trabajando con Deutsche Telekom y Vodafone en operaciones autónomas. Y con One NZ — el operador de Nueva Zelanda — están probando agentes autónomos que gestionan el core de voz y la red OSS, moviéndose más allá del monitoreo hacia la ejecución activa — como redirigir tráfico o resetear configuraciones para restaurar calidad de llamadas.

Nokia también está empujando fuerte, especialmente en redes fijas. Lanzaron capacidades de IA agéntica para redes de hogar y banda ancha. Su plataforma Altiplano gestiona más de seiscientos millones de líneas de banda ancha desplegadas. Y están usando IA para automatizar el despliegue de fibra, la optimización de WiFi en el hogar, y el diagnóstico de fallas en la red de acceso.

Huawei tiene su propia propuesta con iMaster NCE y MAE — Mobile Automation Engine. Telecom Argentina, nuestra empresa, desplegó la solución Xinghe AI Ultra-Resilient Fabric de Huawei para sus ocho data centers. Y Huawei reporta que operadores como China Mobile están alcanzando nivel cuatro en dominios específicos.

Un dato importante: Ericsson y Nokia anunciaron en el MWC 2026 que van a integrar sus plataformas de automatización para acelerar el desarrollo de redes autónomas. Esto es significativo porque históricamente cada vendor tenía su ecosistema cerrado. Que los dos principales vendors de radio se pongan de acuerdo en interoperabilidad de automatización es una señal clara de hacia dónde va la industria.

Para cerrar, hay un punto que quiero que te lleves. Esto no es solo para redes móviles. Nokia está automatizando redes de fibra. Cisco tiene Crosswork para redes de transporte. Juniper tiene Apstra para redes empresariales. El TM Forum tiene un Catalyst específico para "Intelligent Fixed Broadband Operations". La autonomía aplica a todos los dominios de red — móvil, fijo, transporte, core, enterprise.

Y Telecom Argentina ya es parte de este movimiento. Somos signatarios del Manifiesto de Redes Autónomas del TM Forum desde 2023. Junto con Intraway e Iquall Networks — dos empresas argentinas que también firmaron. Tenemos el despliegue de Huawei en nuestros data centers. Tenemos artículos publicados en TM Forum Inform sobre nuestra transformación cloud y nuestro enfoque de Team Topologies. Y estamos yendo al DTW Ignite 2026 a ver de primera mano cómo la industria está haciendo todo esto realidad.

Eso es todo. Cinco episodios que cubren desde el concepto hasta la implementación. Espero que te sirvan para llegar a Copenhagen con una base sólida y poder aprovechar al máximo cada sesión, cada demo, y cada conversación en el evento. Buen viaje.
