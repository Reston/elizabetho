if (/MSIE (\d+\.\d+);/.test(navigator.userAgent)){ //test for MSIE x.x;
 var ieversion=new Number(RegExp.$1) // capture x.x portion and store as a number
 if (ieversion <= 7) {
  alert("¡Hola! Parece que usted está utilizando Internet Explorer 7 o inferior, esto es muy malo:  "+ document.domain +" ya no lo soporta Le estamos enviando a una página \n para ayudará a instalar un navegador mejor.. \n \nPor favor vuelva a "+ document.domain +" en un navegador mejor!");
  
  window.location="http://abetterbrowser.org";
  
  }
}