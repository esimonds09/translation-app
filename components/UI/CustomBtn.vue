<template>
  <v-btn
    :color="color"
    class="ma-2"
    style="width: 170px"
    @click="$emit('click')"
  >
    <slot>{{ buttonText }}</slot>
  </v-btn>
</template>

<script>
export default {
  props: {
    color: {
      type: String,
      default: "primary",
    },
    buttonText: {
      type: String,
      required: true,
    },
  },
};
</script>

<style></style>
