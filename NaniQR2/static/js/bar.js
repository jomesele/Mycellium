let video = document.querySelector("video");
let div = document.querySelector("div.message");
let canvas = document.querySelector("canvas");
let ctx = canvas.getContext("2d");
let rect = video.getBoundingClientRect();
let interval = null;
let scanFrame = null;
let coordinates = null;
let doUpdate = true;

video.addEventListener("loadedmetadata", () => {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
});

function updateFrameOfVideo() {
    if (doUpdate) ctx.drawImage(video, 0, 0);
    else if (coordinates !== null) {
        let imageObj = new Image();
        imageObj.src = scanFrame;
        ctx.drawImage(imageObj, 0, 0);
        ctx.beginPath();
        ctx.lineCap = "round";
        ctx.lineWidth = 5;
        ctx.strokeStyle = "red";
        ctx.moveTo(coordinates[0][0], coordinates[0][1]);
        for (let i = 1; i <= 4; i++) {
            ctx.lineTo(coordinates[i % 4][0], coordinates[i % 4][1]);
        }
        ctx.stroke();
    }
}

window.setInterval(updateFrameOfVideo, 1000 / 30);

window.onload = () => {
    navigator.mediaDevices.getUserMedia({
        video: {
            width: { ideal: 1280 },
            height: { ideal: 720 },
            facingMode: "environment"
        },
        audio: false
    }).then((stream) => {
        document.querySelector("video").srcObject = stream;
        document.querySelector("video").play();

        function capture() {
            let dataURL = doUpdate ? canvas.toDataURL("image/png") : "";
            scanFrame = dataURL;

            let formData = new FormData();
            formData.append("url", dataURL);

            window.fetch("/decode", {
                method: "POST",
                body: JSON.stringify({
                'Metar': formData,
                }),
            })
            .then(response => response.json())
            .then(result => {
                if (result.success) {
                    div.textContent = result.result;
                    div.style.fontWeight = "bold";
                    doUpdate = false;
                    coordinates = result.coordinates;
                    window.setTimeout(capture, 5000);
                } else {
                    div.textContent = "Detecting...";
                    div.style.fontWeight = "normal";
                    doUpdate = true;
                    coordinates = null;
                    window.setTimeout(capture, 1000);
                }
            });
        }

        capture();
    });
}