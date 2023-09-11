<template>
  <v-container>
    <v-card class="pa-4">
      <v-row>
        <v-col cols="12" sm="4">
          <v-select
            v-model="selectedLanguage"
            :items="languageOptions"
            label="Translate to:"
            outlined
          ></v-select>
        </v-col>
        <v-col cols="12" sm="3">
          <VoiceInput
            @recognized="handleRecognizedText"
            @voice-input-active="handleVoiceInputActive"
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" sm="12">
          <v-textarea
            v-model="activeInputText"
            rows="5"
            outlined
            :label="labelText"
          ></v-textarea>
        </v-col>
      </v-row>
      <v-btn @click="translateText" color="primary" class="ma-3"
        >Translate</v-btn
      >

      <v-divider class="my-4"></v-divider>
      <v-row>
        <v-col cols="12" sm="3">
          <VoiceOutput :textToSpeak="translatedText" :lang="selectedLanguage" />
        </v-col>
      </v-row>
      <v-card v-if="translatedText" outlined>
        <v-row>
          <v-card-title>Translated Text</v-card-title>
          <v-card-text>{{ translatedText }}</v-card-text>
        </v-row>
      </v-card>
    </v-card>
  </v-container>
</template>
<script>
// Import Axios for making HTTP requests
import axios from "axios";
import VoiceInput from "@/components/VoiceInput.vue";
import VoiceOutput from "@/components/VoiceOutput.vue";

const api = axios.create({
  baseURL: "http://localhost:8000", // Update with FastAPI server's URL
});

export default {
  components: {
    VoiceInput,
    VoiceOutput,
  },
  data() {
    return {
      inputText: "",
      recognizedText: "",
      activeInputText: "",
      selectedLanguage: null,
      translatedText: "",
      isVoiceInputActive: false,
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
      return this.activeInputText ? "" : "Input Text";
    },
  },
  methods: {
    async translateText() {
      if (!this.selectedLanguage) {
        this.errorMessage = "Please select a target language!";
        return;
      }

      try {
        const response = await api.post("/translate", {
          text: this.activeInputText,
          target_lang: this.selectedLanguage,
        });
        this.translatedText = response.data;
      } catch (error) {
        console.error("Translation Error", error);
        // Handle the error and display an error msg to the user
        this.errorMessage = "Translation failed. Please try again.";
      }
    },
    handleRecognizedText(text) {
      this.recognizedText = text;
      this.activeInputText = this.isVoiceInputActive ? text : this.inputText;
    },
    handleVoiceInputActive(flag) {
      this.isVoiceInputActive = true;
    },
  },
  created() {
    this.$on("voice-input-active", this.handleVoiceInputActive);
  },
};
</script>
