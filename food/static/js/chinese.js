var ccart = document.querySelector("#ccart");
var ctotal = document.querySelector("#ctotal");

//add Chinese Items
function addChinese(cid) {
  //get chiense name
  chineseId = "#ciz" + cid;
  var name = document.querySelector(chineseId).innerHTML;
  //get chinese price
  var radio = "chi" + cid;
  var pri = document.getElementsByName(radio);
  var size, price;
  if (pri[0].checked) {
    price = pri[0].value;
    size = "Half";
    console.log(size);
  } else {
    price = pri[1].value;
    size = "Full";
    console.log(size);
  }

  var orders = JSON.parse(localStorage.getItem("orders"));
  var total = localStorage.getItem("total");
  var cartSize = orders.length;
  console.log(cartSize);

  //saving item and total in localstorage
  orders[cartSize] = [name, size, price];
  localStorage.setItem("orders",JSON.stringify(orders));
  console.log(orders[cartSize]);

  total = Number(total) + Number(price);
  localStorage.setItem("total", total);

  //updating number of item in shopping cart
  var cart = document.querySelector("#cart");
  cart.innerHTML = orders.length;

  butto =
    '<button class="del" onclick="removeChinese(' + cartSize + ')">x</button>';
  ctotal.innerHTML = "Total: " + Math.round(total) + "$";
  ccart.innerHTML +=
    "<li>" + name + " " + size + ":" + price + "$" + butto + "</li>";
}

function cshoppingCart() {
  var orders = JSON.parse(localStorage.getItem("orders"));
  var total = localStorage.getItem("total");
  var cartSize = orders.length;
  ccart.innerHTML = "";
  for (let i = 0; i < cartSize; i++) {
    butto = '<button class="del" onclick="removeChinese(' + i + ')">x</button>';
    ccart.innerHTML +=
      "<li>" +
      orders[i][0] +
      " " +
      orders[i][1] +
      ": " +
      orders[i][2] +
      "$" +
      butto +
      "</li>";
  }
  ctotal.innerHTML = "Total: " + Math.round(total) + " $";
  console.log(ctotal);
}
cshoppingCart();

function removeChinese(n) {
  var orders = JSON.parse(localStorage.getItem("orders"));
  var total = localStorage.getItem("total");
  total = Number(total) - Number(orders[n][2]);
  orders.splice(n, 1);

  //updating number of item in shopping cart
  var cart = document.querySelector("#cart");
  cart.innerHTML = orders.length;

  localStorage.setItem("orders", JSON.stringify(orders));
  localStorage.setItem("total", total);
  cshoppingCart();
}
