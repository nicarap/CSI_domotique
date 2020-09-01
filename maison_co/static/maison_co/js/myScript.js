$(document).ready(function() {
  $('.div_contain').on('mouseover',function(e){
    // $(this).children('.card-head').attr('style','display:block')
     // $(this).attr('style','border:10px solid #34495e')
  })
  $('.div_contain').on('mouseout',function(e){
    // $(this).attr('style','border:0')
    // $(this).children('.card-head').attr('style','display:none')
  })




})
//FUNCTION UPDATELUM Au clique sur la div
/* 
SI le bouton selectionner est active -> selectionne les divs en changeant couleur de fond
SINON ->  
  SI id_fk <> 1 Change l'état de toutes les lumières de la pièce id_fk
  SINON -> Change l'état de la lumière passé en paramètre.
*/
function updateLum(elmt, id_fk, id, etat)
{
  if ($(".lum_delete").hasClass("active")){
    if($(elmt).css('background-color') == "rgb(128, 128, 128)") {
      $(elmt).attr('style',  'background-color:none');
    } else {
      $(elmt).attr('style',  'background-color:grey');
    }
  }
  else
  {
  $.ajax({
          url: `/MyLum/update/${id_fk}/${id}/${etat}`,
          success: function (data) {
            if(etat == -1){
              if (data.Etat) {
              $(elmt).children('img').attr('src', "static/maison_co/image/amp_on.png") ;
              }
              else {$(elmt).children('img').attr('src', "static/maison_co/image/amp_off.png") ;}
            }
            else if(etat ==0){$('.' + id_fk).children('img').attr('src', "static/maison_co/image/amp_off.png");}   
            else{$('.' + id_fk).children('img').attr('src', "static/maison_co/image/amp_on.png");}        
          }
        });
  }
}

//FUNCTION deleteLum
/* 
Supprime la lumière selectionné.
id de la div = l'id de la lumiere
*/
function  deleteLum(el){
    lumId  = $(el).attr('id');
    $.ajax({
        url:  `/MyLum/delete/${lumId}`,
        type:  'post',
        dataType:  'json',
        success:  function (data) {
            $(el).parents()[1].remove();
        }
    });
    $(el).remove();
}

//FUNCTION DeleteMass
/* 
Pour chaque div selectionné (avec un fond d'une certaine couleur)
On appel la fonction delete 
*/
function DeleteMass()
{
  $(".div_lum").each(function(){
    if($(this).css('background-color') == "rgb(128, 128, 128)") {
      deleteLum(this);
    }
 })
 select($(".lum_delete"));

}

//FUNCTION Select
/* 
Change l'état du bouton Select, modif et suoppr à chaque clique
Permet de "selectionner" les divs
*/
function select(elmt)
{
    $(elmt).toggleClass("active");
    if (!$(elmt).hasClass("active"))  {
      $(".div_lum").each(function(){
        $(".div_lum").attr('style', 'background-color:none')
        });
      $(".btn_delete").addClass("invisible");
      $(".btn_modif").removeClass("disabled");
      $(".btn_add").removeClass("disabled");
    }
    else {
      $(".btn_delete").removeClass("invisible");
      $(".btn_modif").addClass("disabled");
      $(".btn_add").addClass("disabled");
    }
    
}


