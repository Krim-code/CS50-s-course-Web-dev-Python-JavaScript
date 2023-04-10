async function createElements(array) {

    array.forEach(function(element) {
        const elements = document.createElement('div');
    elements.className = 'el'

    const heading = document.createElement('h1')
    heading.innerHTML = element

    elements.appendChild(heading)
    document.querySelector(".containerBox").appendChild(elements)
    })




}
async function getData(num) {
    let response = await fetch(`/scroll/${num}`)
    let data = await response.json();
    return data.pages
}
addEventListener("DOMContentLoaded",async () => {
    const container = document.createElement('div');
    container.className = 'containerBox';
    document.body.appendChild(container);
        let count = 0;
        createElements(await getData(++count))
        window.onscroll = async () => {
            if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
                createElements(await getData(++count))
            } else {
                // s
            }
        }
    }
)