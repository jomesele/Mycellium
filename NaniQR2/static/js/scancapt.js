let video = document.querySelector("#videoElement");
let captureButton = document.querySelector("#capture");

if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(function (stream) {
      video.srcObject = stream;
    })
    .catch(function (error) {
      console.log("Something went wrong!");
    });
}

captureButton.addEventListener("click", function() {
  let canvas = document.createElement("canvas");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  let context = canvas.getContext("2d");
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  
  let imageData = canvas.toDataURL("image/png");
  
  // Send the image data to the server
  fetch("/upload", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ image: imageData })
  });
});