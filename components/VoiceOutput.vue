<template>
  <div>
    <button @click="speakText">Speak Text</button>
  </div>
</template>

<script>
export default {
  props: ["textToSpeak", "lang"],
  methods: {
    async speakText() {
      const utterance = new SpeechSynthesisUtterance(this.textToSpeak);
      const langCode = this.mapLanguageToCode(this.lang);

      //   Optional: Adjust voice and other settings
      utterance.voice = this.getVoiceByLangCode(langCode);
      utterance.pitch = 1;
      utterance.rate = 1;
      utterance.lang = langCode;
      speechSynthesis.speak(utterance);
    },
    mapLanguageToCode(language) {
      const languageMap = {
        en: "en-US", // English
        de: "de-DE", // German
        nl: "nl-NL", // Dutch
        ru: "ru-RU", // Russian
      };
      return languageMap[language] || "en-US";
    },
    getVoiceByLangCode(langCode) {
      const voices = speechSynthesis.getVoices();
      return voices.find((voice) => voice.lang === langCode);
    },
  },
};
</script>
