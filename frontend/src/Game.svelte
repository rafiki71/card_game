<script>
    import { onMount } from "svelte";
    import GameHandler from "./GameHandler.js";
    import { gameDataStore } from "./gameStore.js"; // Importiere den neuen Store
    import { selectedCardsStore } from "./selectedCardsStore.js"; // Importiere den neuen Store
    import Hand from "./Hand.svelte";
    import GameState from "./GameState.svelte";
    import Table from "./Table.svelte";

    export let params = {};

    let gameData = {};
    gameDataStore.subscribe((value) => {
        gameData = value;
    });

    // Funktion, um die ausgewählten Karten zu spielen
    async function playSelectedCards() {
        let selectedCardsArray = [];

        // Konvertiert den Set von JSON-Zeichenketten zurück in ein Array von Objekten
        selectedCardsStore.subscribe((cards) => {
            selectedCardsArray = [...cards].map((card) => JSON.parse(card));
        })();

        const response = await handler.karteAusspielen(
            spielerName,
            selectedCardsArray,
            spielName
        );
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

    let spielName = params.name || "";
    let spielerName = gameData.spielerName || "";
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

<div class="view-container">
    <GameState spieler_kartenanzahl={spielstatus.spieler_kartenanzahl} />
    <Table
        {spielName}
        ausgelegte_karten={spielstatus.ausgelegte_karten}
        on:click={spielStart}
    />
    {#if spielstatus && spielstatus.meine_karten}
        <Hand karten={spielstatus.meine_karten} />
    {/if}
    <button on:click={playSelectedCards}>Legen</button>
</div>

<style>
    /* Für die gesamte View */
    .view-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        height: 100vh;
        width: 100vw;
        background-image: url("/img/bgw.png");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        background-color: black;
    }

    /* Stil für den "Legen"-Button */
    button {
        /* Laser-Optic-Stil, ähnlich wie der Tisch */
        border: 2px solid rgba(0, 255, 255, 0.5);
        box-shadow: 0 0 5px rgba(0, 255, 255, 0.5), 0 0 10px #00ffff,
            0 0 15px #00ffff;
        border-radius: 20px;
        padding: 10px 20px;
        font-size: 1em;
        color: #f0f0f0;
        cursor: pointer;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 5vh;
    }

    button:hover {
        transform: translateY(-4px);
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.7), 0 0 20px #00ffff,
            0 0 30px #00ffff;
    }
</style>
