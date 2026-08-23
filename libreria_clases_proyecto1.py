import math

def validar_positivo(
    valor,
    nombre,
    permitir_cero=False
):

    if permitir_cero:

        if valor < 0:
            raise ValueError(
                f"{nombre} no puede ser negativo."
            )

    else:

        if valor <= 0:
            raise ValueError(
                f"{nombre} debe ser mayor que cero."
            )


class InventarioProducto:

    def __init__(self, nombre, costo_unitario, precio_unitario, stock_actual, stock_minimo):
        self.nombre = nombre
        self.costo_unitario = costo_unitario
        self.precio_unitario = precio_unitario
        self.stock_actual = stock_actual
        self.stock_minimo = stock_minimo

        validar_positivo(self.costo_unitario, "costo_unitario")
        validar_positivo(self.precio_unitario, "precio_unitario")
        validar_positivo(self.stock_actual, "stock_actual", permitir_cero=True)
        validar_positivo(self.stock_minimo, "stock_minimo", permitir_cero=True)

    def valor_inventario(self):
        return self.costo_unitario * self.stock_actual

    def margen_unitario(self):
        return self.precio_unitario - self.costo_unitario

    def margen_porcentaje(self):
        return (self.margen_unitario() / self.precio_unitario) * 100

    def necesita_reposicion(self):
        return self.stock_actual <= self.stock_minimo

    def resumen(self):
        return {
            "producto": self.nombre,
            "stock_actual": self.stock_actual,
            "valor_inventario": round(self.valor_inventario(), 2),
            "margen_unitario": round(self.margen_unitario(), 2),
            "margen_pct": round(self.margen_porcentaje(), 2),
            "necesita_reposicion": self.necesita_reposicion()
        }


