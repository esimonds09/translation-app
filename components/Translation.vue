<template>
  <v-container>
    <v-card class="pa-4">
      <v-row>
        <v-col cols="12" sm="2">
          <v-select
            v-model="selectedLanguage"
            :items="languageOptions"
            label="Translate to:"
            outlined
          ></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" sm="12">
          <v-textarea
            v-model="inputText"
            rows="5"
            outlined
            :label="labelText"
          ></v-textarea>
        </v-col>
      </v-row>
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
      selectedLanguage: null,
      translatedText: "",
      errorMessage: "",
      languageOptions: [
        { text: "English", value: "en" },
        { text: "German", value: "de" },
        { text: "Dutch", value: "nl" },
        { text: "Russian", value: "ru" },
      ],
    };
  },
  computed: {
    labelText() {
      return this.inputText ? "" : "Input Text";
    },
  },
  methods: {
    async translateText() {
      // const targetLang = "ru"; // Replace with your desired target language code
      if (!this.selectedLanguage) {
        this.errorMessage = "Please select a target language!";
        return;
      }
      console.log(this.selectedLanguage);
      const response = await api.post("/translate", {
        text: this.inputText,
        target_lang: this.selectedLanguage,
      });
      console.log(response);
      this.translatedText = response.data;
      console.log(this.translateText);
    },
  },
};
</script>
