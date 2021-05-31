
   /* search engine
    * -------------------------------------------------- */

  function myFunction() {
    var val = document.getElementById("mySearch").value.toLowerCase();
    if( val == null || val.length == 0 || /^\s+$/.test(val) ) {
        alert('Empty field! Please type a word.');
    }else{
        document.location.href = "#" + val;
    }

  }