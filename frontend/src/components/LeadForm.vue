<template>
  <div class="form-container">
    <h1 class="title">Cadastre-se para receber seu treino grátis!</h1>
    
    <input 
      v-model="email" 
      @input="validateEmail"
      @blur="validateEmail" 
      placeholder="Digite seu melhor e-mail" 
      type="email" 
      class="email-input"
      :class="{ 'input-error': error }"
    />
    <p v-if="error" class="error-message">{{ error }}</p>
    
    <button 
      @click="submitForm" 
      class="submit-btn"
      :disabled="!isFormValid"
    >
      Quero meu treino!
    </button>
    
    <p v-if="message" class="message">{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      message: "",
      error: "",
    };
  },
  computed: {
    isFormValid() {
      return this.email && !this.error;
    }
  },
  methods: {
    validateEmail() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!this.email.trim()) {
        this.error = "⚠️ Por favor, digite seu e-mail.";
      } else if (!emailRegex.test(this.email)) {
        this.error = "⚠️ E-mail inválido. Exemplo: nome@exemplo.com";
      } else {
        this.error = "";
      }
    },
    
    async submitForm() {
      this.validateEmail();
      if (!this.isFormValid) return;
      
      try {
        const response = await fetch("https://km-homefit-fastapi.onrender.com/api/leads", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email: this.email }),
        });
        
        if (!response.ok) {
          const error = await response.json();
          throw new Error(error.detail || "Erro ao cadastrar");
        }
        
        this.message = "✅ Cadastro realizado!";
        this.email = "";
      } catch (error) {
        this.message = `❌ ${error.detail}`;
      }
    },
  },
};
</script>

<style scoped>
.form-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Arial', sans-serif;
  text-align: center;
  background-color: #f8f9fa;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.title {
  color: #2c3e50;
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
}

.email-input {
  width: 100%;
  padding: 12px;
  font-size: 1rem;
  border: 2px solid #ddd;
  border-radius: 5px;
  margin-bottom: 1rem;
  transition: border-color 0.3s;
}

.email-input:focus {
  border-color: #42b983; /* Verde Vue.js */
  outline: none;
}

.submit-btn {
  width: 100%;
  padding: 12px;
  background-color: #42b983; /* Verde Vue.js */
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-btn:hover {
  background-color: #3aa876; /* Verde mais escuro */
}

.message {
  margin-top: 1rem;
  font-size: 0.9rem;
  color: #333;
}


.input-error {
  border-color: #ff4444 !important;
}

.error-message {
  color: #ff4444;
  font-size: 0.85rem;
  margin-top: -0.5rem;
  margin-bottom: 1rem;
  text-align: left;
}

.submit-btn:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
</style>