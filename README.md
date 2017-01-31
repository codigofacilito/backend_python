Un servidor no es más que un equipo de computo el que esta ejecutando un programa que es capaz de comprender y responde apropiadamente a un cliente.
Esa es la definición de un servidor.

Por lo regular cuando escuchamos la palabra servidor aspciamos esta
a un equipo de computo con recursos muy grandes ya sea para su almacenamiento
o para el procesamiento de infromación, sin embargo un servidor puedeser cualquier
computador, una lap top con recursos limitados puede llegar a ser un servidor

Ahora que es un cliente, un cliente es una entidad la cual se encarga de realizar peticiones a un servidor para obtener un recurso, un recurso puede ser cualquier cosa, una imagen, un vídeo, un archivo html, un archivo xml etc.., utilozo la plabra entidad ya que existe una gran cantidad de ejemplos para cliente, tenemos nuestro navegador web, c, safari, firexfox tu ponle el nombre es un cliente, las app que tenemos en nuestros dispositivos moviles o en nuestras smar tv tambien son clientes, facebook, twitter, whatsapp, instagram por decir algunas.
Los programas de escritorio escritos en Java , C# que se comunican atraves de ineternet son clientes.

Ahora que menciono internet eso me lleva al segundo punto. La comunicación
Para que un servidor se pueda comunicar con un cliente y vicebesa nececitan un canla de comunicacón, para esto vamos a poyarnos de internet y usar el protocolo HTTP por sus siglas en ingles.

HTTP será el canal donde comunicaremos estas dos entidades, más adelante vamos a ter un vídeo completo para este protocolo.

Retomando los servidores existen n tipos de servidores, 
se de correos.
se de archivos.
se de base de datos.
se web. etc 
en este curso como ya mencione nos concentraremos en los servidores web.
La caracteristica de estos servidores es que 

este servidor provee de contenidos estáticos a los navegadores. Este le envía los archivos que carga por medio de la red al navegador del usuario. Los archivos pueden ser imágenes, escrituras, documentos HTML y cualquier otro material web.
Fuente: http://www.tiposde.org/informatica/131-tipos-de-servidores/#ixzz4XIwNIe37

Una vez aclarado lo que vamos a construir sigamos con las URLs.

____________________________

Actualmente nosotros tenemos un servidor el cual por ahora no realiza muchas acciones, por no decir que no hace absolutamente nada, para que este servidor se convierta en un servidor web lo primero que debemos de hacer es establcer ciertas URLs,

¿Qué son las urls?
Como mencionamos anteriormente nuestro cliente realizará una petición a un servidor para obtener sierto recursos, si estamos hablando de un servidor web encontes lo más probable es que espere recibir un archivo con extención html.

para que el cliente pueda encontrar un recurso dentro de internet necesitará una dirección. 
La urls no son más que direcciones dentro de internet.
Las urls tiene una estrucura definida que es la que ves en pantalla.

protocolo://dominio/ruta

creemos una url para nuestro servidor

http://localhost:3000/login

vamos nuestro servirdor , localhost, vemos el puerto, el protocolo y la dirección login.

vamos a explicar estar url con una pequeña analogia.

imaginemos que nuestro servidor es una pequeño ciudad, y que todas las paginas web en el servidor son casas, si queremos ver una casa vamos a tener que viajar a ese pueblo, para ello tendremos que usar un auto pista ya definida que sera la autopista http, lo siento no tengo mucha imaginación.

una vez llegemos ala ciudad debemos de buscar la colonia, la colonia vendra a ser el puerto.

ua vez estemos en la colonia simplemente buscamos la casa login y la visualizamos.

Espero me haya dado a entender que es una url.

bien ahora vamos a crear nuestra prpia url.




nuestro servidor será 

vamos a poner una pequeña analogia.
todas las páginas web que el servidor pueda proporcionar a los cliente serán 

Un servidor es capaz de almacenar multiples urls


-----------------
http://www.buyto.es/general-diseno-web/que-es-una-pagina-web-dinamica-para-que-sirve-una-pagina-web-dinamica



