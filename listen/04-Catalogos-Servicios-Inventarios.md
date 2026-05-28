---
tags: [listen, audio, español, CFS, RFS, catalog, inventory, SID]
---

# Episodio 4 — Catálogos, CFS, RFS e Inventarios

En este episodio vamos a hablar de algo que parece aburrido pero es absolutamente crítico: cómo se estructura la información en una telco para que las redes autónomas puedan funcionar. Sin datos bien organizados, ningún agente de IA puede tomar buenas decisiones.

---

Empecemos con una pregunta simple. Cuando un cliente contrata "Internet 500 megas", ¿qué es eso para la red? Para el cliente es una cosa simple — tiene internet rápido. Pero para la red, eso implica un montón de cosas técnicas: un puerto en un OLT configurado, una ONT activada, una VLAN asignada, un perfil de QoS aplicado, una dirección IP entregada. El cliente ve una cosa. La red hace diez cosas.

TM Forum resuelve esto con un modelo de tres capas llamado PSR: Producto, Servicio, Recurso.

La capa de Producto es lo que vendés. "Plan Fibra 500 megas con TV y teléfono". Tiene precio, tiene condiciones comerciales, tiene elegibilidad. Es lo que ve el área de marketing y ventas.

La capa de Servicio es lo que entregás. Y acá viene lo interesante, porque se divide en dos: CFS y RFS.

CFS significa Customer Facing Service — servicio orientado al cliente. Es una descripción del servicio desde la perspectiva del cliente, pero sin decir cómo se implementa técnicamente. Por ejemplo: "Acceso a Internet 500 Megabits". No dice si es por GPON, por HFC, o por 5G. Es agnóstico de la tecnología. Esto es clave porque el mismo CFS puede entregarse de diferentes formas según la zona o la tecnología disponible.

RFS significa Resource Facing Service — servicio orientado al recurso. Es la traducción técnica del CFS. Dice exactamente qué hay que hacer en la red. "Activar puerto GPON en OLT tal, asignar VLAN cien, aplicar perfil de velocidad quinientos megas, entregar IP por DHCP". Es específico de la tecnología y del dominio de red.

La relación es: un CFS se descompone en uno o más RFS. Y cada RFS se mapea a recursos físicos o lógicos de la red.

La capa de Recurso es lo que operás. Los equipos físicos — routers, OLTs, antenas, fibra. Y los recursos lógicos — VLANs, direcciones IP, puertos, funciones de red virtualizadas.

Ahora, dentro de cada capa hay dos conceptos: catálogo e inventario.

El catálogo es el menú. Define qué puede existir. Es la plantilla. "Tenemos un servicio que se llama Internet 500 megas, que requiere estos RFS, que usa estos recursos". Es como la carta de un restaurante.

El inventario es la realidad. Dice qué existe ahora mismo. "El cliente Juan Pérez tiene activo el servicio Internet 500 megas, implementado con estos RFS específicos, usando estos recursos específicos en esta dirección". Es como las órdenes que están siendo servidas en este momento.

Entonces tenés seis combinaciones: catálogo de productos, inventario de productos, catálogo de servicios, inventario de servicios, catálogo de recursos, inventario de recursos. Cada uno gestionado por un componente de ODA y expuesto a través de APIs estándar del TM Forum.

Las APIs más importantes son: TMF 620 para catálogo de productos. TMF 633 para catálogo de servicios. TMF 638 para inventario de servicios. TMF 639 para inventario de recursos. TMF 641 para órdenes de servicio.

¿Y por qué todo esto importa para redes autónomas? Porque sin esta estructura, un agente de IA no puede hacer análisis de impacto. Si se corta una fibra, el agente necesita saber: ¿qué recursos están afectados? ¿Qué RFS dependen de esos recursos? ¿Qué CFS dependen de esos RFS? ¿Qué clientes tienen esos CFS? Sin la cadena completa — recurso, RFS, CFS, cliente — no podés hacer self-healing inteligente.

Ahora, todo esto se describe usando un lenguaje común llamado SID — Shared Information and Data model. SID es el vocabulario estándar de TM Forum. Define qué es un "Servicio", qué atributos tiene, cómo se relaciona con otros objetos. Es como un diccionario que todos los sistemas de una telco deberían hablar. Si tu sistema de inventario y tu sistema de aseguramiento hablan SID, pueden entenderse sin traducciones custom.

En la práctica, SID se materializa como estructuras JSON a través de las APIs. Un servicio en el inventario tiene un ID, un estado, un tipo — CFS o RFS —, características como clave-valor, referencias a los servicios que lo soportan, referencias al cliente, y referencia a la ubicación. Todo estandarizado.

El patrón más importante de SID es el de "especificación e instancia". Cada cosa tiene una plantilla — la especificación — y ocurrencias reales — las instancias. La especificación vive en el catálogo. La instancia vive en el inventario. Cuando provisionás un servicio, estás creando una instancia a partir de una especificación.

Otro patrón clave es el de características flexibles. En vez de tener columnas fijas en una base de datos, SID usa pares clave-valor. "Velocidad de bajada: 500 megas". "Tecnología de acceso: GPON". Esto permite modelar cualquier servicio sin cambiar el esquema de la base de datos.

Y el tercer patrón fundamental es el de relaciones. "Este CFS está soportado por estos RFS". "Este RFS usa estos recursos". "Este servicio pertenece a este cliente". Estas relaciones son las que permiten navegar la cadena de impacto. Y son exactamente lo que un knowledge graph modela de forma nativa.

Por eso la industria está convergiendo hacia knowledge graphs como base del inventario. Porque una red ES un grafo — equipos conectados por enlaces, servicios que recorren caminos. Modelarla como tablas relacionales con foreign keys es forzar una estructura plana sobre algo que es inherentemente un grafo.

El problema real en la mayoría de las telcos hoy es que esta información está fragmentada. El inventario de red está en un sistema. El inventario de servicios en otro. El catálogo de productos en otro. Y no están bien conectados. No hay un mapeo limpio de CFS a RFS a recurso. Eso hace imposible el análisis de impacto automático.

La solución que propone la industria es construir un digital twin que unifique toda esta información en un grafo en tiempo real. El digital twin no reemplaza los sistemas existentes. Se alimenta de ellos. Pero provee una vista unificada que los agentes de IA pueden consultar para tomar decisiones.

En el próximo y último episodio vamos a ver casos concretos: qué operadores están haciendo esto realidad, con qué vendors, y qué resultados están logrando.
