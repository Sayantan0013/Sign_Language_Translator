navigator.getUserMedia = navigator.getUserMedia ||
    navigator.webkitGetUserMedia ||
    navigator.mozGetUserMedia;
navigator.getUserMedia({ video: true, audio: false }, (localMediaStream) => {
    var video = document.querySelector('video')
    video.srcObject = localMediaStream
    video.autoplay = true
}, (e) => { })