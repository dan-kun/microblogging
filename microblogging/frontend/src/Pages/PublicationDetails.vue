<template>
  <layout>
    <template #content>
      <edit-publication
        title-modal="Editar Publicación"
        title-button="Editar"
        :url-action="route('blog:edit_publication', publication.id)"
        :publication="publication"
        :open="openEditPublication"
        @open-modal="(value) => (openEditPublication = value)"
      />

      <header>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 class="text-3xl font-bold leading-tight text-gray-900">
            {{ publication.title }}
          </h1>
          <h4 class="mt-2 text-2xl font-bold leading-tight text-gray-500">
            {{ publication.author }}
          </h4>
          <p class="mt-2 text-sm text-gray-300">{{ publication.date }}</p>
        </div>
      </header>
      <main>
        <div class="mt-10 max-w-7xl mx-auto sm:px-6 lg:px-8">
          <p>{{ publication.content }}</p>
        </div>

        <div class="mt-6 max-w-7xl mx-auto sm:px-6 lg:px-8">
          <p>
            <span class="ml-2 flex text-sm font-medium text-gray-500">
              {{ publication.upVotes }}
              <ThumbUpIcon class="w-5 h-5 text-blue-500" /> /
              {{ publication.downVotes }}
              <ThumbDownIcon class="w-5 h-5 text-red-500" />
            </span>
          </p>
        </div>

        <div class="mt-6 flex max-w-7xl mx-auto sm:px-6 lg:px-8">
          <button
            type="button"
            class="ml-1 flex inline-flex justify-center rounded-md border border-red-700 shadow-sm px-4 py-2 bg-red-600 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:col-start-2 sm:text-sm"
          >
            Eliminar
          </button>
          <button
            type="button"
            class="ml-1 flex inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:col-start-2 sm:text-sm"
            @click="openEditPublication = true"
          >
            Editar
          </button>
          <inertia-link
            class="ml-1 flex inline-flex justify-center rounded-md border border-gray-700 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-100 sm:col-start-2 sm:text-sm"
            :href="route('blog:publications')"
          >
            Regresar
          </inertia-link>
        </div>
      </main>
    </template>
  </layout>
</template>

<script>
import Layout from "../Components/Layout.vue";
import EditPublication from "../Components/CreatePublication.vue";
import { ThumbUpIcon, ThumbDownIcon } from "@heroicons/vue/outline";

export default {
  components: {
    Layout,
    EditPublication,
    ThumbUpIcon,
    ThumbDownIcon,
  },
  props: {
    publication: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      openEditPublication: false,
    };
  },
};
</script>
