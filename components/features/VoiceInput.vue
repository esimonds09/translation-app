<template>
  <div>
    <CustomBtn @click="startSpeechRecognition" buttonText="Voice Input" />
  </div>
</template>

<script>
import CustomBtn from "../UI/CustomBtn.vue";
export default {
  components: {
    CustomBtn,
  },
  data() {
    return {
      recognizedText: "",
    };
  },
  methods: {
    async startSpeechRecognition() {
      const recognition = new webkitSpeechRecognition(); // Check for browser compatibility
      recognition.lang = "en-US"; // Set the language
      recognition.start(); // Start recognition

      recognition.onresult = (event) => {
        this.recognizedText = event.results[0][0].transcript;
        console.log(this.recognizedText);
        this.$emit("voice-input-active", true);
        this.$emit("recognized", this.recognizedText);
      };

      recognition.onerror = (event) => {
        console.error("Speech recognition error:", event.error);
      };
    },
  },
};
</script>
