function changeHeadings(text,img) {
    let heading = document.querySelector("#change-heading")
    heading.innerHTML = text
    document.body.style.background = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${img} ) no-repeat fixed center`
    document.body.style.backgroundSize = "cover"
}


addEventListener("DOMContentLoaded",async () => {
    let buttons = document.querySelectorAll("button")
    buttons.forEach(button => {
        button.onclick = async ()=>{
            let data = await fetch(`api/${button.dataset['page']}`)
            let response = await data.json()
            await changeHeadings(response.text,response.img)
        }
    })
})
