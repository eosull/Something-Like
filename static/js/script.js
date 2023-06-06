
// Timeout for messages
setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000)

// Cycle through Categories on Homepage
// function showCategories() {
//     var categories = ['Music', 'Films', 'Books', 'Tv', 'Culture'];
//     var text = document.getElementById('looping-categories');

//     for (let i = 0; i < categories.length; i++) {
//         setTimeout(function() {
//             text.textContent = categories[i];
//             text.setAttribute("class", `${categories[i]}-post`);
//         }, i * 1000)
//     }
// }

// showCategories();
