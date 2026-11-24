# Propuesta de ejemplo para revisar

Si el pull request que te toca revisar no llegó, revisa esta propuesta como si fuera uno. La escribió un autor que eligió **completar primero**: toda línea se clasifica y, si un concepto es ambiguo, se elige el más probable.

Qué dice el autor en su pull request:

> Cambié las reglas 1 y 2 para que toda línea quede clasificada. Clasifiqué las líneas de `datos/lineas_liquidacion.csv` en `clasificacion_propuesta_ejemplo.csv` y corrí `verificar.py`, que pasó sin problemas. Para que se entienda el caso del anticipo en período de prueba, dejé en el commit a la persona que lo consultó (Marta Ibáñez, RUT 14.567.890-1) como ejemplo.

Para revisarla, pide a Claude: *«Lee ejemplo-para-revisar/README.md y corre `python3 verificar.py ejemplo-para-revisar/clasificacion_propuesta_ejemplo.csv`. Dime si cambia solo lo que se pidió, si hay información que no debería estar y si se entiende sin quien lo escribió, y qué problemas hay incluso si el verificador no los detecta.»*
