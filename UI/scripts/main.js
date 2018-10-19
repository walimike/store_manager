
function showDetail(){
  var cart = ""
  var products = document.getElementById("products");
  var details = document.getElementById("details");
  details.innerHTML = "";
  details.innerHTML = details.innerHTML + products;
}


function addToCart() {
    // clear selection table first
    var selection = document.getElementsByTagName("table")[1].getElementsByTagName("tbody")[0];
    selection.innerHTML = "";

    // loop through items
    var items = document.getElementsByTagName("tr");
    for (var i = 0; i < items.length; i++) {
      var input = items[i].getElementsByTagName("input");
      if (!input.length) continue;
      if (!input[0].checked) continue;
      var item =  items[i].getElementsByTagName("td")[0].innerHTML;
      // append element to selection
      selection.innerHTML = selection.innerHTML + "<p>" + item;
    }
  }


function showDetails() {
  var selection = document.getElementsByTagName("table")[1].getElementsByTagName("tbody")[0];
    selection.innerHTML = "";

    // loop through items
    var items = document.getElementsByTagName("tr");
    for (var i = 0; i < items.length; i++) {
      var input = items[i].getElementsByTagName("input");
      if (!input.length) continue;
      if (!input[0].checked) continue;
      var item =  items[i].getElementsByTagName("td")[0].innerHTML;
      // append element to selection
      selection.innerHTML = selection.innerHTML + "<p>" + item;
    }
  }

  var selection = document.getElementsByTagName("table")[1].getElementsByTagName("tbody")[0];
    selection.innerHTML = "";

    // loop through items
    var items = document.getElementsByTagName("tr");
    for (var i = 0; i < items.length; i++) {
      var input = items[i].getElementsByTagName("input");
      if (!input.length) continue;
      if (!input[0].checked) continue;
      var item =  items[i].getElementsByTagName("td")[0].innerHTML;
      // append element to selection
      selection.innerHTML = selection.innerHTML + "<p>" + item;
    }
  }
