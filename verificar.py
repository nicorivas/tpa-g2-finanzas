#!/usr/bin/env python3
"""Verifica que clasificacion_propuesta.csv no rompa las reglas duras. Uso: python3 verificar.py [archivo.csv]
El archivo debe tener las columnas: linea_id, categoria, cuenta_erp, regla_aplicada (y motivo). Una línea pendiente lleva «pendiente» en cuenta_erp."""
import csv, sys
plan = {r["cuenta_erp"]: r for r in csv.DictReader(open("datos/plan_cuentas.csv"))}
lineas = {r["linea_id"] for r in csv.DictReader(open("datos/lineas_liquidacion.csv"))}
errores, filas = [], list(csv.DictReader(open(sys.argv[1] if len(sys.argv) > 1 else "clasificacion_propuesta.csv")))
vistos = {f["linea_id"] for f in filas}
for n in sorted(lineas - vistos): errores.append(f"{n}: no aparece en la propuesta")
for f in filas:
    n, cta = f["linea_id"], f["cuenta_erp"].strip()
    if n not in lineas: errores.append(f"{n}: no es una línea del cierre"); continue
    if cta.lower() == "pendiente": continue
    if cta not in plan: errores.append(f"{n}: regla 3, la cuenta {cta} no está en el plan"); continue
    if f["categoria"].strip() != plan[cta]["categoria"]:
        errores.append(f"{n}: regla 3, la cuenta {cta} es de «{plan[cta]['categoria']}» y la propuesta dice «{f['categoria']}»")
    if not f.get("regla_aplicada", "").strip(): errores.append(f"{n}: regla 10, falta la regla aplicada")
print(f"{len(filas)} filas revisadas, {len(errores)} problemas")
for x in errores: print(" -", x)
sys.exit(1 if errores else 0)
