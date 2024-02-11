<template>
  <v-select
    v-model="selectedLanguage"
    :items="languageOptions"
    label="Translate to:"
    outlined
    @change="emitLanguage"
    class="w-100 pr-2"
    style="max-width: 200px"
  ></v-select>
</template>

<script>
export default {
  data() {
    return {
      selectedLanguage: null,
      languageOptions: [
        { text: "English", value: "en" },
        { text: "German", value: "de" },
        { text: "Dutch", value: "nl" },
        { text: "Russian", value: "ru" },
        { text: "Chinese", value: "zh" },
        { text: "Spanish", value: "es" },
        { text: "Hindi", value: "hi" },
        { text: "Arabic", value: "ar" },
        { text: "Portuguese", value: "pt" },
        { text: "Japanese", value: "ja" },
        { text: "Indonesian", value: "id" },
        { text: "Turkish", value: "tr" },
        { text: "Korean", value: "ko" },
        { text: "French", value: "fr" },
        { text: "Nepali", value: "ne" },
        { text: "Italian", value: "it" },
        { text: "Czech", value: "cs" },
        { text: "Greek", value: "el" },
        { text: "Norwegian", value: "nb" },
        { text: "Swedish", value: "sv" },
      ],
    };
  },
  methods: {
    emitLanguage() {
      this.$emit("language", this.selectedLanguage);
    },
  },
};
</script>

<style></style>
