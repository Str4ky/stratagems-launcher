let lastTouchEnd = 0;
let audio = new Audio('assets/audio/input.wav');
let json = 'assets/json/config.json';
let open_key;
let port;
let url;

fetch(json)
.then(response => response.json())
.then(data => {
    url = data.url;
    port = data.server_port;
    keys = data.keys;
})

    
document.addEventListener('touchend', (event) => {
    const now = new Date().getTime();
    if (now - lastTouchEnd <= 300) {
        event.preventDefault();
    }
    lastTouchEnd = now;
});

function press(action){
    key = keys[action];
    fetch(`${url}:${port}/keypress/${key}`)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
    audio.play();
}