<template>
  <div class="wrapper">
    <b-table :data="tableData" striped hoverable>
      <template slot-scope="props">
        <b-table-column v-for="(column, index) in tableColumns" :key="index" :label="column.title" centered>
          <template v-if="column.field == 'block'">
            <div class="box small-box is-white">{{ props.row[column.field] }}</div>
          </template>
          <template v-if="props.row[column.field] != null && column.field != 'block'">
            <div class="zone box small-box" :class="props.row[column.field].className">
              {{ props.row[column.field].stageLabel }}
            </div>
          </template>
        </b-table-column>
      </template>
    </b-table>
  </div>
</template>

<script>
import Vue from "vue";

export default Vue.extend({
  data: function() {
    return {}
  },
  components: {
  },
  props: {
    selectedDaysData: Array,
    selectedDate: Date,
    selectedZone: String,
    selectedStage: Number,
    blockTitles: Array
  },
  computed: {
    tableColumns: function() {
      const headers = [{ title: "Block", field: "block" }];
      const dayHeaders = this.selectedDaysData.map((d, i) => ({
        title: d.label,
        field: `day${i}`
      }));

      return headers.concat(dayHeaders);
    },

    tableData: function() {
      const rows = [];
      if (this.selectedDaysData.length == 0) return [];

      for (let blockIndex = 0; blockIndex < 12; blockIndex += 1) {
        const row = {};
        
        row["block"] = this.blockTitles[blockIndex]
        
        rows.push(row);
      }

      for (const day of this.selectedDaysData) {
          for (const block of day.blocks){
            if (block.blockIndex >= 0 && rows[block.blockIndex] != null)
              rows[block.blockIndex][`day${day.dayIndex}`] = block;
          }
        }
        
      return rows;
    }
  }
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
