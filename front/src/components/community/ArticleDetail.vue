<!--<template>
  <v-container>
    <v-card elevation="10" outlined width="100%" class="mx-auto">
      <v-card-title>
        <span class="mr-2">Detail></span>
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col>
            <v-text-field label="Title" readonly :value="title" ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-textarea
              label="Content"
              readonly
              :value="content"
            >
            </v-textarea>
          </v-col>
        </v-row>
        <v-divider></v-divider>
				<v-row>
					<v-col cols="12" md="11" style="padding: 0px 12px;">
						<v-textarea
							clearable
							clear-icon="mdi-close-circle"
							rows="2"
							no-resize
							full-width
							v-model="comment"
						></v-textarea>
					</v-col>
					<v-col md="1" align-self="center" style="padding: 0px 10px;">
						<Button
							@click="commentSave"
							color="indigo"
							rounded
							small
							iconName="mdi-pencil"
							btnName="Save"
						></Button>
					</v-col>
				</v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewDetail',
  methods: {
    commentSave (article_pk) {
      const COMMENT_URL = 'http://127.0.0.1:8000/community/articles/' + article_pk +'/comments'
      axios.get(COMMENT_URL)
      .then((response) => {
          console.log(response)
        })
      .catch((error) => {
        console.error(error)
      })
    }
  }
}
</script>

<style>

</style>-->