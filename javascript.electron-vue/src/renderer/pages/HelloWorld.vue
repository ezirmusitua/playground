<style lang="scss" scoped>
</style>

<template>
  <div>
    <p>Hello World</p>
    <form>
      <input title="target directory" v-model="target"/>
      <button @click="listdir">Search</button>
    </form>
    <ul>
      <li v-for="file in files">
        <p :title="file.path">{{file.name}}</p>
      </li>
    </ul>
    <button @click="$router.push({name: 'landing-page'})">Go to Home</button>
  </div>
</template>

<script>
  import { listdir } from '@/services/Utiltity';

  export default {
    name: 'HelloWorld',
    computed: {},
    methods: {
      listdir() {
        this.files = listdir(this.target);
      },
    },
    data() {
      return {
        target: '',
        files: [],
      };
    },
  };
</script>
