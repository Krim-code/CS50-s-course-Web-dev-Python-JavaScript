function changeHeadings(response) {
    let heading = document.querySelector("#change-heading")
    heading.innerHTML = response
}


addEventListener("DOMContentLoaded",async () => {
    let buttons = document.querySelectorAll("button")
    buttons.forEach(button => {
        button.onclick = async ()=>{
            let data = await fetch(`api/${button.dataset['page']}`)
            let response = await data.json()
            changeHeadings(response)
        }
    })
})
