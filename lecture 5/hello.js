document.addEventListener("DOMContentLoaded",function(){
         let headings =  document.querySelector("h1")
         document.querySelector('button').onclick = () => {
           headings.innerHTML === "hello" ? headings.innerHTML = "GoodBuy" : headings.innerHTML = "hello"
         }
      })