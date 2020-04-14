<template id='app'>
  <h1>hello</h1>
</template>

<script>
Vue.compoent("hello-component", {
  template: "#hello",
  el: function() {
    return "#hello";
  },
  data: function() {
    return {
      msg: "hello"
    };
  }
});
</script>

<style>
</style>
