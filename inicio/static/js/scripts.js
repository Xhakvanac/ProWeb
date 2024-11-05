// Selección de elementos
const darkModeToggle = document.getElementById('darkModeToggle');

// Modo Oscuro
darkModeToggle.addEventListener('check', () => {
    document.body.classList.toggle('dark-mode');
    navbar.classList.toggle('dark-mode');
});

 // Abre el modal de inicio de sesión al hacer clic en el botón de navegación
 document.getElementById('loginBtn').onclick = function(event) {
    event.preventDefault();
    document.getElementById('loginModal').style.display = 'block';
};

// Abre el modal de registro y cierra el de inicio de sesión al hacer clic en "¿No tienes cuenta? Regístrate aquí"
document.getElementById('registerBtn').onclick = function(event) {
    event.preventDefault();
    document.getElementById('loginModal').style.display = 'none';
    document.getElementById('registerModal').style.display = 'block';
};

// Abre el modal de inicio de sesión y cierra el de registro al hacer clic en "¿Ya tienes cuenta? Inicia Sesión"
document.getElementById('backToLoginBtn').onclick = function(event) {
    event.preventDefault();
    document.getElementById('registerModal').style.display = 'none';
    document.getElementById('loginModal').style.display = 'block';
};


// Cierra el modal al hacer clic fuera de él
window.onclick = function(event) {
    var loginModal = document.getElementById('loginModal');
    var registerModal = document.getElementById('registerModal');
    if (event.target == loginModal) {
        loginModal.style.display = 'none';
    }
    if (event.target == registerModal) {
        registerModal.style.display = 'none';
    }
};

// JavaScript para mostrar u ocultar los registros
document.getElementById('toggle-registros').addEventListener('click', function() {
    const container = document.getElementById('registros-container');
    if (container.style.display === 'none') {
        container.style.display = 'block';
        this.textContent = 'Ocultar registros';
    } else {
        container.style.display = 'none';
        this.textContent = 'Mostrar registros';
    }
});