//* Toda la logica para mostrar fotos en la pantalla gigante
document.addEventListener("DOMContentLoaded", function () {
	let photos = JSON.parse(document.getElementById("photos-data").textContent);
	let currentIndex = 0;
	const eventId = document.getElementById("event-id").textContent;

	console.log("Fotos iniciales:", photos);

	//* Funcion para mostrar la siguiente foto
	function showNextPhoto() {
		if (photos.length > 0) {
			currentIndex = (currentIndex + 1) % photos.length;
			document.getElementById("current-photo").src =
				"data:image/png;base64," + photos[currentIndex]["image"];
			console.log("Mostrando foto - Indice:", currentIndex);
		} else {
			console.log("No hay fotos para mostrar.");
		}
	}

	setInterval(showNextPhoto, 3000);

	//* Funcion para actualizar las fotos aprobadas
	function updatePhotos() {
		console.log("Buscando fotos actualizadas...");
		fetch(`/get_approved_photos?event_id=${eventId}`)
			.then((response) => response.json())
			.then((data) => {
				if (data.length > 0) {
					const newPhotos = data;
					// Fusionar nuevas fotos con las existentes, evitando duplicados
					const mergedPhotos = [
						...photos,
						...newPhotos.filter(
							(newPhoto) => !photos.some((photo) => photo.image === newPhoto.image)
						),
					];
					photos = mergedPhotos;
					console.log("Fotos actualizadas:", photos);
				}
			});
	}

	setInterval(updatePhotos, 10000); // Actualizar cada 10 segundos

	//* Funcion para activar/desactivar el modo de pantalla completa
	function toggleFullscreen() {
		const elem = document.documentElement;
		if (!document.fullscreenElement) {
			if (elem.requestFullscreen) {
				elem.requestFullscreen();
			} else if (elem.mozRequestFullScreen) {
				// Firefox
				elem.mozRequestFullScreen();
			} else if (elem.webkitRequestFullscreen) {
				// Chrome, Safari and Opera
				elem.webkitRequestFullscreen();
			} else if (elem.msRequestFullscreen) {
				// IE/Edge
				elem.msRequestFullscreen();
			}
		} else {
			if (document.exitFullscreen) {
				document.exitFullscreen();
			} else if (document.mozCancelFullScreen) {
				// Firefox
				document.mozCancelFullScreen();
			} else if (document.webkitExitFullscreen) {
				// Chrome, Safari and Opera
				document.webkitExitFullscreen();
			} else if (document.msExitFullscreen) {
				// IE/Edge
				document.msExitFullscreen();
			}
		}
	}

	document.addEventListener("fullscreenchange", function () {
		const fullscreenButton = document.getElementById("fullscreen-button");
		if (!document.fullscreenElement) {
			fullscreenButton.style.display = "block";
		} else {
			fullscreenButton.style.display = "none";
		}
	});

	// Mostrar el boton de pantalla completa al cargar la pagina si no esta en pantalla completa
	if (!document.fullscreenElement) {
		document.getElementById("fullscreen-button").style.display = "block";
	}

	document.getElementById("fullscreen-button").addEventListener("click", toggleFullscreen);
});
