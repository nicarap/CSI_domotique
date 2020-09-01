$(document).ready(function() {

	
	$.ajaxSetup({
    // fonction appelée avant d'envoyer une requête AJAX
    beforeSend: function(xhr, settings) {
         // on ajoute le header que si la requête est pour le site en cours
         // (URL relative) et est de type POST
         if (!/^https?:.*/.test(settings.url)  && settings.type == "POST") {
             // attachement du token dans le header
             xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
         }
     }
	});
	function getCookie(name) {
	    if (document.cookie && document.cookie != '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                return decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	}


	$('input[type="checkbox"]').on('change', function(e){
		if($(this).prop('checked') == true)
		{
			updateLum(this,$(this).attr('whatever'), 1, 1);
		}else{
			updateLum(this,$(this).attr('whatever'), 1, 0);
		}
	})
/*

    $(".p_lumimere_off").click( function(event) {
    alert("Allumer la lumière -> AJAX");
    });
    $(".lumimere_on").click( function(event) {
    alert("Eteindre la lumière -> AJAX");

	


    });

	$.ajax({
	   type: "POST",
	   url: "/add_bouteille",
	   dataType: "json",
	   traditional: true,
	   data: {'list_bouteille': JSON.stringify(tab_bouteille)},
	   success: function(data) {
	           console.log(data["HTTPRESPONSE"]);
	   }
	});
});
 */


});
