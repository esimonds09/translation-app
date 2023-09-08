<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <v-col cols="12">
            <h1 class="text-h4">Translation App</h1>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <Translation />
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
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
