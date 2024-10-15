"""
# Deploy

Este módulo es en donde se definen todas las tareas de deployments de los modelos.
Antes de adentrarse en la creación de estos modulos y como organizarlos es importante
tener algunas consideraciones relevantes.

1. Cada *padre* del deployment debe ser la versión en formato *camellcase* como se
se verá mas adelante.
2. Cada padre de la version, debe ser el tipo de modelo.
3. Deben existir archivos `__init__.py` solo hasta el nivel del tipo de dataset

La razón tras el putno *3*, se debe a que el codigo dentro de cada version de cada
*deploy* debe podemos funcionar de forma aislada y no deberia depender de **ningún
otro modeulo**; garantizando el correcto funcionamiento de cada uno.


## Modelos soportados

|modelo|
|:---:|
|modelV1|
"""
