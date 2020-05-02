# Generación de clasificaciones SKOS
En este repositorio se encuentran todos los componentes necesarios para generar ficheros de clasificaciones que siguen el modelo [SKOS](https://www.w3.org/TR/swbp-skos-core-spec/) a partir de mappings RML . SKOS Core es un modelo y un vocabulario RDF para expresar la estructura básica y el contenido de esquemas conceptuales como tesauros, esquemas de clasificación, listas de encabezados de temas, taxonomías, 'folksonomías', otros tipos de vocabulario controlado, y también esquemas conceptuales integrados en glosarios y terminologías. [RML](https://rml.io/) es un lenguaje de mapeo definido para expresar reglas de correspondencia de bases de datos o ficheros con formatos CSV, JSON o XML hacia  modelos de datos representados en RDF. Para la generación de clasificaciones SKOS en RDF se generarán los ficheros SKOS a partir de ficheros CSV.

## ¿Cuál es la entrada del proceso de generación?
La entrada a este proceso de generación son dos ficheros:
* Fichero para los datos de la clasificación. Este fichero contiene columnas para los niveles de la taxonomía (tantas columnas como niveles). Luego se tienen columnas para los labels en inglés y español y para las definiciones en inglés y español. 
Un fichero ejemplo es ejemplo-clasificacion.csv que corresponde a la clasificación económica del gasto de presupuesto de los ayuntamientos. En este fichero se pueden ver cuatro niveles, el label en español y la definición en español. Para la primera fila se ha ejemplificado un label y una definición en inglés. El label en inglés y las definiciones en inglés y español son opcionales. En este ejemplo los niveles son números, existen otras clasificaciones en donde son strings de caracteres, por ejemplo en el caso de tipo de entidad de un convenio se tiene un primer nivel llamado "administracion-local" y como subnivel "diputacion-provincial". 

* Fichero para la descripción de la clasificación. Este fichero contiene los metadatos de la taxonomía, tales como el creador, la fecha de creación, el título de la taxonomía y su label (nombre). En el fichero ejemplo-descripcion se pueden ver los metadatos de la clasificacion económica de gasto.

## ¿Cuál es la salida del proceso de generación?
El SKOS generado contiene skos:topConcept para todos los términos del nivel 1. Para cada término se genera skos:prefLabel para español e inglés y skos:definition para español e inglés. Luego, de un nivel a uno más específico se generan tripletas con skos:narrower y de uno específico a uno más general se genera un skos:broader.

## ¿Cómo se ejecuta el proceso?

## ¿En qué consiste el proceso de generación?
* A partir del fichero csv de datos de la clasificación y genera dos ficheros csv: (1) fichero para los labels y definiciones y (2) fichero para la jerarquía entee términos.

* A partir de los dos ficheros csv del paso anterior y del fichero de descripción se genera un fichero de mappings [YARRRML](https://rml.io/yarrrml/) (mappings representados en YAML). Para este paso también se tiene como entrada un template de fichero yarrrml ya que un RDF en SKOS para los casos que estamos considerando sigue siempre la misma estructura. 

* Se ejecuta la traducción del fichero [YARRRML a un fichero de mappins RML.

* Se genera el fichero RDF al ejecutar la herramienta RDFizer que a partir de los ficheros csv y el fichero de mappings RML, materializa a un fichero RDF serializado en Turtle.



