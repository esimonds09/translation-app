<!-- <template>
  <v-snackbar v-model="snackbarModel" :color="color">
    {{ message }}
    <v-btn color="white" text @click="snackbarModel = false">Close</v-btn>
  </v-snackbar>
</template>

<script>
export default {
  props: {
    message: String,
    color: String,
  },
  data() {
    return {
      snackbarModel: false,
    };
  },
  watch: {
    snackbarModel(newValue) {
      if (newValue) {
        setTimeout(() => {
          this.snackbarModel = false;
        }, 3000); // Close snackbar after 3 seconds
      }
    },
  },
};
</script> -->
<template>
  <v-snackbar v-model="showSnackbar" :color="color">
    {{ message }}
    <v-btn color="white" text @click="showSnackbar = false">Close</v-btn>
  </v-snackbar>
</template>

<script>
export default {
  props: {
    message: String,
    color: String,
  },
  data() {
    return {
      showSnackbar: false, // Local data property to control the snackbar visibility
    };
  },
  watch: {
    message(newValue) {
      if (newValue) {
        this.showSnackbar = true;
        setTimeout(() => {
          this.showSnackbar = false;
        }, 3000); // Close snackbar after 3 seconds
      }
    },
  },
};
</script>
