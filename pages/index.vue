<template>
  <v-app>
    <v-main>
      <v-container>
        <div class="mt-10">
          <h1 class="text-h4">Translator</h1>
        </div>
        <div class="mx-auto">
          <!-- <Translation /> -->
          <Display />
        </div>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
// import Translation from "~/components/Translation.vue";
import Display from "~/components/Display.vue";

export default {
  name: "IndexPage",
  components: {
    // Translation,
    Display,
  },
};
</script>
