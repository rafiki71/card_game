<script>
    import { onMount } from 'svelte';
    import GameHandler from './GameHandler.js';
    import { navigate } from 'svelte-routing'; 
    import { gameDataStore } from './gameStore.js';


    let spiele = [];
    let neuerSpielName = '';
    let spielerName = '';

    const handler = new GameHandler();

    onMount(ladenSpiele);

    async function ladenSpiele() {
        const result = await handler.alleSpiele();
        spiele = result.spiele;
    }

    async function spielErstellen() {
        await handler.spielErstellen(neuerSpielName);
        neuerSpielName = ''; 
        ladenSpiele();
    }

    async function spielBeitreten(spielName) {
        gameDataStore.update(data => {
        data.spielerName = spielerName;
        return data;
        });

        await handler.spielerBeitreten(spielerName, spielName);        
        // Nachdem der Spieler erfolgreich beigetreten ist, navigieren Sie zur Spielansicht
        navigate(`/game/${spielName}`);
    }

    async function spielLoeschen(name) {
        await handler.spielLoeschen(name);
        ladenSpiele();
    }
</script>

<div class="container">
    <div class="player-name-input">
        <input id="playerName" class="game-input" bind:value={spielerName} placeholder="Ihr Name" />
    </div>

    <div class="header">
        <input class="game-input" bind:value={neuerSpielName} placeholder="Neues Spiel erstellen" />
        <button class="create-btn" on:click={spielErstellen}>+</button>
    </div>


    <ul class="games-list">
        {#each spiele as spiel}
            <li class="game-item" on:click={() => spielBeitreten(spiel)}>
                <span>{spiel}</span>
                <i class="fas fa-trash-alt delete-icon" on:click={(event) => { 
                    event.stopPropagation();  // Verhindert das Weiterleiten des Events an übergeordnete Elemente
                    spielLoeschen(spiel);
                }}></i>
                
            </li>
        {/each}
    </ul>
</div>

<style>
     .player-name-input {
        margin-top: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Optional: Stil für das Label */
    label {
        color: #e6e6e6;
        font-weight: bold;
    }

    .container {
        width: 100%;
        max-width: 700px;
        margin: 5% auto;
        padding: 20px;
        background-color: #162447; /* Dunkler Hintergrund */
        border-radius: 10px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
    }

    .header {
        display: flex;
        justify-content: space-between;
    }

    .game-input {
        flex-grow: 1;
        padding: 10px 15px;
        font-size: 16px;
        border: 1px solid #e6e6e6;
        border-radius: 8px;
        margin-right: 10px;
        background-color: #1f4068; /* Dunkelblauer Input */
        color: #e6e6e6; /* Textfarbe */
        outline: none;
    }

    .create-btn {
        width: 40px;
        height: 40px;
        background-color: #e43f5a; /* Hervorgehobenes Pink */
        border: none;
        border-radius: 50%; /* Kreisform */
        color: #FFF;
        cursor: pointer;
        transition: background-color 0.3s;
        font-size: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .create-btn:hover {
        background-color: #d83367; /* Dunkleres Pink beim Überfahren */
    }

    .games-list {
        margin-top: 20px;
    }

    .game-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 15px;
        background-color: #1b1b2f; /* Noch dunklerer Hintergrund */
        margin: 10px 0;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .game-item:hover {
        background-color: #23243a; /* Etwas hellerer Blauton beim Überfahren */
    }

    .delete-icon {
        cursor: pointer;
        color: #e43f5a; /* Rot für das Löschen-Icon */
        font-size: 20px;
        transition: color 0.3s;
    }

    .delete-icon:hover {
        color: #d83367; /* Dunkleres Rot beim Überfahren */
    }
</style>
