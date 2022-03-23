<template>
  <nav
    class="bg-white py-3 flex items-center justify-between border-t border-gray-200 sm:px-6"
    aria-label="Pagination"
  >
    <div class="hidden sm:block">
      <p class="text-sm text-gray-700">
        Mostrando
        {{ " " }}
        <span class="font-medium">{{
          (currentPage - 1) * paginateBy + 1
        }}</span>
        {{ " " }}
        a
        {{ " " }}
        <span class="font-medium">{{
          currentPage == pages ? count : currentPage * paginateBy
        }}</span>
        {{ " " }}
        de
        {{ " " }}
        <span class="font-medium">{{ count }}</span>
        {{ " " }}
        resultados
      </p>
    </div>
    <div class="flex-1 flex justify-between sm:justify-end">
      <inertia-link
        v-if="currentPage > 1"
        :href="previuosLink"
        class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
      >
        Anterior
      </inertia-link>
      <button
        v-else
        disabled="true"
        class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-300 bg-gray-100"
      >
        Anterior
      </button>

      <inertia-link
        v-if="currentPage < pages"
        :href="nextLink"
        class="relative inline-flex items-center px-4 py-2 ml-3 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
      >
        Siguiente
      </inertia-link>
      <button
        v-else
        disabled="true"
        class="relative inline-flex items-center px-4 py-2 ml-3 border border-gray-300 text-sm font-medium rounded-md text-gray-300 bg-gray-100"
      >
        Siguiente
      </button>
    </div>
  </nav>
</template>

<script>
export default {
  name: "PaginationTable",
  props: {
    link: {
      type: String,
      default: () => "",
    },
    count: {
      type: Number,
      default: () => 0,
    },
    paginateBy: {
      type: Number,
      default: () => 10,
    },
    pages: {
      type: Number,
      default: () => 1,
    },
    currentPage: {
      type: Number,
      default: () => 1,
    },
    search: {
      type: String,
      default: () => "",
    },
  },
  computed: {
    previuosLink() {
      let query = `?page=${this.currentPage - 1}`;
      if (this.search) {
        query = `${query}&search=${this.search}`;
      }
      return `${this.link}${query}`;
    },
    nextLink() {
      let query = `?page=${this.currentPage + 1}`;
      if (this.search) {
        query = `${query}&search=${this.search}`;
      }
      return `${this.link}${query}`;
    },
  },
};
</script>
