<script>
    import { onMount } from 'svelte';
    import GameHandler from './GameHandler.js';
    import { gameDataStore } from './gameStore.js';
    import Hand from './Hand.svelte';
    
    export let params = {};

    let gameData = {};
    gameDataStore.subscribe(value => {
        gameData = value;
    });

    let spielName = params.name || '';
    let spielerName = gameData.spielerName || '';
    let spielstatus = {};

    const handler = new GameHandler();

    onMount(() => {
        if (spielName) {
            aktualisiereSpielstatus();
        }
    });

    async function aktualisiereSpielstatus() {
        spielstatus = await handler.spielstatusAbrufen(spielName, spielerName);
        console.log(spielstatus);
    }

    async function spielStart() {
        const response = await handler.spielStarten(spielName);
        console.log(response);
        aktualisiereSpielstatus();
        // Sie können hier weitere Aktionen durchführen, z.B. den Spielstatus erneut aktualisieren oder eine Benachrichtigung anzeigen.
    }

</script>

<h1>{spielName}</h1>
<h1>{spielerName}</h1>

<button on:click={spielStart}>Spiel starten</button>
{#if spielstatus && spielstatus.meine_karten}
    <Hand karten={spielstatus.meine_karten} />
{/if}