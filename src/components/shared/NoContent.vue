<template>
  <div class="no-content">
    <span class="emoji">🤔</span>
    <span class="msg">Nenhuma opção selecionada!</span>
  </div>
</template>

<style lang="scss" scoped>
.no-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  animation: fadeIn 0.5s;

  .emoji {
    display: block;
    font-size: 2rem;
  }
  .msg {
    display: block;
    font-size: 1.25rem;
  }
}
</style>
