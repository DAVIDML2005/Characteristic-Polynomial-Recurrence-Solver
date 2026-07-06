# Solución de Relaciones de Recurrencia mediante Polinomios Característicos

## Descripción

Este repositorio presenta una implementación en Python para resolver automáticamente relaciones de recurrencia lineales homogéneas con coeficientes constantes utilizando el método del polinomio característico. El proyecto transforma una relación de recurrencia en su fórmula cerrada (no recurrente) mediante técnicas de álgebra lineal y teoría de ecuaciones características. La implementación automatiza todo el proceso, desde la construcción del polinomio característico hasta la obtención de la expresión final que satisface las condiciones iniciales.

## Objetivos

* Automatizar la resolución de relaciones de recurrencia lineales homogéneas.
* Implementar el método del polinomio característico en Python.
* Obtener la fórmula cerrada asociada a una recurrencia.
* Resolver automáticamente los coeficientes de la solución mediante sistemas de ecuaciones lineales.
* Facilitar el aprendizaje de uno de los métodos clásicos de Matemáticas Discretas.

## Fundamento Matemático

El proyecto resuelve recurrencias de la forma:

$$
f_n = a_1f_{n-1} + a_2f_{n-2} + \cdots + a_mf_{n-m}
$$

mediante la construcción del polinomio característico:

$$
t^m - a_1t^{m-1} - a_2t^{m-2} - \cdots - a_m = 0
$$

Dependiendo de las raíces obtenidas:

* **Raíces simples**

  Si una raíz \(r\) tiene multiplicidad 1, la solución contiene un término de la forma

$$
c\,r^n
$$


* **Raíces múltiples**

  Si una raíz \(r\) tiene multiplicidad \(k\), la solución contiene un término de la forma

$$
(c_0 + c_1n + \cdots + c_{k-1}n^{k-1})\,r^n
$$

Finalmente, los coeficientes desconocidos se determinan resolviendo un sistema lineal construido a partir de las condiciones iniciales.

## Funcionamiento del Algoritmo

La implementación automatiza las siguientes etapas:

1. Construcción del polinomio característico.
2. Cálculo de las raíces (enteras en esta implementación).
3. Detección de multiplicidades.
4. Construcción de la solución general.
5. Generación del sistema de ecuaciones utilizando las condiciones iniciales.
6. Resolución del sistema mediante álgebra lineal.
7. Obtención de la fórmula cerrada final.

## Aprendizajes

Este proyecto demuestra cómo diferentes áreas de las matemáticas se integran para resolver un mismo problema:

* Álgebra.
* Álgebra lineal.
* Polinomios.
* Ecuaciones características.
* Sistemas lineales.
* Relaciones de recurrencia.

La implementación busca no solo automatizar cálculos, sino también servir como una herramienta didáctica para comprender el funcionamiento del método del polinomio característico.
