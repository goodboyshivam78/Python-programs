
// let btn = document.querySelector(".class")
// let btn = document.querySelector("#id")
let btn = document.querySelector("button")
// let btn = document.getElementById("")
// let btn = document.getElementsByClassName("")
// let btn = document.getElementsByTagName("h1")
let ck = true;
btn.addEventListener("click", () => {
    const greeting = document.getElementById("greeting");
    if (ck == true) {
        greeting.style.display = "block";
        ck = false;
    }
    else {
        greeting.style.display = "none"
        ck = true
    }

})
