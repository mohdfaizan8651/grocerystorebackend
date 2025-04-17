<template>
    <div class="search-component">
      <input
        type="text"
        v-model="query"
        @input="onSearch"
        placeholder="Search..."
      />
      <ul v-if="filteredItems.length">
        <li v-for="item in filteredItems" :key="item.id">
          {{ item.name }}
        </li>
      </ul>
      <p v-else>No results found.</p>
      Search
    </div>
  </template>
  
  <script>
  export default {
    props: {
      items: {
        type: Array,
        required: true,
      },
    },
    data() {
      return {
        query: '',
      };
    },
    computed: {
      filteredItems() {
        return this.items.filter(item =>
          item.name.toLowerCase().includes(this.query.toLowerCase())
        );
      },
    },
    methods: {
      onSearch() {
        this.$emit('search', this.query);
      },
    },
  };
  </script>
  
  <style>

  </style>
  