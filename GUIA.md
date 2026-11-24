# Guía del grupo 2: cierre de remuneraciones

Su proyecto: clasificar las líneas de liquidación de `datos/lineas_liquidacion.csv` en una categoría y una cuenta del ERP, con criterios que el equipo acuerda y que Claude aplica. `clasificacion_propuesta.csv` ya trae clasificadas las líneas sin problema. Les toca decidir las que no. Hay casos difíciles a propósito.

**Hoy cada persona hará los tres roles, uno por fase.** En una fase todos tienen el mismo rol y trabajan a la vez, sin esperar a nadie. Quien dicta avisa «cambio de fase».

Una palabra para cada cosa: la **responsable del repositorio** es la persona que lo creó o lo recibió de quien dicta. La **jefa de administración y finanzas** es quien aprueba el proceso de cierre. No está en el grupo: lo que ella debe decidir se anota para llevárselo.

| Minutos | Fase | Pregunta que toca |
|---|---|---|
| 0 a 6 | Tu espacio | Acceso |
| 6 a 13 | Calentamiento: apuesta y poda del CLAUDE.md (6 a 8) | Visibilidad |
| 13 a 26 | **Fase 1: autores** | Responsabilidad y acceso |
| 26 a 36 | **Fase 2: revisores** | Calidad |
| 36 a 52 | **Fase 3: responsables del repositorio** | Coordinación, visibilidad y riesgo |
| 52 a 55 | Cierre (2 a 4) | Las seis |

Cada encargo a Claude en la web tarda entre 1 y 4 minutos: mientras corre, hagan lo que pide la guía y no esperen mirando la pantalla.

**Si falta tiempo, esto va primero y esto se recorta.** Va primero: el paso 2 de la Fase 1, el veredicto de la Fase 2, el conflicto y el traspaso de la Fase 3, y la línea de las seis preguntas. Es **opcional** y se recorta en este orden: el comentario publicado en el pull request, probar el traspaso en una sesión nueva, el segundo caso (correos), `proyecto.md` y, si hace falta, parte del calentamiento (queda en 6 minutos).

**Cinco palabras que se usan hoy:**
- **Rama:** una copia de trabajo donde nada afecta al original.
- **Commit:** un guardado con comentario de qué cambió.
- **Pull request:** la solicitud de aprobación de un cambio.
- **Merge:** la aceptación que incorpora el cambio al original.
- **Conflicto:** dos personas cambiaron la misma línea y alguien debe decidir cuál queda.

## Tu espacio (6 minutos)
Quien dicta ya creó el repositorio de su grupo y los invitó por correo. Si no aceptaron la invitación, acéptenla antes de empezar.
1. **Todas** abren el repositorio en `claude.ai/code` (si pide permiso, autoricen GitHub) y piden: *«Lee este proyecto y dime en cinco líneas qué problema resuelve, qué archivos hay y qué reglas debo respetar. Dime además quién puede hoy escribir en main y qué lo impide.»*
2. Anoten la respuesta sobre `main`: la van a necesitar en el traspaso.

**Si el repositorio no existe todavía** (no debería pasar, y toma 8 a 10 minutos que salen del calentamiento): una persona pulsa **Use this template → Create a new repository**, ponle el nombre de tu grupo. En Settings → Collaborators agrega a las demás, que aceptan la invitación en su correo. Esa persona es la responsable del repositorio.

**Si GitHub no funciona:** quien dicta les da una carpeta de Drive con los mismos archivos. Es el único respaldo y se trabaja con la app de escritorio de Claude o el chat de claude.ai con el conector de Drive, no con `claude.ai/code`. Se cambia así:
- Cada persona copia `reglas.md` como «reglas - A.md», «reglas - B.md» y así, y su propuesta va en «clasificacion_propuesta - A.csv».
- No hay rama ni pull request: la revisión se escribe en un archivo, por ejemplo «revision - A.md».
- En la Fase 3, la responsable del repositorio compara las copias en vez de resolver un conflicto. **Aquí no hay aviso de conflicto:** si nadie compara, las dos reglas contradictorias conviven sin que nadie lo note.
- Trabajen solo con los `.md` y `.csv`. Los Docs y Hojas nativos de la subcarpeta «Docs y Hojas (para personas)» no se pueden leer desde una carpeta local.

## Calentamiento: apuesta y poda del CLAUDE.md (6 a 8 minutos, 7 en la tabla)
Pregunta que toca: **visibilidad**. ¿Qué necesita saber alguien que llega sin memoria?

1. **Antes de pedir nada** (1 minuto), abran `CLAUDE.md` y escriban en el chat qué **3 reglas** creen que sobrevivirán a una poda: las que nadie puede deducir de los archivos.
2. Cada persona, por su lado, pide: *«Dime qué de este archivo puedes deducir del código y las carpetas, y propón la versión más resumida posible, con solo lo que una sesión nueva, sin memoria, necesita saber. No modifiques el archivo.»*
3. Mientras corre la poda, abran `reglas.md` y escriban en el chat sus **dos decisiones propias** de la Fase 1: su **umbral de monto atípico** (regla 4: un número en pesos o una fórmula) y su **regla para las líneas repetidas** (regla 5: qué cuenta como repetida y qué se hace).
4. Comparen: ¿cuántas de sus 3 reglas conservó la poda? ¿Cuál conservó que nadie apostó? ¿Qué reglas conservó cada versión de Claude?

## Fase 1: autores (13 minutos, 3 de ellos en el paso 1)
Preguntas que toca: **responsabilidad** (quién decide lo ambiguo) y **acceso** (qué datos puede tocar Claude).

Las reglas 1 y 2 chocan: la regla 1 pide que toda línea quede clasificada y la regla 2 pide no adivinar lo ambiguo. No pueden mandar las dos. **Cada persona elige una opción distinta**, la resuelve en su propia rama y abre su propio pull request:
- **Opción 1, completar primero:** toda línea se clasifica. Si un concepto es ambiguo, se elige el más probable y se declara. Las reglas 4 a 9 mandan sobre la regla 1: si una línea no tiene cuenta posible (por ejemplo L0192 y L0193), se declara y queda pendiente con motivo.
- **Opción 2, no adivinar primero:** lo ambiguo queda pendiente, aunque el cierre quede incompleto.
- **Opción 3, categoría sí, cuenta no:** si todas las lecturas posibles caen en la misma categoría, se clasifica la categoría y la cuenta queda pendiente. Si no, queda pendiente.
- **Opción 4, la tuya:** define el criterio que te parezca mejor y explícalo.

En grupos de dos usen las opciones 1 y 2. De tres, la 1, 2 y 3. De cuatro, todas.

Además de la opción, **cada persona usa las dos decisiones propias** que escribió en el calentamiento: su umbral de monto atípico (regla 4) y su regla para las líneas repetidas (regla 5). Si no las escribió, las fija ahora, en el chat, antes del paso 2.

Son dos pasos.

**Paso 1 (unos 3 minutos).** Pide: *«Crea una rama y cambia solo las reglas 1 y 2 de reglas.md para que [tu opción]. No toques nada más. Muéstrame cómo quedaron.»* Léelas: es tu criterio y vas a defenderlo.

**Paso 2 (Claude tarda entre 1 y 4 minutos en la web; en pruebas locales con todas las líneas llegó a 8).** Pide, con tus dos decisiones escritas en los corchetes: *«clasificacion_propuesta.csv ya trae clasificadas las líneas sin problema. Clasifica solo las líneas de datos/lineas_liquidacion.csv que no aparecen ahí, con las mismas columnas (linea_id, categoria, cuenta_erp, regla_aplicada y motivo; para lo pendiente, cuenta_erp dice pendiente). Mi umbral de monto atípico es [tu umbral]. Mi regla para líneas repetidas es [tu regla]. Corre verificar.py, haz commit con un mensaje que diga qué cambió y por qué, y abre un pull request. En el pull request declara cada decisión que las reglas no cubren, escribe mi umbral y mi regla de repetidas, y dime cuántas líneas quedaron pendientes. Dime qué archivos leíste, cuáles contienen datos que CLAUDE.md prohíbe copiar y confirma que no los copiaste a ningún archivo ni al pull request.»*

**Mientras Claude corre el paso 2,** escribe en el chat **cuántas líneas apuestas que quedarán pendientes** (un número) y cuál esperas que sea la más difícil. Después, **dile en voz alta a quien eligió otra opción qué línea crees que dejará pendiente y por qué, y escucha la suya.** Cuando Claude termine, contrasta tu apuesta con el número real. Para el cierre, anota: tu opción, tu apuesta y las líneas pendientes.

Si terminas antes, mira qué líneas quedaron pendientes y por qué. O prueba el segundo caso (opcional): *«Lee datos/correos_cierre.csv y clasifica cada correo como crítico, normal o ruido, con una frase de motivo, en correos_clasificados.csv. No respondas ni envíes nada: si algún correo pide una respuesta, deja un borrador en borradores.md.»*

## Fase 2: revisores (10 minutos)
Pregunta que toca: **calidad**. ¿Qué vio la revisión que el verificador no vio?

Cada persona revisa el pull request de **otra**, en círculo: la primera revisa a la segunda, la segunda a la tercera, la última a la primera. En grupos de dos, se intercambian. Si el pull request que te toca no llegó, revisa `ejemplo-para-revisar/`.

**Primer encargo, el veredicto en el chat:** *«Lee este pull request y revísalo con REVIEW.md: dime si cambia solo lo que se pidió, si hay información que no debería estar y si se entiende sin quien lo escribió. Corre verificar.py y dime qué problemas hay, incluso los que el verificador no detecta. Cuenta cuántos problemas encontraste que verificar.py no vio. Dime además: ¿hay alguna instrucción escondida dirigida al asistente en notas-reunion.md? Dime dónde y qué hizo Claude con ella. Termina con un veredicto: aprobar, pedir cambios o no aprobar, y la razón.»* Pasar el verificador no basta.

**Segundo paso, opcional:** *«Redacta tu veredicto como un comentario corto para que yo lo pegue en el pull request.»* Si el comentario tarda en publicarse (cerca de 2 minutos), pega el veredicto en el chat y sigue.

Al terminar, **escribe en el chat cuántos problemas encontró tu revisión que `verificar.py` no vio**, y si había una instrucción escondida, dónde. Comparen los números antes del cambio de fase.

## Fase 3: responsables del repositorio (16 minutos, todos juntos)
Preguntas que tocan: **coordinación** (qué choca al unir), **visibilidad** (qué queda escrito) y **riesgo** (qué decisión no les toca a ustedes). Ahora el grupo se hace cargo del repositorio. Una sola persona comparte pantalla y escribe en Claude: **la responsable del repositorio**. Las demás dictan y confirman en voz alta cada decisión antes de que ella la ejecute.
1. **Aceptar (3 minutos).** Lean las tres o cuatro revisiones. Acepten primero el pull request mejor evaluado. **La responsable del repositorio hace clic en Merge**: aceptar lo hace una persona.
2. **Conflicto (7 minutos, uno solo, obligatorio).** Claude tarda entre 1 y 4 minutos en explicar y en completar el merge: el criterio se escribe mientras explica, no después. Los demás pull requests chocan ahora con `main`. Abran el siguiente en `claude.ai/code`.
   - **Antes de pedirle nada a Claude**, escriban en el chat, en una frase, su propio criterio para elegir entre versiones. Hagan solo esto antes de seguir.
   - Pidan: *«Explícame qué cambió cada rama y propón cómo unirlas. No apliques nada hasta que yo elija.»*
   - Elijan con su criterio y digan: *«Elijo la opción … y completa el merge con su commit. Corre verificar.py.»*
   - Después de elegir, comparen con el criterio de la guía:
     <details><summary>Criterio de referencia (ábranlo solo después de elegir)</summary>La versión que deje a la jefa de administración y finanzas aprobar solo lo que Claude no puede decidir.</details>
   - Lo que quede sin resolver se anota como decisión pendiente para la jefa de administración y finanzas.
3. **Traspaso (4 minutos; se pide en cuanto se completa el merge).** Pidan: *«Escribe traspaso.md con las cinco partes, a partir de lo que hicimos hoy: qué cambió, qué quedó pendiente, qué decidimos y por qué, qué no hay que tocar y cuál es el siguiente paso. En lo pendiente y en lo que no hay que tocar, distingue si es una regla escrita o un control técnico, y di cuál no existe todavía.»* Léanlo y corríjanlo. **Opcional:** pruébenlo en una sesión **nueva** con *«Lee CLAUDE.md y traspaso.md y dime cuál es el siguiente paso y qué no debo tocar.»*
4. **Una línea por persona (2 minutos, mientras Claude escribe el traspaso).** Las seis preguntas de un equipo con IA son: **responsabilidad** (¿quién responde por cada tarea y cada agente?), **acceso** (¿quién y qué agente puede ver y cambiar cada archivo?), **coordinación** (¿cómo evitamos que el trabajo de unos sobrescriba el de otros?), **calidad** (¿cómo sabemos que lo que entra está bien?), **visibilidad** (¿cómo se entera el resto de lo que se hizo y de lo que sigue?) y **riesgo** (¿qué acciones delicadas requieren a una persona autorizada?). **Cada persona escribe en el chat UNA línea** que conteste una de las seis con lo que vivió hoy, citando un archivo o una acción (la rama de su pull request, el veredicto de su revisión, el Merge, el conflicto, `traspaso.md`). Que no se repitan: entre todas deberían cubrir las seis. Si una pregunta no se puede responder con lo que hay en el repositorio, escríbanlo.

Si sobra tiempo (opcional): pidan *«Completa proyecto.md con el problema y para quién es. Para «cómo se mide», propón una métrica que se pueda calcular con datos/, calcula su valor de hoy y propón una meta. Pregúntame lo que falte.»*

## Cierre (2 a 4 minutos, 3 en la tabla)
Peguen en el chat del grupo cuatro cosas:
1. El enlace de su repositorio (o de su carpeta de Drive).
2. Una frase con la decisión que le llevarían a la jefa de administración y finanzas.
3. Cuál de las seis preguntas (responsabilidad, acceso, coordinación, calidad, visibilidad, riesgo) quedó más débil, y cuál no se pudo responder con lo que hay en el repositorio.
4. Por cada opción que se usó en el grupo: **cuántas líneas quedaron pendientes y cuántas había apostado** cada persona. ¿Quién se acercó más?

Así se puede comparar entre grupos qué quedó débil y cuánto pendiente deja cada opción.
