<template>
  <div>
    <h1>Translation App</h1>
    <Translation />
  </div>
</template>

<script>
import Translation from "~/components/Translation.vue";
export default {
  name: "IndexPage",
  components: {
    Translation,
  },
};
</script>
