<template>
  <v-textarea
    v-model="activeInputText"
    rows="5"
    outlined
    :label="labelText"
  ></v-textarea>
</template>

<script>
export default {
  data() {
    return {
      activeInputText: "",
    };
  },
  watch: {
    activeInputText(newValue) {
      this.$emit("inputText", newValue);
    },
  },
  computed: {
    labelText() {
      return this.activeInputText ? "" : "Input Text";
    },
  },
};
</script>

<style></style>
