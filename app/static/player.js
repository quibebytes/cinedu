const player = new Plyr('#player', {

    controls: [],

    youtube: {
        noCookie: true,
        rel: 0,
        modestbranding: 1
    }

});

const playBtn = document.getElementById("playBtn");
const backBtn = document.getElementById("backBtn");
const nextBtn = document.getElementById("nextBtn");

const muteBtn = document.getElementById("muteBtn");
const captionBtn = document.getElementById("captionBtn");
const fullscreenBtn = document.getElementById("fullscreenBtn");

const timeline = document.getElementById("timeline");
const progress = document.getElementById("progress");

const current = document.getElementById("current");
const duration = document.getElementById("duration");

const overlay = document.getElementById("overlay");

let dragging = false;
let hideTimer;



/* ===========================
   PLAYER READY
=========================== */

player.on("ready", () => {

    duration.textContent = format(player.duration);

    update();

});



/* ===========================
   PLAY
=========================== */

playBtn.onclick = () => {

    player.togglePlay();

};



player.on("play", () => {

    playBtn.textContent = "⏸";

});



player.on("pause", () => {

    playBtn.textContent = "▶";

});



/* ===========================
   MUTE
=========================== */

muteBtn.onclick = () => {

    player.muted = !player.muted;

};



player.on("volumechange", () => {

    muteBtn.textContent = player.muted ? "🔈" : "🔊";

});



/* ===========================
   SEEK
=========================== */

backBtn.onclick = () => {

    player.currentTime -= 10;

};



nextBtn.onclick = () => {

    player.currentTime += 10;

};



/* ===========================
   TIMELINE
=========================== */

function update() {

    if (!dragging && player.duration) {

        progress.style.width =
            (player.currentTime / player.duration) * 100 + "%";

        current.textContent =
            format(player.currentTime);

        duration.textContent =
            format(player.duration);

    }

    requestAnimationFrame(update);

}



timeline.addEventListener("click", seek);

timeline.addEventListener("mousedown", () => dragging = true);

document.addEventListener("mouseup", () => dragging = false);

document.addEventListener("mousemove", e => {

    if (dragging)
        seek(e);

});



function seek(e) {

    const rect = timeline.getBoundingClientRect();

    let percent = (e.clientX - rect.left) / rect.width;

    percent = Math.max(0, Math.min(1, percent));

    player.currentTime = percent * player.duration;

}



/* ===========================
   FULLSCREEN
=========================== */

fullscreenBtn.onclick = () => {

    fullscreenBtn.onclick = async () => {

    if (!document.fullscreenElement) {

        await document.querySelector(".player").requestFullscreen();

    } else {

        await document.exitFullscreen();

    }

    };

};



/* ===========================
   LEGENDAS
=========================== */

captionBtn.onclick = () => {

    player.toggleCaptions();

};



/* ===========================
   ESCONDER CONTROLES
=========================== */

function showControls() {

    overlay.classList.remove("hide");

    clearTimeout(hideTimer);

    if (!player.paused) {

        hideTimer = setTimeout(() => {

            overlay.classList.add("hide");

        }, 2500);

    }

}



document.addEventListener("mousemove", showControls);

document.addEventListener("keydown", showControls);



/* ===========================
   TECLADO
=========================== */

document.addEventListener("keydown", e => {

    switch (e.code) {

        case "Space":

            e.preventDefault();

            player.togglePlay();

            break;

        case "ArrowLeft":

            player.currentTime -= 5;

            break;

        case "ArrowRight":

            player.currentTime += 5;

            break;

        case "KeyM":

            player.muted = !player.muted;

            break;

        case "KeyF":

            fullscreenBtn.onclick = async () => {

            if (!document.fullscreenElement) {

                await document.querySelector(".player").requestFullscreen();

            } else {

                await document.exitFullscreen();

            }

            };

            break;

    }

});



/* ===========================
   TEMPO
=========================== */

function format(sec) {

    sec = Math.floor(sec);

    const m = Math.floor(sec / 60);

    const s = sec % 60;

    return String(m).padStart(2, "0") + ":" +
           String(s).padStart(2, "0");

}