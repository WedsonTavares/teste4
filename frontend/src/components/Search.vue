
<template>
  <div class="search-container">
    <h1>Busca de Operadoras</h1>
    <input
      v-model="termo"
      @input="buscar"
      placeholder="Digite o termo de busca"
    />
    <ul>
      <li v-for="(resultado, index) in resultados" :key="index">
        <strong>{{ resultado.Nome_Fantasia }}</strong> - {{ resultado.Modalidade }}
        <br />
        <small>{{ resultado.Cidade }}, {{ resultado.UF }}</small>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      termo: "", 
      resultados: [], 
    };
  },
  methods: {
    async buscar() {
      if (this.termo) {
        try {
          const response = await fetch(
            `http://127.0.0.1:5000/buscar?termo=${this.termo}`
          );
          this.resultados = await response.json();
        } catch (error) {
          console.error("Erro ao buscar dados:", error);
        }
      } else {
        this.resultados = [];
      }
    },
  },
};
</script>



