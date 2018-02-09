$(document).ready(function(){
	/*NAVBAR SLIDER*/
	$('#menu-toggle').click(function(){
		$('.sidebar').toggleClass('ocultar');
		
	});

});

/*FORMULARIOS DEL DASHBOARD*/

$(document).ready(function(){

	/*REGISTRO DE EMPRESA*/
	$('#btn-pub-emp').click(function(){
		$('#form2').hide();
		$('#form1').show();
		$('.pub-emp').addClass('active');
		$('.pub-anu').removeClass('active');

	});
	/*REGISTRO DE ANUNCIO*/
	$('#btn-pub-anu').click(function(){
		$('#form1').hide();
		$('#form2').show();
		$('.pub-anu').addClass('active');
		$('.pub-emp').removeClass('active');

	});
});

$(document).ready(function(){

	// /*REGISTRO DE EMPRESA*/
	$('#modal-close').click(function(){
		$('.modal-backdrop').removeClass('show');
		$('.modal-backdrop').addClass('hide');
		$('.login_modal_enter').modal('toggle');
		// $('body').removeClass('modal-open');
	});

	$('#modal-reg-close').click(function(){
		$('.modal-backdrop').removeClass('show');
		$('.modal-backdrop').addClass('hide');
		$('.login_modal_register').modal('toggle');
		// $('body').removeClass('modal-open');
	});
	
});



// $(document).ready(function(){

// 	$('a.say').on('click', function(e){
// 		e.preventDefault();
// 		var text = $('input[name="translate_es"]').change(function(){
// 			$('input[name="translate_en"]').val($(this).val());
// 		}); 

// 	})
	
// });

