<h1>Proyecto Final - CoderHouse</h1>

La aplicacion final está basada en el modelo de una librería que maneja:
- Libros
- Editoriales
- Autores

Donde un libro pertenece a un autor y a una editorial. La aplicación permite dar de alta autores, editoriales y libros. Asimismo, permite realizar busquedas por autor (a partir de su apellido), editorial (a partir de su nombre) o libro (a partir de su título y/o autor). 

Las siguientes URLs estan a disposición para el administrador:

- ~/AppLibros/   --> Inicio
- ~/AppLibros/autorCrear/   --> Crear un nuevo Autor
- ~/AppLibros/libroCrear/  --> Crear un nuevo Libro
- ~/AppLibros/editorialCrear/ --> Crear una nueva Editorial
- ~/AppLibros/busquedaAutor/ --> Buscar autor por su apellido 
- ~/AppLibros/busquedaLibro/ --> Buscar libro por su título y/o su autor
- ~/AppLibros/busquedaEditorial/ --> Buscar editorial por su nombre

<h3>Herencia de templates</h3>

<p>El template del cual se hereda el resto (padre.html) está compuesto por:</p>
- una barra de navegación, que permite acceder al inicio y a tres menús desplegables, cada uno de los cuales contiene enlaces para acceder a los formularios para crear y para buscar objetos dentro de cada modelo (libros, autores, editoriales); 
- un título (masthead), compuesto por una imagen común para todas las páginas y un texto que cambia para indicar la funcionalidad de cada una;
- un pie o footer, cuyos enlaces todavía no están en funcionamiento. 

<h3>Formulario para crear autores:</h3>
<p>A través de GET (por ejemplo, cuando se ingresa por medio del menú desplegable), la página muestra un formulario vacío para completar. </p>
<p>A través del método POST, muestra y envía los atributos para instanciar un objeto de esta clase. El nombre y el apellido son obligtorios, no así el mail, que puede dejarse vacío en caso de que el autor esté muerto o de que no se posea esa información. </p>
<p>Si el formulario es válido, debe redirigir a la página de inicio, en la que se mostrará un mensaje que indica que se creó el autor, incluyendo su nombre y apellido. </p> 
<p>Si hay un error al ingresar alguno de los datos requeridos, el formulario también redirige a la página inicio, pero en este caso el mensaje avisa al usuario que hubo un error. </p>

<h3>Formulario para buscar autores:</h3>
<p>La búsqueda se realiza por apellido, a través de "icontains"; es decir, deberá ser insensible a las minúsculas y mayúsculas, y devolverá como resultado (en AppLibros/resultadoAutores.html) todos los autores cuyos apellidos contengan parte de la cadena ingresada. </p>
<p>Asimismo, si la base de datos tiene cargados libros del autor, estos deberán aparecer luego de la información de este, ordenados alfabéticamente por su título (tal como se indica en la definición de este modelo). </p>
<p>En caso de que el autor ya esté cargado, pero no así alguno de sus libros, la página debe mostrar el mensaje: "Todavía no hay ningún libro cargado del autor", indicando su nombre y apellido. </p>
<p>Por último, si se presiona el botón "Buscar" con el formulario vacío, la página redirige a la búsqueda (AppLibros/busquedaAutor.html), informando al usuario que no ha ingresado ningún dato. </p>

<h3>Formulario para crear editoriales:</h3>
<p>A través de GET (por ejemplo, cuando se ingresa por medio del menú desplegable), la página muestra un formulario vacío para completar. </p>
<p>A través del método POST, muestra y envía los atributos para instanciar un objeto de esta clase. En este caso, todos los campos son obligtorios. </p>
<p>Si el formulario es válido, debe redirigir a la página de inicio, en la que se mostrará un mensaje que indica que se creó la editorial, incluyendo su nombre. </p> 
<p>Si hay un error al ingresar alguno de los datos requeridos, el formulario también redirige a la página inicio, pero en este caso el mensaje avisa al usuario que hubo un error. </p>
