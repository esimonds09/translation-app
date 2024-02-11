<!-- <template>
  <v-container>
    <Snackbar :message="errorMessage" color="error" />
    <v-card class="pa-4">
      <div class="d-flex flex-column flex-md-row">
        <v-select
          v-model="selectedLanguage"
          :items="languageOptions"
          label="Translate to:"
          outlined
        ></v-select>
        <div class="d-flex flex-row">
          <VoiceInput
            @recognized="handleRecognizedText"
            @voice-input-active="handleVoiceInputActive"
          />
          <v-btn @click="translateText" color="primary" class="ma-3"
            >Translate</v-btn
          >
        </div>
      </div>

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
import VoiceInput from "@/components/features/VoiceInput.vue";
import VoiceOutput from "@/components/features/VoiceOutput.vue";
import Snackbar from "@/components/features/Snackbar.vue";

const api = axios.create({
  baseURL: "http://localhost:8000", // Update with FastAPI server's URL
});

export default {
  components: {
    VoiceInput,
    VoiceOutput,
    Snackbar,
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
        console.log("No language");
        this.errorMessage = "Please select a target language!";
      } else if (!this.activeInputText.trim()) {
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
            text: this.activeInputText,
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
</script> -->
