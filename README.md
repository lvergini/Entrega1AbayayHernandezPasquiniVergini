<h1>Primera entrega del Trabajo Final - CoderHouse</h1>

<p>La aplicación está basada en el modelo de una librería que maneja tres modelos que, además de sus atributos, cuentan con un método __str__ y, como metadato, un orden predeterminado en el que aparecerán: </p>

  <ul>
        <li> <strong>Libros</strong> (se ordenan por título) </li>
        <li> <strong>Editoriales</strong> (se ordenan por nombre)</li>
        <li> <strong>Autores</strong> (se ordenan por apellido)</li>
  </ul<h1>Primera entrega del Trabajo Final - CoderHouse</h1>

<p>La aplicación está basada en una librería que maneja tres modelos que, además de sus atributos, cuentan con un método __str__ y, como metadato, un orden predeterminado en el que aparecerán: </p>

  <ul>
        <li> <strong>Libros</strong> (se ordenan por título) </li>
        <li> <strong>Editoriales</strong> (se ordenan por nombre)</li>
        <li> <strong>Autores</strong> (se ordenan por apellido)</li>
  </ul>

<p>Donde un libro pertenece a un autor y a una editorial. La aplicación permite dar de alta autores, editoriales y libros. Asimismo, permite realizar búsquedas por autor (a partir de su apellido), editorial (a partir de su nombre) o libro (a partir de su título y/o autor). </p>

<p>Las siguientes URLs están a disposición:</p>

  <ul>
        <li> ~/AppLibros/   --> Inicio </li>
        <li> ~/AppLibros/autorCrear/   --> Crear un nuevo Autor</li>
        <li> ~/AppLibros/libroCrear/  --> Crear un nuevo Libro</li>
        <li> ~/AppLibros/editorialCrear/ --> Crear una nueva Editorial </li>
        <li> ~/AppLibros/busquedaAutor/ --> Buscar autor por su apellido </li>
        <li> ~/AppLibros/busquedaLibro/ --> Buscar libro por su título y/o su autor</li>
        <li> ~/AppLibros/busquedaEditorial/ --> Buscar editorial por su nombre</li>
  </ul>


<h3>Herencia de templates</h3>

<p>El template del cual se hereda el resto (padre.html) está compuesto por:</p>

  <ul>
        <li> <strong>una barra de navegación</strong>, que permite acceder al inicio y a tres menús desplegables, cada uno de los cuales contiene enlaces para acceder a los formularios para crear y para buscar objetos dentro de cada modelo (libros, autores, editoriales); </li>
        <li> <strong>un título (masthead)</strong>, compuesto por una imagen común para todas las páginas y un texto que cambia para indicar la funcionalidad de cada una;</li>
        <li> <strong>un pie o footer</strong> cuyos enlaces todavía no están en funcionamiento.</li>
  </ul>


<h3>Formulario para crear objetos de cada modelo:</h3>
<p>A través de GET (por ejemplo, cuando se ingresa por medio del menú desplegable), la página muestra un formulario vacío para completar. </p>
<p>A través del método POST, muestra y envía los atributos para instanciar un objeto de la clase correspondiente. Todos los campos son obligatorios, excepto:
  <ul>
        <li>el mail de un autor (puede dejarse vacío en caso de que el autor esté muerto o de que no se posea esa información); </li>
        <li>la descripción de un libro.</li>
  </ul>
<p> En el caso del formulario para crear libros, los campos “Autor” y “Editorial” (correspondientes a atributos anidados) se seleccionan por medio de una lista desplegable, que muestra, en orden alfabético, los autores o editoriales cargados en la base de datos. En este sentido, es importante tener en cuenta que, para crear un libro, deben estar ya creados su autor y editorial. </p> 

<p>Si el formulario es válido, debe redirigir a la página de inicio, en la que se mostrará un mensaje que indica que se creó el objeto, especificando: </p> 
  <ul>
        <li>para los autores, su nombre y apellido; </li>
        <li>para las editoriales, su nombre;</li>
        <li>para los libros, su título.</li>
  </ul>

<p>Si hay un error al ingresar alguno de los datos requeridos, el formulario también redirige a la página inicio, pero en este caso el mensaje avisa al usuario que hubo un error. </p>

<h3>Formulario para buscar libros:</h3>

<p>URL: ~/AppLibros/busquedaLibro/</p>
<p>URL de resultados: ~/AppLibros/resultadoLibros/</p>
<p>Se brindan dos opciones de búsqueda (por medio de su título o del apellido de su autor). En ambos casos, la búsqueda se realiza a través de "icontains"; es decir, deberá ser insensible a las minúsculas y mayúsculas. </p>
<p>Puede completarse un solo campo o los dos. </p>
  <ul>
        <li>Caso en que se ingresa un solo campo: </li>
  </ul>

<p>Se devolverá como resultado  los libros que contengan en su título o en el apellido del autor la cadena ingresada. Por ejemplo, al poner  “noche” en título, se encontrarán los libros Cae la noche tropical, de Manuel Puig, Las maquinarias de la noche, de Abelardo Castillo, y Nuestra parte de noche, de Mariana Enriquez. Al ingresar “Enriquez” en apellido de autor, el resultado serán los tres libros cargados de esta autora: Las cosas que perdimos en el fuego, Los peligros de fumar en la cama y Nuestra parte de noche. </p>
<p>En caso de que se busque por título, si ningún libro coincide, se mostrará el mensaje “No hay libros que contengan en su título "{titulo}”. Si se busca por apellido de un autor y este no está cargado en la BD, el mensaje será: 'No hay ningún autor de apellido "{autor}"'. Si está cargado, pero no así sus libros, aparecerá: 'No hay libros del autor "{autor}". Esto último puede probarse ingresando, por ejemplo, “Lamberti”.</p>

  <ul>
        <li>Caso en que se ingresan los dos campos: </li>
  </ul>

<p>Si se completan los dos campos, retornará los libros que cumplan con ambas condiciones. Siguiendo con el ejemplo anterior, si se ingresa “noche” en título y “Castillo” en apellido del autor, solo aparecerá Las maquinarias de la noche. En caso de que no exista en la base de datos ningún autor cuyo apellido coincida con parte de la cadena ingresada, se mostrará en la página de resultados el mensaje: 'No hay ningún autor de apellido "{autor}"’. En cambio, si el autor existe, pero no posee libros cargados, el mensaje será: 'No hay libros del autor "{autor}" que contengan en su título "{titulo}"'.</p>
<p>Cuando se presiona enviar sin haber ingresado ningún dato, el formulario redirige a la página de búsqueda (AppLibros/busquedaLibro) con el mensaje: ¡No enviaste datos!".</p>

<h3>Formulario para buscar autores:</h3>

<p>URL: ~/AppLibros/busquedaAutor/</p>
<p>URL de resultados: ~/AppLibros/resultadoAutores/</p>

<p>La búsqueda se realiza por apellido, también a través de "icontains". Devolverá como resultado todos los autores cuyos apellidos contengan parte de la cadena ingresada, con sus respectivos atributos (nombre, apellido y email). En caso de que no existan, aparecerá el mensaje: “"No hay autores con el apellido {apellido}". </p>
<p>Asimismo, si la base de datos tiene cargados libros del autor, deberán aparecer luego de la información de este, ordenados alfabéticamente por su título (tal como se indica en los metadatos de este modelo). Este sería, por ejemplo, el caso si se busca “Schweblin”: se mostrarán sus dos libros cargados, Kentukis y Pájaros en la boca.  </p>
<p>En caso de que el autor ya esté cargado, pero no así alguno de sus libros, la página debe mostrar el mensaje: "Todavía no hay ningún libro cargado del autor", indicando su nombre y apellido. Esto sucedería, por ejemplo, con Lamberti.</p>
<p>Por último, si se presiona el botón "Buscar" con el formulario vacío, la página redirige a la búsqueda (AppLibros/busquedaAutor.html), informando al usuario que no ha ingresado ningún dato.</p>

<h3>Formulario para buscar editoriales:</h3>

<p>URL: ~/AppLibros/busquedaEditorial/</p>
<p>URL de resultados: ~/AppLibros/resultadoEditoriales/</p>
<p>La búsqueda se realiza por nombre, también a través de "icontains". Devolverá como resultado todas las editoriales cuyos nombres contengan parte de la cadena ingresada, con sus respectivos atributos (nombre, dirección, responsable y email). En caso de que no existan, aparecerá el mensaje: “No hay editoriales con el nombre "{nombre}"'. </p>
<p>En caso de que la base de datos tenga cargados libros publicados por la editorial a buscar, deberán aparecer luego de la información de esta, ordenados alfabéticamente por su título.</p>
<p>Si no hay ningún libro cargado de la editorial, luego de los datos de esta, la página debe mostrar el mensaje: “Todavía no hay ningún libro cargado de la editorial {{ editorial.nombre }}”. Esto sucedería, por ejemplo, al buscar la editorial Planeta.  </p>
<p>Como en los casos anteriores, si se presiona el botón "Buscar" con el formulario vacío, la página redirige a la búsqueda (~/AppLibros/busquedaEditorial/), informando al usuario que no ha ingresado ningún dato.</p>


<p>Donde un libro pertenece a un autor y a una editorial. La aplicación permite dar de alta autores, editoriales y libros. Asimismo, permite realizar búsquedas por autor (a partir de su apellido), editorial (a partir de su nombre) o libro (a partir de su título y/o autor). </p>

<p>Las siguientes URLs están a disposición:</p>

  <ul>
        <li> ~/AppLibros/   --> Inicio </li>
        <li> ~/AppLibros/autorCrear/   --> Crear un nuevo Autor</li>
        <li> ~/AppLibros/libroCrear/  --> Crear un nuevo Libro</li>
        <li> ~/AppLibros/editorialCrear/ --> Crear una nueva Editorial </li>
        <li> ~/AppLibros/busquedaAutor/ --> Buscar autor por su apellido </li>
        <li> ~/AppLibros/busquedaLibro/ --> Buscar libro por su título y/o su autor</li>
        <li> ~/AppLibros/busquedaEditorial/ --> Buscar editorial por su nombre</li>
  </ul>


<h3>Herencia de templates</h3>

<p>El template del cual se hereda el resto (padre.html) está compuesto por:</p>

  <ul>
        <li> <strong>una barra de navegación</strong>, que permite acceder al inicio y a tres menús desplegables, cada uno de los cuales contiene enlaces para acceder a los formularios para crear y para buscar objetos dentro de cada modelo (libros, autores, editoriales); </li>
        <li> <strong>un título (masthead)</strong>, compuesto por una imagen común para todas las páginas y un texto que cambia para indicar la funcionalidad de cada una;</li>
        <li> <strong>un pie o footer</strong> cuyos enlaces todavía no están en funcionamiento.</li>
  </ul>


<h3>Formulario para crear objetos de cada modelo:</h3>
<p>A través de GET (por ejemplo, cuando se ingresa por medio del menú desplegable), la página muestra un formulario vacío para completar. </p>
<p>A través del método POST, muestra y envía los atributos para instanciar un objeto de la clase correspondiente. Todos los campos son obligatorios, excepto:
  <ul>
        <li>el mail de un autor (puede dejarse vacío en caso de que el autor esté muerto o de que no se posea esa información); </li>
        <li>la descripción de un libro.</li>
  </ul>
<p> En el caso del formulario para crear libros, los campos “Autor” y “Editorial” (correspondientes a atributos anidados) se seleccionan por medio de una lista desplegable, que muestra, en orden alfabético, los autores o editoriales cargados en la base de datos. </p> 

<p>Si el formulario es válido, debe redirigir a la página de inicio, en la que se mostrará un mensaje que indica que se creó el objeto, especificando: </p> 
  <ul>
        <li>para los autores, su nombre y apellido; </li>
        <li>para las editoriales, su nombre;</li>
        <li>para los libros, su título.</li>
  </ul>

<p>Si hay un error al ingresar alguno de los datos requeridos, el formulario también redirige a la página inicio, pero en este caso el mensaje avisa al usuario que hubo un error. </p>

<h3>Formulario para buscar libros:</h3>

<p>URL: ~/AppLibros/busquedaLibro/</p>
<p>URL de resultados: ~/AppLibros/resultadoLibros/</p>
<p>Se brindan dos opciones de búsqueda (por medio de su título o del apellido de su autor). En ambos casos, la búsqueda se realiza a través de "icontains"; es decir, deberá ser insensible a las minúsculas y mayúsculas. </p>
<p>Puede completarse un solo campo o los dos. </p>
<p>Si se ingresa uno solo, se devolverá como resultado  los libros que contengan en su título o en el apellido del autor la cadena ingresada. Si ningún libro coincide, se mostrará el mensaje “No hay libros que contengan en su título "{titulo}” o 'No hay libros del autor "{autor}"'.</p>
<p>Si se completan los dos campos, retornará los libros que cumplan con ambas condiciones. En caso de que no exista en la base de datos ningún autor cuyo apellido coincida con parte de la cadena ingresada, se mostrará en la página de resultados el mensaje: 'No hay ningún autor de apellido "{autor}"’. En cambio, si el autor existe, pero no posee libros cargados, el mensaje será: 'No hay libros del autor "{autor}" que contengan en su título "{titulo}"'.</p>
<p>Cuando se presiona enviar sin haber ingresado ningún dato, el formulario redirige a la página de búsqueda (AppLibros/busquedaLibro) con el mensaje: ¡No enviaste datos!".</p>

<h3>Formulario para buscar autores:</h3>

<p>URL: ~/AppLibros/busquedaAutor/</p>
<p>URL de resultados: ~/AppLibros/resultadoAutores/</p>

<p>La búsqueda se realiza por apellido, también a través de "icontains". Devolverá como resultado todos los autores cuyos apellidos contengan parte de la cadena ingresada, con sus respectivos atributos (nombre, apellido y email). En caso de que no existan, aparecerá el mensaje: “"No hay autores con el apellido {apellido}". </p>
<p>Asimismo, si la base de datos tiene cargados libros del autor, deberán aparecer luego de la información de este, ordenados alfabéticamente por su título (tal como se indica en los metadatos de este modelo).</p>
<p>En caso de que el autor ya esté cargado, pero no así alguno de sus libros, la página debe mostrar el mensaje: "Todavía no hay ningún libro cargado del autor", indicando su nombre y apellido.</p>
<p>Por último, si se presiona el botón "Buscar" con el formulario vacío, la página redirige a la búsqueda (AppLibros/busquedaAutor.html), informando al usuario que no ha ingresado ningún dato.</p>

<h3>Formulario para buscar editoriales:</h3>

<p>URL: ~/AppLibros/busquedaEditorial/</p>
<p>URL de resultados: ~/AppLibros/resultadoEditoriales/</p>
<p>La búsqueda se realiza por nombre, también a través de "icontains". Devolverá como resultado todas las editoriales cuyos nombres contengan parte de la cadena ingresada, con sus respectivos atributos (nombre, dirección, responsable y email). En caso de que no existan, aparecerá el mensaje: “No hay editoriales con el nombre "{nombre}"'. </p>
<p>En caso de que la base de datos tenga cargados libros publicados por la editorial a buscar, deberán aparecer luego de la información de esta, ordenados alfabéticamente por su título.</p>
<p>Si no hay ningún libro cargado de la editorial, luego de los datos de esta, la página debe mostrar el mensaje: “Todavía no hay ningún libro cargado de la editorial {{ editorial.nombre }}”. </p>
<p>Como en los casos anteriores, si se presiona el botón "Buscar" con el formulario vacío, la página redirige a la búsqueda (~/AppLibros/busquedaEditorial/), informando al usuario que no ha ingresado ningún dato.</p>
