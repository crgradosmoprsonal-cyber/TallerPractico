# Taller Práctico - Paquete Python

Este paquete contiene dos funcionalidades principales:

1. **Conversor de monedas**  
   Convierte un valor en dólares a otras monedas:  
   - Euros (EUR)  
   - Libras Esterlinas (LB)  
   - Won Surcoreano (KRW)  
   - Bitcoin (BTC)  

2. **Contador de vocales**  
   Cuenta cuántas veces aparece cada vocal en una frase.

---

## Uso

Ejemplo de uso desde `main.py`:

```python
from Paquete import convertir_dolares, contar_vocales

# Conversor
print(convertir_dolares(100, "EUR"))

# Contador de vocales
print(contar_vocales("Hola mundo, esto es un ejemplo"))
