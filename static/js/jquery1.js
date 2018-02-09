
//Agrega una clase a un elemento mediante otro selector.
//> selecciona todos los elementos q le siguen

$(() => {
  $('#selected-plays > li')
    .addClass('horizontal');
});

//$(() => {}), esta forma de pasar comandos es utilizada para que el comando se ejectue una vez que haya sido cargado en el dom.


//:not(.className), sele cciona todos los elementos que no tengan la clase especificada

$(() => {
	$('#selected-plays > li')
	.addClass('horizontal');
	$('#selected-plays li:not(.horizontal)')
	.addClass('sub-level');
});

// selectores de especificidad, >, not(.someClass), son aplicadas al objeto
//


//Buscame todos los enlaces que tengan href que comienzen con mailto: y se coloca con todo y comilla como cuando se escribe en el html. 
$(() => {
	$('a[href^="mailto:"]')
	.addClass('mailto');
}); 

$(() =>{
	$('#pelicula')
	.addClass('mailto')
})

//'a[href^="mailto:"]' = que comienzen con
//'a[href^="http"][href*="henry"]', qye comienzen con http y que contengan a la palabra henry en algun lugado 
//'a[href$="final"]'

//Para seleccionar a determinado elemento hijo con determinada classe, el siguiente ejemplo selecciona el segundo elemento ya que jquery es zero-based

$('div.horizontal:eq(1)')

//para seleccionar a los numeros pares o impares de un grupo de selectores.
$(() => {
	$('tr:even').addClass('alt');
});


//Selecciona determinados elementos con :nth-child(even)
$(() => {
	$('tr:nth-child(odd)').addClass('alt');
});

//Cuando se usa addClass('talCosa'), no se le agrega el punto.

$(() =>{

	$('.peluca:nth-child(odd)').addClass('torombolo')
})

//agrega el selector a todo aquello que contega determinada palabra, utilizar con cuidado. En este caso agrega el selector a todo aquello que contenga la plabra Henry. Case sensitive

$('td:contains(Henry)')


//Selectores para elementos de formulario.
:input
:button
:enabled
:disabled
:checked
:selected 

//DOM traversarl methods son utiles para seleccionar elementos parientes o ancestros. 
//En este ejemplo se esta agregando a todos los tr pares, comenzando desde cero, la classe .alt

$('tr')
.filter(':even')
.addClass('alt');


//En el siguiente ejemplo los enlaces deben contener un nombre dns y deben ser diferentes a la direccion de la pagina actual. 

$('a')
.filter((i, a) =>
	a.hostname && a.hostname !== location.hostname
	)
.addClass('external');

// para seleccionar los elementos que se encuentra siguientes a determinado elemento. se utiliza el metodo next(), y para seleccionar a todos los que se encuentran despues d determinado elemento se utiliza el metodo .nextAll
$(() => {
	$('td:contains(Henry)')
	.next()
	.addClass('highlight');
});

//para agregar el selector no solamente a las siguiente si no a la misma que se utiliza para empezar a medir se utiliza .addBack()

$(() => {
	$('td:contains(Henry)')
	.nextAll()
	.addBack()
	.addClass('highlight');
});


//Seleccionar todas las celdas en una fila donde al menos una de ellas tenga la palabra Henry.s
$(() => {
	$('td:contains(Henry)')
	.parent()
	.children()
	.addClass('highlight');
});

//Demostracion de una cadena de instrucciones.

$('td:contains(Henry)') // Find every cell containing "Henry"
	.parent() // Select its parent
	.find('td:eq(1)') // Find the 2nd descendant cell
	.addClass('highlight') // Add the "highlight" class
	.end() // Return to the parent of the cell containing "Henry"
	.find('td:eq(2)') // Find the 3rd descendant cell
	.addClass('highlight'); // Add the "highlight" class

//Atar todos esos comandos en una sola instruccion no es muy recomendable pero es un buen ejemplo de chaining el cual es un poco complicado de leer pero 

//Acceder al primer elemento referido por el Dom. 
$('#my-element').get(0).tagName;


$('li:eq(1)').addClass('special');

//Existen dos maneras de manejar los eventos utilizando el comando $(()=>{}), o el evento window.onload, siempre es mas recomendable el primero pero puede que en ocasiones cause problema el ancho y alto de las imagenes por lo cual se puede implementar el otro y ambos pueden coexistir perfectamente. Pueden ser agregados de las siguientes maneras. 

//Directamente en la etiqueta html
<body onload="doStuff();">

//mediante codigo js 
window.onload = doStuff;


$(()=>{
	$('#header-nav').addClass('efecto-1');
})


