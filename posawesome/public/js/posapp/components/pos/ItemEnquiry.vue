<template>
  <v-row justify="center">
    <v-dialog v-model="itemEnquiry" max-width="400px">
      <v-card>
        <v-card-text class="pa-0">
          <v-container>
            <v-row>
              <v-col cols="12" class="pa-1">
                  <v-autocomplete
                    class="mx-auto w-75"
                    label="Medicine Name"
                    dense
                    outlined
                    prepend-inner-icon="mdi-medical-bag"
                    background-color="white"
                    hide-details
                    clearable
                    v-model="medicine"
                    :items="items"
                  ></v-autocomplete>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" dark @click="close_enq">{{__('Close')}}</v-btn>
          <v-btn color="primary" dark @click="submit_enq">{{__('Submit')}}</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import { evntBus } from '../../bus';
export default {
  data: () => ({
    itemEnquiry: false,
    items: []
  }),
  watch: {},
  methods: {
    close_enq() {
      this.itemEnquiry = false;
    },
    submit_enq() {
      frappe.call({
          method: "idl4gen.tasks.add_enquiry",
          args: {
            "item_code": this.medicine
          }
      })
      this.itemEnquiry = false;
    }
  },
  created: function () {
    evntBus.$on('open_itemEnquiry', () => {
      JSON.parse(localStorage.getItem('items_storage')).forEach((element) => {
        this.items.push(element.item_code);
      });
      this.itemEnquiry = true;
    });
  },
};
</script>
