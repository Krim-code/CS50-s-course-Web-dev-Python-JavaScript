document.addEventListener("DOMContentLoad",async () => {
    let GetInfo = await fetch("https://www.postman-echo.com/get")
    const body = document.querySelector('body')
    const p = document.createElement("p")
    console.log(GetInfo.headers.get('host'))
    p.innerHTML = GetInfo.headers.get('host')
    body.append(p)
})

