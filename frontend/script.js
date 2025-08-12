document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        if (data.audio_url) {
            const audioPlayer = document.getElementById("audioPlayer");
            audioPlayer.src = data.audio_url;
            audioPlayer.play();
        } else {
            alert("Error: " + data.error);
        }
    } catch (err) {
        console.error("Upload failed:", err);
        alert("Failed to upload file");
    }
});
