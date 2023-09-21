<script>
    import { createEventDispatcher } from "svelte"; // 1. Schritt: Importieren Sie createEventDispatcher
    import Card from "./Card.svelte";

    export let ausgelegte_karten = [];
    export let spielName = "";

    const dispatch = createEventDispatcher(); // 2. Schritt: Erstellen Sie einen dispatch
</script>

<div class="content">
    <div class="table" on:click={() => dispatch("click")}>
        <!-- 3. Schritt: Fügen Sie den on:click-Handler hinzu -->
        {#each ausgelegte_karten as karte}
            <Card farbe={karte.farbe} wert={karte.wert} />
        {/each}
    </div>
</div>

<style>
    .table {
        width: 300px;
        height: 300px;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 10px;
        margin-top: 5vh;

        /* Setze alle visuellen Eigenschaften auf null */
        background: transparent;
        border: none;
        box-shadow: none;
    }

    .content {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
        gap: 15px;
    }
</style>
