<template>
  <layout>
    <template #content>
      <header>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 class="text-3xl font-bold leading-tight text-gray-900">
            Publicaciones
          </h1>
        </div>
      </header>
      <main>
        <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
          <div v-if="publications.length > 0">
            <ul role="list" class="divide-y divide-gray-200">
              <li v-for="pub in publications" :key="pub.id" class="py-4 flex">
                <div class="ml-3">
                  <p class="flex text-sm font-medium">
                    <span class="text-md text-gray-900">{{ pub.title }}</span>
                    <span class="ml-2 text-gray-500">({{ pub.author }})</span>
                    <span class="ml-2 flex text-sm font-medium text-gray-500">
                      {{ pub.upVotes }}
                      <ThumbUpIcon class="w-5 h-5 text-blue-500" /> /
                      {{ pub.downVotes }}
                      <ThumbDownIcon class="w-5 h-5 text-red-500" />
                    </span>
                  </p>
                  <p class="mt-2 text-sm text-gray-500">
                    {{ pub.content }}
                    <inertia-link
                      class="ml-2 text-sm text-blue-500 hover:text-blue-700"
                      :href="route('blog:index')"
                    >
                      Ver más
                    </inertia-link>
                  </p>
                  <p class="text-xs">
                    <span class="text-gray-500">{{ pub.date }}</span>
                  </p>
                </div>
              </li>
            </ul>

            <pagination
              :link="route('blog:publications')"
              :count="count"
              :paginate-by="paginateBy"
              :pages="pages"
              :current-page="currentPage"
            />
          </div>
          <div v-else>
            <p class="text-lg font-medium text-center py-14">
              No hay Publicaciones. Cree una nueva publicación
            </p>
          </div>
        </div>
      </main>
    </template>
  </layout>
</template>

<script>
import Layout from "../Components/Layout.vue";
import Pagination from "../Components/Pagination.vue";
import { ThumbUpIcon, ThumbDownIcon } from "@heroicons/vue/outline";

export default {
  components: {
    Layout,
    Pagination,
    ThumbUpIcon,
    ThumbDownIcon,
  },
  props: {
    publications: {
      type: Array,
      default: () => [],
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
  },
};
</script>
