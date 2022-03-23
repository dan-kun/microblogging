<template>
  <TransitionRoot as="template" :show="open">
    <Dialog
      as="div"
      static
      class="fixed z-10 inset-0 overflow-y-auto"
      :open="open"
      @click="$emit('show-modal', false)"
    >
      <div
        class="flex items-center justify-center min-h-screen pt-4 px-4 pb-60 text-center sm:block sm:p-0 sm:pb-0"
      >
        <TransitionChild
          as="template"
          enter="ease-out duration-300"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="ease-in duration-200"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <DialogOverlay
            class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
          />
        </TransitionChild>

        <!-- This element is to trick the browser into centering the modal contents. -->
        <span
          class="hidden sm:inline-block sm:align-middle sm:h-screen"
          aria-hidden="true"
          >&#8203;</span
        >
        <TransitionChild
          as="template"
          enter="ease-out duration-300"
          enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
          enter-to="opacity-100 translate-y-0 sm:scale-100"
          leave="ease-in duration-200"
          leave-from="opacity-100 translate-y-0 sm:scale-100"
          leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
        >
          <div
            class="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg w-full sm:p-6"
          >
            <div>
              <DialogTitle
                ref="title"
                as="h3"
                class="text-center text-lg leading-6 font-medium text-gray-900"
              >
                {{ titleModal }}
              </DialogTitle>
              <hr class="my-4" />

              <form @submit="onSubmit">
                <div class="mt-2">
                  <div class="py-2 sm:py-2">
                    <div class="font-medium text-gray-500">Título</div>
                    <div class="flex text-sm text-gray-900">
                      <span class="flex-grow">
                        <div class="mt-2 relative rounded-md shadow-sm">
                          <input
                            id="titulo"
                            name="title"
                            type="text"
                            v-model="form.title"
                            @input="checkFieldsErrors('title')"
                            class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                            :class="[
                              fieldsErrors.title
                                ? 'border-red-300 focus:ring-red-500 focus:border-red-500'
                                : 'border-gray-300 focus:ring-indigo-500 focus:border-indigo-500',
                            ]"
                          />
                          <div
                            class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none"
                          >
                            <ExclamationCircleIcon
                              class="h-5 w-5 text-red-500"
                              aria-hidden="true"
                              v-show="fieldsErrors.title"
                            />
                          </div>
                        </div>
                        <p
                          v-for="text in textErrors.title"
                          v-show="fieldsErrors.title"
                          :key="text"
                          class="mt-1 text-xs text-red-600"
                        >
                          {{ text }}
                        </p>
                      </span>
                    </div>

                    <div class="mt-2 font-medium text-gray-500">Autor</div>
                    <div class="flex text-sm text-gray-900">
                      <span class="flex-grow">
                        <div class="mt-2 relative rounded-md shadow-sm">
                          <input
                            id="autor"
                            name="author"
                            type="text"
                            v-model="form.author"
                            @input="checkFieldsErrors('author')"
                            class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                            :class="[
                              fieldsErrors.author
                                ? 'border-red-300 focus:ring-red-500 focus:border-red-500'
                                : 'border-gray-300 focus:ring-indigo-500 focus:border-indigo-500',
                            ]"
                          />
                          <div
                            class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none"
                          >
                            <ExclamationCircleIcon
                              class="h-5 w-5 text-red-500"
                              aria-hidden="true"
                              v-show="fieldsErrors.author"
                            />
                          </div>
                        </div>
                        <p
                          v-for="text in textErrors.author"
                          v-show="fieldsErrors.author"
                          :key="text"
                          class="mt-1 text-xs text-red-600"
                        >
                          {{ text }}
                        </p>
                      </span>
                    </div>

                    <div class="mt-2 font-medium text-gray-500">Contenido</div>
                    <div class="flex text-sm text-gray-900">
                      <span class="flex-grow">
                        <div class="mt-2 relative rounded-md shadow-sm">
                          <textarea
                            id="content"
                            name="content"
                            v-model="form.content"
                            @input="checkFieldsErrors('content')"
                            class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                            :class="[
                              fieldsErrors.content
                                ? 'border-red-300 focus:ring-red-500 focus:border-red-500'
                                : 'border-gray-300 focus:ring-indigo-500 focus:border-indigo-50',
                            ]"
                            rows="6"
                          />
                        </div>
                        <p
                          v-for="text in textErrors.content"
                          v-show="fieldsErrors.content"
                          :key="text"
                          class="mt-1 text-xs text-red-600"
                        >
                          {{ text }}
                        </p>
                      </span>
                    </div>
                  </div>
                </div>
                <div class="mt-4 sm:mt-4 flex">
                  <button
                    type="button"
                    class="w-full ml-1 flex inline-flex justify-center rounded-md border border-gray-700 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-100 sm:col-start-2 sm:text-sm"
                    @click="closeModal"
                  >
                    Cerrar
                  </button>
                  <button
                    type="submit"
                    :disabled="isSendingForm"
                    class="w-full ml-1 flex inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:col-start-2 sm:text-sm"
                  >
                    {{ titleButton }}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </TransitionChild>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script>
import useVuelidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";
import {
  Dialog,
  DialogOverlay,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import { ExclamationCircleIcon } from "@heroicons/vue/solid";

export default {
  components: {
    Dialog,
    DialogOverlay,
    DialogTitle,
    TransitionChild,
    TransitionRoot,
    ExclamationCircleIcon,
  },
  props: {
    open: {
      type: Boolean,
      default: () => false,
    },
    titleModal: {
      type: String,
      default: () => "Nueva Publicación",
    },
    titleButton: {
      type: String,
      default: () => "Crear",
    },
    urlAction: {
      type: String,
      default: () => "/create/publication",
    },
    publication: {
      type: Object,
      default: () => {
        return {
          title: "",
          author: "",
          content: "",
        };
      },
    },
  },
  emits: ["open-modal"],
  setup() {
    return { v$: useVuelidate() };
  },
  validations() {
    return {
      form: {
        title: { required },
        author: { required },
        content: { required },
      },
    };
  },
  data() {
    return {
      isSendingForm: false,
      form: {
        title: this.publication.title,
        author: this.publication.author,
        content: this.publication.content,
      },
      fieldsErrors: {
        title: false,
        author: false,
        content: false,
      },
      textErrors: {
        title: [],
        author: [],
        content: [],
      },
    };
  },
  methods: {
    clearFields() {
      for (const item in this.fieldsErrors) {
        this.fieldsErrors[item] = false;
      }
      for (const item in this.form) {
        this.form[item] = this.publication[item];
      }
    },
    checkFieldsErrors(field) {
      this.fieldsErrors[field] = false;
      this.textErrors[field] = [];
      this.v$.$validate();
      if (this.v$.form[field].$errors.length) {
        this.fieldsErrors[field] = true;
        this.textErrors[field].push(this.v$.form[field].$errors[0].$message);
      }
    },
    fieldsValidate() {
      let valid = true;
      this.checkFieldsErrors("title");
      this.checkFieldsErrors("author");
      this.checkFieldsErrors("content");
      for (const item in this.fieldsErrors) {
        if (this.fieldsErrors[item]) {
          valid = false;
        }
      }
      return valid;
    },
    onSubmit(event) {
      event.preventDefault();
      let valid = this.fieldsValidate();
      if (!valid) return;
      try {
        this.$inertia.post(this.urlAction, this.form, {
          onStart: () => (this.isSendingForm = true),
          onFinish: () => {
            this.isSendingForm = false;
            this.closeModal();
          },
        });
      } catch (error) {
        alert(error);
      }
    },
    closeModal() {
      this.clearFields();
      this.$emit("open-modal", false);
    },
  },
};
</script>
