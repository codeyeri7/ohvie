<template>
  <v-app>
    <v-app-bar
      app
      color="black"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Ohvie Logo"
          class="shrink mr-2"
          contain
          src="@/assets/ohvie_logo_middle.png"
          transition="scale-transition"
          width="60"
        />
      </div>

    <v-spacer></v-spacer>

    <!-- <v-list>
      <v-list-item>Community</v-list-item>
    </v-list> -->
    <v-toolbar-title>Community</v-toolbar-title>

    <v-btn icon>
      <v-icon>mdi-heart</v-icon>
    </v-btn>

    <v-btn icon>
      <v-icon>mdi-magnify</v-icon>
    </v-btn>

    <v-menu
      left
      bottom
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          icon
          v-bind="attrs"
          v-on="on"
        >
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
      </template>

      <v-list>
        <v-list-item @click="() => {}">
          <v-list-item-title>My Wish</v-list-item-title>
        </v-list-item>
        <v-list-item @click="() => {}">
          <v-list-item-title>My Review</v-list-item-title>
        </v-list-item>
        <v-list-item @click="() => {}">
          <v-list-item-title>Profile</v-list-item-title>
        </v-list-item>
        <v-list-item @click="() => {}">
          <v-list-item-title>Sign out</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    </v-app-bar>

  </v-app>
</template>

<script>
  export default {
    name: 'Header',
  }
</script>
