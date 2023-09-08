<template>
  <v-container>
    <v-card class="pa-4">
      <v-textarea
        v-model="inputText"
        rows="5"
        outlined
        :label="labelText"
      ></v-textarea>

      <v-btn @click="translateText" color="primary">Translate</v-btn>

      <v-divider class="my-4"></v-divider>

      <v-card v-if="translatedText" outlined>
        <v-card-title>Translated Text</v-card-title>
        <v-card-text>{{ translatedText }}</v-card-text>
      </v-card>
    </v-card>
  </v-container>
</template>
<script>
// Import Axios for making HTTP requests
import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // Update with your FastAPI server's URL
});

export default {
  data() {
    return {
      inputText: "",
      translatedText: "",
      errorMessage: "",
    };
  },
  computed: {
    labelText() {
      return this.inputText ? "" : "Input Text";
    },
  },
  methods: {
    async translateText() {
      const targetLang = "zrt"; // Replace with your desired target language code

      const response = await api.post("/translate", {
        text: this.inputText,
        target_lang: targetLang,
      });
      console.log(response);
      this.translatedText = response.data;
      console.log(this.translateText);
    },
  },
};
</script>
