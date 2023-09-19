<script>
    import { onMount } from 'svelte';
    import GameHandler from './GameHandler.js';
    import { gameDataStore} from './gameStore.js'; // Importiere den neuen Store
    import { selectedCardsStore } from './selectedCardsStore.js'; // Importiere den neuen Store
    import Hand from './Hand.svelte';
    import GameState from './GameState.svelte';
    import Table from './Table.svelte';
    
    export let params = {};

    let gameData = {};
    gameDataStore.subscribe(value => {
        gameData = value;
    });

    // Funktion, um die ausgewählten Karten zu spielen
    async function playSelectedCards() {
        let selectedCardsArray = [];

        // Konvertiert den Set von JSON-Zeichenketten zurück in ein Array von Objekten
        selectedCardsStore.subscribe(cards => {
            selectedCardsArray = [...cards].map(card => JSON.parse(card));
        })();

        const response = await handler.karteAusspielen(spielerName, selectedCardsArray, spielName);
        console.log(response);
        aktualisiereSpielstatus(); // Aktualisiert den Spielstatus nach dem Ausspielen
    }

    onMount(() => {
        if (spielName) {
            aktualisiereSpielstatus();
        }
        
        // Resette den selectedCardsStore beim Mounten
        selectedCardsStore.set(new Set());
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
<button on:click={playSelectedCards}>Legen</button>