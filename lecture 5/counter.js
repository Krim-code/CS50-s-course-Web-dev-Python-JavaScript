if (!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0)
}

const hello = () => {
    let counter = localStorage.getItem('counter')
    document.querySelector("h1").innerHTML = `${++counter}`
    localStorage.setItem('counter', counter)
}

document.addEventListener("DOMContentLoaded",()=>{
    document.querySelector("h1").innerHTML = localStorage.getItem("counter")
    setInterval(hello,1000)
})