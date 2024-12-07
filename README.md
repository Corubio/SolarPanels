# SolarPanels ☀️😎

Este programa calcula la cantidad máxima de paneles rectangulares que se pueden colocar en un área determinada. El área puede ser una figura rectangular (R) o dos rectangulos iguales superpuestos (O) y los paneles pueden colocarse tanto horizontal como verticalmente. Se genera un archivo de salida con la cantidad máxima de paneles colocados.

## Input 👈

El archivo de entrada debe contener los siguientes datos:

Figura del área: Una sola línea que indica el tipo de figura.

* R: indica un área rectangular
* O: indica un área donde dos rectángulos iguales se encuentran superpuestos en un área igual a la de un panel

Dimensiones del panel: Dos números enteros separados por un espacio que representan el ancho y la altura del panel.
Dimensiones del área: Dos números enteros separados por un espacio que representan el ancho y la altura del área.
Ejemplos de entrada (in.txt):

```txt
R
2 3
2 4
```

```txt
O
1 2
2 4
```

## Output 👉

El archivo de salida contendrá un solo número que indica la cantidad máxima de paneles que se pueden colocar en el área.

## Como correr el programa? 💻

Dependiendo de tu instalacion una de las siguientes deberia bastar

```txt
python main.py
```

```txt
python3 main.py
```

## Consideraciones ⚙️

* Actualmente, solo se admite el área rectangular ("R") y áreas superpuestas iguales ("O").
* Las dimensiones de los paneles y el área sean números enteros positivos.
* La superposición de áreas iguales se hace en un area igual a la de un panel, esto con el objetivo de simplificar el input
* Se asume que lo anterior siempre es posible por lo que un area no puede ser mas pequeña que el panel en el caso de O.
