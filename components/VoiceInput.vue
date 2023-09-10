<template>
  <div>
    <button @click="startSpeechRecognition">Start Voice Input</button>
    <!-- <p>{{ recognizedText }}</p> -->
  </div>
</template>

<script>
export default {
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
