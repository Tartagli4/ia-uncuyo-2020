# Inteligencia Artificial 1: Fundamentos
**Alumno:** Tartaglia, Juan Ignacio

**Fecha de entrega:** 21/10/2020

## Introducción
En el siguiente documento, se presenta un resumen del **capitulo N° 26**  del libro **"Inteligencia Artificial: Un Enfoque Moderno"** de los autores **Stuart Rusell** y **Peter Norvig**.

Este capitulo del libro tiene 3 subtópicos principales los cuales son:
- **Inteligencia Artificial Débil.**
- **Inteligencia Artificial Fuerte**
- **La ética y los riesgos de desarrollar Inteligencia Artificial.**

## Inteligencia Artificial Débil

Algunos filósofos han intentado demostrar que **la IA es imposible**; que las máquinas no tendrán la posibilidad de actuar inteligentemente. 
>Hipótesis de la IA débil: Afirmación de que es posible que las máquinas actúen con inteligencia.

Obviamente **, si la IA es imposible o no lo es, dependerá de cómo se defina.** En esencia, la IA consiste en la búsqueda del mejor programa agente en una arquitectura dada.

Nuestra definición de IA funciona bien para el problema de encontrar un buen agente, dependiendo de la arquitectura.

Sin embargo, los filósofos están interesados en el problema de comparar dos arquitecturas, la humana y la de la máquina. Además, ellos por tradición han formulado la pregunta de la siguiente manera: **¿Pueden pensar las máquinas?** Desgraciadamente, esta cuestión no está bien definida.

Alan Turing, en su famoso artículo *Computing Machinery and Intelligence* (Turing,1950), sugirió que en vez de preguntar si las máquinas pueden pensar, deberíamos preguntar si las máquinas pueden aprobar un test de inteligencia conductiva (de comportamiento), conocido como el **Test de Turing**. La prueba se realiza para que el programa mantenga una conversación durante cinco minutos (mediante mensajes escritos en línea, online) con un interrogador (interlocutor). Éste tiene que averiguar si la conversación se está llevando a cabo con un programa o con una persona; si el programa engaña al
interlocutor un 30 por ciento del tiempo, este pasará la prueba.

Turing también examinó una gran gama de posibles objeciones ante la posibilidad de las máquinas inteligentes, incluyendo virtualmente aquellas que han aparecido me dio siglo después de que apareciera este artículo. **Examinaremos algunas de ellas.**
###   Argumento de Incapacidad

El *argumento de incapacidad* afirma que *una máquina nunca puede hacer X*. 
>Ejemplos de X: Ser amable, tener recursos, ser guapo, simpático, tener iniciativas, tener sentido del humor, entre otros.

Turing tuvo que utilizar su intuición para adivinar aquello que en un futuro sería posible, pero nosotros tenemos el privilegio de poder mirar hacia atrás y ver qué es lo que ya pueden hacer los computadores. Es innegable que los computadores actualmente hacen muchas cosas que anteriormente eran sólo del dominio humano.

Sin embargo, los algoritmos también funcionan a nivel humano en tareas
que aparentemente se relacionan con el juicio humano, o como apunta Turing, *aprender a partir de la experiencia* y la capacidad de *distinguir lo que es correcto de lo incorrecto*.

### La Objeción Matemática

Es bien conocido, a través de los trabajos de Turing (1936) y Gödel (1931), que **ciertas cuestiones matemáticas no pueden ser respondidas por sistemas formales concretos**. 
El teorema de la incompletitud de Gödel es el ejemplo más conocido en este respecto.
>Teorema de incompletitud:  En resumen, para cualquier sistema axiomático formal F lo suficientemente potente como para hacer aritmética, es posible construir una *sentencia Gödel* G(F) con las propiedades siguientes:
>-  G(F) es una sentencia de F, pero no se puede probar dentro de F. 
>- Si F es consistente, entonces G(F) es verdadero.

Filósofos como J. R. Lucas (1961) han afirmado que este teorema demuestra que las máquinas son mentalmente inferiores a los hombres, porque las máquinas son sistemas formales limitados por el teorema de la incompletitud, es decir no pueden establecer la verdad de su propia sentencia Gödel, mientras que los hombres no tienen dicha limitación.

### El Argumento de la Informalidad
Una de las críticas más persistentes e influyentes de la IA como empresa la realizó Turing mediante su *argumento de la informalidad del comportamiento*. En esencia, esta afirmación consiste en que el comportamiento humano es demasiado complejo para poder captarse mediante un simple juego de reglas y que debido a que los computadores no pueden nada más que seguir un conjunto  de reglas, no pueden generar un comportamiento tan inteligente como el de los hombres. En IA la incapacidad de capturarlo todo en un conjunto de reglas lógicas se denomina **problema de cualificación**.

## Inteligencia Artificial Fuerte
Muchos filósofos han afirmado que una máquina que pasa el Test de Turing no quiere decir que esté realmente pensando, sería solamente una simulación de la acción de pensar.
>Hipótesis de  la IA fuerte:  consiste en la afirmación de que las máquinas sí piensan realmente.

Esto es lo que Turing llama el argumento de la **consciencia**, la máquina 
tiene que ser consciente de sus propias acciones y estados mentales. el punto de vista clave de otro autor (Jefferson) se relaciona realmente con la **fenomenología**, es decir, la máquina tiene que sentir emociones realmente. Otros se centran en la **intencionalidad**, esto es, en la cuestión de si las creencias, deseos y otras representaciones supuestas de la máquina son de verdad algo que pertenece al mundo real.

- **Funcionalismo**: La teoría del funcionalismo dice que un estado mental es cualquier condición causal inmediata entre la entrada y la salida. Bajo la teoría funcionalista, dos sistemas con procesos causales isomórficos tendrían los mismos estados mentales. Por tanto, un programa informático podría tener los mismos estados mentales que una persona.

- **Naturalismo Biológico**: La teoría del naturalismo biológico dice que los estados mentales son características emergentes de alto nivel originadas por procesos neurológicos de bajo nivel en las neuronas, y lo que importa son las propiedades (no especificadas) de las neuronas.

### El Problema Mente-Cuerpo
El problema mente-cuerpo cuestiona cómo se relacionan los estados y los procesos mentales con los estados y los procesos del cuerpo.

**¿Por qué es un problema el problema mente-cuerpo?**
Este se da porque existen dos posturas, la cuales son:
- **Teoría dualista:** un alma inmortal interactúa con un cuerpo mortal, esto quiere decir que el alma y el cuerpo son dos tipos de cosas diferentes. 

- **Materialismo:** No existen cosas tales como almas inmateriales, sino sólo objetos materiales.
El materialista se debe enfrentar por lo menos con dos obstáculos serios. 
  -  El primer problema es el de la **libertad de elección**.

  - El segundo problema tiene que ver con el tema general de la **conciencia** (y cuestiones de **entendimiento** y de **autoconocimiento**
relacionadas, aunque no idénticas).

Para empezar a responder estas cuestiones, necesitamos formas de hablar sobre los estados del cerebro a niveles más abstractos, particularmente las **actitudes proposicionales o estados intencionales**. Estos son estados tales como creer, conocer, desear, temer, y otros más que se relacionan con algunos aspectos del mundo exterior.

Los estados intencionales tienen una conexión necesaria con otros
objetos del mundo externo. Por otro lado hemos argumentado que los estados mentales son estados del cerebro, y de aquí que los estados mentales de identidad o no-identidad se deberían determinar permaneciendo completamente *dentro de la cabeza*, sin hacer referencia al mundo real.

## La Etica y los Riesgos de Desarrollar la Inteligencia Artificial

Hasta ahora nos hemos concentrado en si podemos desarrollar la IA, pero debemos también tener en cuenta si deberíamos hacerlo.

He aquí algunos problemas que se exponen a partir del avance de la IA:

### Las personas podrían perder sus trabajos por la automatización.
 La economía industrial moderna ha llegado a depender en general de los computadores, y selecciona programas de IA en particular.
 
 Hasta ahora, la automatización por medio de la tecnología de la IA ha creado más trabajos de los que ha eliminado, y ha creado puestos de trabajo más interesantes y mejor pagados.
 
### Las personas podrían tener demasiado (o muy poco) tiempo de ocio.
Las personas que trabajan en las industrias muy relacionadas con el conocimiento han descubierto que forman parte de un sistema computarizado integrado que funciona 24 horas al día; para mantenerlo se han visto forzados a trabajar durante más horas.

La IA incrementa el ritmo de la innovación tecnológica y contribuye así a esta tendencia general, pero la IA también mantiene la promesa de permitirnos ahorrar tiempo y permitir que nuestros agentes automatizados hagan las cosas por un tiempo.

### Las personas podrían perder el sentido de ser únicos.
En el libro de Weizenbaum (1976), *Computer Power and Human Reasonautor* se señalan algunas de las posibles amenazas que supone la IA para la sociedad. Uno de los argumentos principales de Weizenbaum es que la investigación en IA hace posible la idea de que los hombres sean autómatas, una idea que produce pérdida de autonomía o incluso de humanidad. **Sin embargo** podemos señalar que la idea de perder este sentido ya existía mucho antes que la IA.

>Algunos ejemplos de esto podrían ser: El desplazamiento a la tierra lejos del centro del sistema solar o el poner al homo sapiens al mismo nivel que otras especies.
>
La IA quizá sea por lo menos amenazante para las suposiciones morales de la sociedad del siglo al igual que la teoría de la evolución XXI lo fue para los del siglo XIX.

### Las personas podrían perder algunos de sus derechos privados.
Weizenbaum también ha señalado que la tecnología del reconocimiento de voz podría llevar a una intercepción extensa de cableados, y de aquí a la pérdida de las libertades civiles.
Algunas personas reconocen que la computarización conduce a la pérdida de privacidad, otros no están de acuerdo.

### La utilización de los sistemas de IA podría llevar a la pérdida de responsabilidad.
En la atmósfera de litigios, la obligación legal se convierte en un tema importante. Esta obligación esta empezando a aparecer en relación con la utilización de agentes inteligentes en Internet. Por ejemplo: se han hecho progresos en la incorporación de limitaciones en los agentes inteligentes de forma que no pueden, por ejemplo, dañar los archivos de otros usuarios.

### El éxito de la IA podría significar el fin de la raza humana.

Casi cualquier tecnología tiene el potencial de hacer daño si se encuentra en las manos equivocadas, pero con la IA y la robótica, tenemos el problema nuevo de que las manos equivocadas podrían pertenecer a dicha tecnología.

Los hombres utilizan su inteligencia de formas agresivas porque son innatas, por naturaleza. Sin embargo, las máquinas que construimos no tienen que ser innatamente agresivas, a menos que decidamos que así sean.

>- **Singularidad Tecnológica:** *Dentro de treinta años, tendremos el medio tecnológico de crear una inteligencia super humana. Algún tiempo después, la era humana habrá acabado*
>- **Trashumanismo:** Movimiento social real que ansía este futuro  de la singularidad tecnológica. 

## Temas Abordados y Resumen Final.

- Los filósofos utilizan el término IA débil para la hipótesis de que las máquinas podrían comportarse posiblemente de forma inteligente, y el término IA fuerte para la hipótesis de que dichas máquinas contarían como si tuvieran mentes reales (en contraposición a las mentes simuladas).

- Alan Turing rechazó la cuestión «¿Pueden pensar las máquinas?», y lo sustituyó por un test de comportamiento. Previeron muchas objeciones a la posibilidad de máquinas pensantes. Pocos investigadores en IA prestan atención al Test de Turing, y prefieren concentrarse en el rendimiento de sus sistemas en base a tareas prácticas, en vez de la habilidad de imitar a los humanos.

-  Actualmente existe el acuerdo general de que los estados mentales son los estados del cerebro.

- Los argumentos a favor y en contra de la IA fuerte no son concluyentes. Unos pocos investigadores dominantes en la disciplina de la IA creen que cualquier cosa significativa gira en torno al resultado del debate.

- La consciencia sigue siendo un misterio.

- Se han identificado ocho amenazas potenciales para la sociedad que se exponen tanto ante la IA como ante una tecnología relacionada. Podemos concluir diciendo que algunas amenazas son improbables, pero merece la pena revisar dos de ellas en particular. La primera es que las máquinas ultra inteligentes podrían llevarnos a un futuro muy diferente del actual y puede que no sea de nuestro agrado. La segunda es que la tecnología de la robótica puede permitir a individuos con una psicopatía emplear armas de destrucción masiva. Concluimos diciendo que esto es más una amenaza de la biotecnología y nanotecnología que de la robótica.
