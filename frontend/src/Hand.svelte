<script>
    import Card from './Card.svelte';

    export let karten = [];

    let selectedCards = new Set();  // Set, um die ausgewählten Karten zu speichern

    function toggleCardSelection(card) {
        let cardIdentifier = card.wert + card.farbe;
        if (selectedCards.has(cardIdentifier)) {
            selectedCards.delete(cardIdentifier);
        } else {
            selectedCards.add(cardIdentifier);
        }
        selectedCards = new Set([...selectedCards]);  // Aktualisieren, um eine Reaktivität zu erzwingen
    }
</script>

<style>
    .hand {
        display: flex;
        flex-direction: row;
        gap: 10px;
        overflow-x: auto; 
        padding: 20px;
    }

    .selected {
        margin-top: -10px;
    }
</style>

<div class="hand">
    {#each karten as karte (karte.wert + karte.farbe)}
        <div
            class="card-container {selectedCards.has(karte.wert + karte.farbe) ? 'selected' : ''}"
            on:click={() => toggleCardSelection(karte)}>
            <Card farbe={karte.farbe} wert={karte.wert} />
        </div>
    {/each}
</div>
