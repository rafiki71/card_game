<script>
    import { onMount } from 'svelte';
    import GameHandler from './GameHandler.js';
    import { gameDataStore } from './gameStore.js';
    import Hand from './Hand.svelte';
    import GameState from './GameState.svelte';
    import Table from './Table.svelte';
    
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
    }

</script>

<GameState spieler_kartenanzahl={spielstatus.spieler_kartenanzahl} />
<Table spielName={spielName} ausgelegte_karten={spielstatus.ausgelegte_karten} on:click={spielStart}/>
{#if spielstatus && spielstatus.meine_karten}
    <Hand karten={spielstatus.meine_karten} />
{/if}
