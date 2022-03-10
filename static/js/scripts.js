// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Capture image
let camera_button = document.querySelector("#start-camera");
let video = document.querySelector("#video");
let click_button = document.querySelector("#click-photo");
let canvas = document.querySelector("#canvas");

camera_button.addEventListener('click', async function() {
   	let stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
	video.srcObject = stream;
});

click_button.addEventListener('click', function() {
   	canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
   	let image_data_url = canvas.toDataURL('image/jpeg');

   	// data url of the image
   	console.log(image_data_url);
});

// capture video
//let camera_button = document.querySelector("#start-camera");
//let video = document.querySelector("#video");
//let start_button = document.querySelector("#start-record");
//let stop_button = document.querySelector("#stop-record");
//let download_link = document.querySelector("#download-video");
//
//let camera_stream = null;
//let media_recorder = null;
//let blobs_recorded = [];
//
//camera_button.addEventListener('click', async function() {
//   	camera_stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
//	video.srcObject = camera_stream;
//});
//
//start_button.addEventListener('click', function() {
//    // set MIME type of recording as video/webm
//    media_recorder = new MediaRecorder(camera_stream, { mimeType: 'video/webm' });
//
//    // event : new recorded video blob available
//    media_recorder.addEventListener('dataavailable', function(e) {
//		blobs_recorded.push(e.data);
//    });
//
//    // event : recording stopped & all blobs sent
//    media_recorder.addEventListener('stop', function() {
//    	// create local object URL from the recorded video blobs
//    	let video_local = URL.createObjectURL(new Blob(blobs_recorded, { type: 'video/webm' }));
//    	download_link.href = video_local;
//    });
//
//    // start recording with each recorded blob having 1 second video
//    media_recorder.start(1000);
//});
//
//stop_button.addEventListener('click', function() {
//	media_recorder.stop();
//});