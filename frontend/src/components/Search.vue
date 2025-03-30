<template>
  <div class="search-container">
    <h1>Busca de Operadoras</h1>
    <!-- Campo de entrada para o termo de busca -->
    <input
      v-model="termo"
      @input="buscar"
      placeholder="Digite o termo de busca"
    />
    <ul>
      <!-- Lista de resultados / AO CLICAR ELA EXPANDE-->
      <li
        v-for="(resultado, index) in resultados"
        :key="index"
        @click="toggleExpand(index)"  
        class="result-item"
        :class="{ expanded: expandedIndex === index }"
      >
        <div>
          <!-- Nome Fantasia e Modalidade -->
          <strong>{{ resultado.Nome_Fantasia }}</strong> - {{ resultado.Modalidade }}
          <br />
          <small>
            <!-- Cidade e Estado -->
            <strong>Cidade:</strong> {{ resultado.Cidade }}, {{ resultado.UF }}
          </small>
        </div>

        <!-- Exibe mais informações se o item for clicado expandindo -->
        <div v-if="expandedIndex === index" class="details">
          <small>
            <strong>Razão Social:</strong> {{ resultado.Razao_Social }}<br />
            <strong>CNPJ:</strong> {{ resultado.CNPJ }}<br />
            <strong>Telefone:</strong> {{ resultado.Telefone }}<br />
            <strong>Representante:</strong> {{ resultado.Representante }}<br />
            <strong>Endereço:</strong> {{ resultado.Logradouro }}, {{ resultado.Numero }} - {{ resultado.Bairro }}<br />
            <strong>Complemento:</strong> {{ resultado.Complemento }}<br />
            <strong>Registro ANS:</strong> {{ resultado.Registro_ANS }}<br />
            <strong>Data Registro ANS:</strong> {{ resultado.Data_Registro_ANS }}<br />
            <strong>E-mail:</strong> {{ resultado.Endereco_eletronico }}
          </small>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      termo: "", // Termo de busca digitado pelo usuário
      resultados: [], // Resultados retornados pela API
      expandedIndex: null, // Índice do item atualmente expandido
    };
  },
  methods: {
    // Método para buscar resultados da API
    async buscar() {
      if (this.termo) {
        try {
          const response = await fetch(
            `http://127.0.0.1:5000/buscar?termo=${this.termo}`
          );
          this.resultados = await response.json(); // Atualiza os resultados
          console.log(this.resultados); // Log dos resultados para depuração
        } catch (error) {
          console.error("Erro ao buscar dados:", error); // Log de erro
        }
      } else {
        this.resultados = []; // Limpa os resultados se o termo estiver vazio
      }
    },
    // Método para alternar a expansão de um item
    toggleExpand(index) {
      this.expandedIndex = this.expandedIndex === index ? null : index;
    },
  },
};
</script>