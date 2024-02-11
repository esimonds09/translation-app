<template>
  <v-container>
    <snackbar :message="errorMessage" color="error"></snackbar>
    <v-card class="w-auto pa-6" style="min-width: 200px">
      <div class="d-flex flex-md-row flex-column">
        <LanguageSelect @language="updateLanguage" />
        <div class="d-flex flex-row">
          <VoiceInput
            @recognized="handleRecognizedText"
            @voice-input-active="handleVoiceInputActive"
          />
          <CustomBtn @click="translateText" :buttonText="'Translate'" />
        </div>
      </div>
      <div>
        <TextInput @inputText="updateText" />
      </div>
      <v-divider></v-divider>
      <div class="text-output">
        <p class="ma-2">
          {{ translatedText }}
        </p>
      </div>
      <div>
        <VoiceOutput
          :textToSpeak="translatedText"
          :lang="selectedLanguage"
          @error="handleError"
        />
      </div>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
import VoiceInput from "./features/VoiceInput.vue";
import VoiceOutput from "./features/VoiceOutput.vue";
import Snackbar from "./features/Snackbar.vue";
import CustomBtn from "./UI/CustomBtn.vue";
import TextInput from "@/components/features/TextInput.vue";
import LanguageSelect from "@/components/features/LanguageSelect.vue";

const api = axios.create({
  baseURL: "http://localhost:8000", // Update with FastAPI server's URL
});

export default {
  components: {
    VoiceInput,
    VoiceOutput,
    Snackbar,
    CustomBtn,
    TextInput,
    LanguageSelect,
  },
  data() {
    return {
      recognizedText: "",
      activeInputText: "",
      selectedLanguage: null,
      inputText: "",
      isVoiceInputActive: false,
      translatedText: "",
      errorMessage: "",
    };
  },
  methods: {
    async translateText() {
      if (!this.selectedLanguage) {
        console.log("No language");
        this.errorMessage = "Please select a target language!";
      } else if (!this.inputText.trim()) {
        console.log("No input");
        this.errorMessage = "Input text cannot be empty!";
      } else {
        // Validation succeeded. Clear error.
        console.log("no error");
        this.errorMessage = "";
      }
      if (!this.errorMessage) {
        try {
          const response = await api.post("/translate", {
            text: this.inputText,
            target_lang: this.selectedLanguage,
          });
          this.translatedText = response.data;
          this.errorMessage = "";
        } catch (error) {
          console.error("Translation Error", error);
          // Handle the error and display an error msg to the user
          this.errorMessage = "Translation failed. Please try again.";
        }
      }
    },
    updateLanguage(language) {
      this.selectedLanguage = language;
    },
    updateText(inputText) {
      this.inputText = inputText;
    },
    test() {
      console.log("Button Test");
    },
    handleRecognizedText(text) {
      this.recognizedText = text;
      this.activeInputText = this.isVoiceInputActive ? text : this.inputText;
    },
    handleVoiceInputActive(flag) {
      this.isVoiceInputActive = true;
    },
    handleError(error) {
      this.errorMessage = error;
    },
  },
};
</script>

<style scoped>
.text-output {
  height: 200px;
  border: 1px solid rgb(82, 82, 82);
  border-radius: 5px;
  margin-top: 50px;
}
</style>
