<script>
    import { createEventDispatcher } from 'svelte';  // 1. Schritt: Importieren Sie createEventDispatcher
    import Card from './Card.svelte';

    export let ausgelegte_karten = [];
    export let spielName = '';

    const dispatch = createEventDispatcher();  // 2. Schritt: Erstellen Sie einen dispatch
</script>

<style>
    .game-name {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: #f0f0f0; /* Weiß, passend zum dunklen Hintergrund */
        font-size: 1.7em; /* Größer für bessere Lesbarkeit */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Ein subtiler Textschatten für Tiefe */
        z-index: 1; /* Damit es über anderen Elementen erscheint, aber unter den Karten */
        opacity: 0.9; /* Ein wenig Transparenz, um den Tisch durchscheinen zu lassen */
        font-weight: bold; /* Fettschrift */
    }

    .content {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
        gap: 15px;
    }

    .table {
        background: #2a2a3e; /* An das dunklere Thema angepasst */
        width: 500px;
        height: 500px;
        border-radius: 20px;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 10px;
        box-shadow: 
            0 8px 24px rgba(0, 0, 0, 0.15),
            0 3px 8px rgba(0, 0, 0, 0.1); /* Ein stärkerer Schatten für mehr Tiefe */
        position: relative;
        border: 3px solid #3a3a4e; /* Einen kontrastreichen Rand hinzugefügt */
        transition: transform 0.3s, box-shadow 0.3s, border 0.3s; /* Hinzufügung von Border zur Transition */
    }

    .table:hover {
        transform: translateY(-4px); 
        box-shadow:
            0 12px 28px rgba(0, 0, 0, 0.18),
            0 4px 10px rgba(0, 0, 0, 0.12);
        border-color: #1a1a2e; /* Randfarbe ändert sich beim Überfahren mit der Maus */
    }
</style>

<div class="content">
    <div class="table" on:click={() => dispatch('click')}>  <!-- 3. Schritt: Fügen Sie den on:click-Handler hinzu -->
        <div class="game-name">{spielName}</div>
        {#each ausgelegte_karten as karte}
            <Card farbe={karte.farbe} wert={karte.wert} />
        {/each}
    </div>
</div>
