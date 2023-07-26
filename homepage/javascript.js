ftotal = 0; htotal = 0; gtotal = 0; ztotal = 0; ctotal = 0; rtotal = 0;
function function1() {
  let num = document.getElementById('box1').value;
  let remainder = num % 1;
  if (num < 10 && remainder === 0) {
    ftotal = 2 *(Number(num));
    document.getElementById("button1").disabled = false;
  } else {
    document.getElementById("button1").disabled = true;
  }
}

function function2() {
  let num = document.getElementById('box2').value;
  let remainder = num % 1;
  if (num < 10 && remainder === 0) {
    htotal = 100000 *(Number(num));
    document.getElementById("button2").disabled = false;
  } else {
    document.getElementById("button2").disabled = true;
  }
}

function function3() {
  let num = document.getElementById('box3').value;
  let remainder = num % 1;
  if (num < 10 && remainder === 0) {
    gtotal = 30000 *(Number(num));
    document.getElementById("button3").disabled = false;
  } else {
    document.getElementById("button3").disabled = true;
  }
}

function function4() {
  let num = document.getElementById('box4').value;
  let remainder = num % 1;
  if (num < 10 && remainder === 0) {
    ztotal = 100 *(Number(num));
    document.getElementById("button4").disabled = false;
  } else {
    document.getElementById("button4").disabled = true;
  }
}

function function5() {
  let num = document.getElementById('box5').value;
  let remainder = num % 1;
  if (num < 10 && remainder === 0) {
    ctotal = 15 *(Number(num));
    document.getElementById("button5").disabled = false;
  } else {
    document.getElementById("button5").disabled = true;
  }
}

function function6() {
  let num = document.getElementById('box6').value;
  let remainder = num % 1;
  if (num < 10 && remainder === 0) {
    rtotal = 5 *(Number(num));
    document.getElementById("button6").disabled = false;
  } else {
    document.getElementById("button6").disabled = true;
  }
}

function sub() {
  document.getElementById("total").innerHTML = parseFloat(ftotal + htotal + gtotal + ztotal + ctotal + rtotal).toFixed(2);
}

document.addEventListener("click", (evt) => {
  let click = document.getElementById("box1");
  let box = evt.target;
  do {
    if(box == click) {
      return;
  }
  box = box.parentNode;
  } while (box);
  function1();
  });

document.addEventListener("click", (evt) => {
  let click = document.getElementById("box2");
  let box = evt.target;
  do {
    if(box == click) {
      return;
  }
  box = box.parentNode;
  } while (box);
  function2();
  });

document.addEventListener("click", (evt) => {
  let click = document.getElementById("box3");
  let box = evt.target;
  do {
    if(box == click) {
      return;
  }
  box = box.parentNode;
  } while (box);
  function3();
  });

document.addEventListener("click", (evt) => {
  let click = document.getElementById("box4");
  let box = evt.target;
  do {
    if(box == click) {
      return;
  }
  box = box.parentNode;
  } while (box);
  function4();
  });

document.addEventListener("click", (evt) => {
  let click = document.getElementById("box5");
  let box = evt.target;
  do {
    if(box == click) {
      return;
  }
  box = box.parentNode;
  } while (box);
  function5();
  });

document.addEventListener("click", (evt) => {
  let click = document.getElementById("box6");
  let box = evt.target;
  do {
    if(box == click) {
      return;
  }
  box = box.parentNode;
  } while (box);
  function6();
  });