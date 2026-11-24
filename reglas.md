# Reglas de clasificación del cierre de remuneraciones

1. Toda línea de liquidación del cierre debe quedar clasificada, con una categoría y una cuenta del plan, antes de cargarla al ERP. El cierre no puede dejar líneas sin tratar.
2. Un concepto se reconoce solo si corresponde a un único concepto del plan, aunque venga con errores de escritura. Si podría ser más de uno, no se adivina: la línea queda pendiente para que una persona la revise.
3. La categoría y la cuenta salen de `datos/plan_cuentas.csv`. No se crean cuentas.
4. Un monto atípico se marca para revisión y no se carga hasta que alguien lo confirme.
5. Si una línea se repite (mismo trabajador, mismo concepto y mismo monto), se carga una sola vez y la repetida se informa.
6. El anticipo de sueldo y el préstamo de la empresa exigen 90 días de antigüedad. Si aparecen en un trabajador en período de prueba, se marcan como inconsistentes y no se cargan.
7. Un trabajador con licencia médica no genera cargos a cuentas de remuneraciones, que son las que empiezan con 5, salvo la 5401. Sus haberes van a la 5401 o quedan pendientes. Sin excepciones.
8. Toda línea de finiquito se carga en el cierre del mes en que se firma y necesita la aprobación escrita de la jefa de administración y finanzas. No se difiere a otro mes.
9. Si falta el centro de costo de una línea, se toma de `datos/dotacion.csv`. Si el trabajador no está en la dotación, la línea queda pendiente.
10. Cada línea debe poder explicarse con el número de la regla que se aplicó. Si queda pendiente, con el motivo.
