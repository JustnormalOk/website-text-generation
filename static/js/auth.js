const authForm = document.getElementById('authForm');
const toggleFormText = document.getElementById('toggleText');

let isLogin = true;

authForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const endpoint = isLogin ? '/login' : '/register';

    const response = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    
    const data = await response.json();
    alert(data.message);
});

toggleFormText.addEventListener('click', () => {
    isLogin = !isLogin;
    document.getElementById('formTitle').innerText = isLogin ? 'Login' : 'Register';
    toggleFormText.innerText = isLogin ? "Don't have an account? Register here" : "Already have an account? Login here";
});
