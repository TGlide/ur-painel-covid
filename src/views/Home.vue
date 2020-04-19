<template>
  <div class="home">
    <section class="section">
      <div class="container is-fluid">
        <div class="columns">
          <div class="column is-12">
            <Charts />
          </div>
        </div>

        <div class="columns">
          <div class="column is-7">
            <LocalStats />
          </div>
          <div class="column is-5">
            <CaseStats />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Charts from "@/components/Charts";
import LocalStats from "@/components/LocalStats";
import CaseStats from "@/components/CaseStats";

export default {
  name: "Home",
  components: { Charts, LocalStats, CaseStats }
};
</script>

<style lang="scss" scoped>
@import "@/styles/theme.scss";

/deep/ .box {
  height: 100%;

  .box-header {
    align-items: center;

    margin-bottom: 1rem;

    .title {
      margin-bottom: 0 !important;
    }

    .column:first-child {
      flex-grow: 1;
      flex-shrink: 0;
    }

    .column:last-child {
      &:not(:first-child) {
        flex-grow: 0;
      }
    }
  }
}
</style>
