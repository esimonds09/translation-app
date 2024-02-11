<template>
  <div>
    <CustomBtn @click="speakText" buttonText="Speak Text" />
  </div>
</template>

<script>
import CustomBtn from "../UI/CustomBtn.vue";

export default {
  components: { CustomBtn },
  props: ["textToSpeak", "lang"],
  data() {
    return {
      errorMessage: "",
    };
  },
  methods: {
    async speakText() {
      if (!this.textToSpeak) {
        this.errorMessage = "No translated text available!";
        this.$emit("error", this.errorMessage);
        return;
      }

      const utterance = new SpeechSynthesisUtterance(this.textToSpeak);
      const langCode = this.mapLanguageToCode(this.lang);

      await this.ensureVoicesLoaded();

      const selectedVoice = speechSynthesis
        .getVoices()
        .find((voice) => voice.lang === langCode);

      if (!selectedVoice) {
        this.errorMessage = "No voice available for the selected language.";
        this.$emit("error", this.errorMessage);
        return;
      }

      //   Optional: Adjust voice and other settings
      utterance.voice = selectedVoice;
      utterance.pitch = 1;
      utterance.rate = 1;
      utterance.lang = langCode;
      speechSynthesis.speak(utterance);
    },
    async ensureVoicesLoaded() {
      if (speechSynthesis.getVoices().length === 0) {
        return new Promise((resolve) => {
          speechSynthesis.onvoiceschanged = () => {
            speechSynthesis.onvoiceschanged = null;
            resolve();
          };
        });
      }
    },
    mapLanguageToCode(language) {
      const languageMap = {
        en: "en-US", // English
        de: "de-DE", // German
        nl: "nl-NL", // Dutch
        ru: "ru-RU", // Russian
        zh: "zh-CN", // Chinese
        es: "es-ES", // Spanish (Spain)
        hi: "hi-IN", // Hindi
        ar: "ar-SA", // Arabic
        pt: "pt-PT", // Portuguese (Portugal)
        ja: "ja-JP", // Japanese
        id: "id-ID", // Javanese
        tr: "tr-TR", // Turkish
        ko: "ko-KO", // Korean
        fr: "fr-FR", // French (France)
        ne: "ne-NP", // Nepali
        it: "it-IT", // Italian
        cs: "cs-CS", // Czech
        el: "el-EL", // Greek
        nb: "no-NO", // Norwegian
        sv: "sv-SE", // Swedish
      };
      return languageMap[language] || "en-US";
    },
  },
};
</script>
