document.addEventListener("DOMContentLoaded", function () {
	const form = document.querySelector(".upload-container form");
	const messageContainer = document.getElementById("message-container");

	form.addEventListener("submit", function (event) {
		event.preventDefault();
		const formData = new FormData(form);

		fetch("/submit_photo", {
			method: "POST",
			body: formData,
		})
			.then((response) => response.json())
			.then((data) => {
				if (data.status === "success") {
					messageContainer.innerHTML = `<div class="message success">${data.message}</div>`;
				} else {
					messageContainer.innerHTML = `<div class="message error">${data.message}</div>`;
				}
			})
			.catch((error) => {
				messageContainer.innerHTML = `<div class="message error">Error al subir la foto</div>`;
			});
	});
});
