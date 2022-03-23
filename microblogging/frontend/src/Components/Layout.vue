<template>
  <div class="min-h-full">
    <create-publication
      :open="openCreatePublication"
      @open-modal="(value) => (openCreatePublication = value)"
    />

    <Disclosure as="nav" class="bg-white border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex">
            <div class="flex-shrink-0 text-gray-500 flex items-center">
              Microblogging
            </div>
          </div>
          <div class="hidden sm:ml-6 sm:flex sm:items-center">
            <button
              type="button"
              class="ml-3 inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              @click="openCreatePublication = true"
            >
              Nueva Publicación
            </button>
          </div>
        </div>
      </div>
    </Disclosure>

    <div class="py-10">
      <slot name="content" />
    </div>
  </div>
</template>

<script>
import { Disclosure } from "@headlessui/vue";
import CreatePublication from "../Components/CreatePublication.vue";

export default {
  components: {
    Disclosure,
    CreatePublication,
  },
  data() {
    return {
      openCreatePublication: false,
    };
  },
};
</script>
