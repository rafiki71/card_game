<script>
    import { selectedCardsStore } from './selectedCardsStore.js';
    import Card from './Card.svelte';

    export let karten = [];

    let selectedCards = new Set();

    selectedCardsStore.subscribe(value => {
        selectedCards = value;
    });

    function toggleCardSelection(card) {
        const cardAsJson = JSON.stringify(card); // Objekt zu JSON-String konvertieren

        if (selectedCards.has(cardAsJson)) {
            selectedCards.delete(cardAsJson);
        } else {
            selectedCards.add(cardAsJson);
        }

        // Aktualisieren Sie den Store mit dem neuen Zustand
        selectedCardsStore.set(new Set([...selectedCards]));
    }
</script>

<style>
    .hand {
        display: flex;
        flex-direction: row;
        gap: 10px;
        overflow-x: auto; 
        padding: 30px 20px 20px 20px; /* Erhöht den oberen Abstand */
        justify-content: center;  /* Zentriert die Karten horizontal */
        width: 100%; 
    }

    .card-container {
        transform: scale(1.2);  /* Vergrößert die Karte um 20% */
        transition: transform 0.3s ease;  /* Fügt eine sanfte Übergangsanimation hinzu */
    }

    .selected {
        transform: scale(1.2) translateY(-10px); /* Kombiniert das Anheben mit der Vergrößerung */
    }
</style>

<div class="hand">
    {#each karten as karte (karte.wert + karte.farbe)}
        <div
            class="card-container {selectedCards.has(JSON.stringify(karte)) ? 'selected' : ''}" 
            on:click={() => toggleCardSelection(karte)}>
            <Card farbe={karte.farbe} wert={karte.wert} />
        </div>
    {/each}
</div>
