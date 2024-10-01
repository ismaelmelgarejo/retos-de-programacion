// Mensaje de bienvenida al cargar la página
window.onload = function() {
    console.log("¡Bienvenido a mi sitio web!");
};

// Ejemplo de interacción simple: cambiar el color de fondo al hacer clic
document.querySelector('h1').addEventListener('click', function() {
    document.body.style.backgroundColor = '#e0f7fa';
});
