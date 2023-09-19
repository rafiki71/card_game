<script>
    export let spieler_kartenanzahl = {};
</script>

<style>
    /* Dies stellt sicher, dass die Breitenberechnung Konsistenz für alle Elemente beibehält */
    *, *::before, *::after {
        box-sizing: border-box;
    }

    .header-card {
        background-color: #282c34;
        color: #fff;
        border-radius: 15px 15px 15px 15px; 
        padding: 10px 20px;
        display: flex;
        justify-content: space-around; 
        align-items: center;
        width: 100%; 
        max-width: 100vw;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
        margin: 0 auto 10px; /* zentriert den header-card horizontal */
        overflow-x: auto; /* ermöglicht das horizontale Scrollen, falls notwendig */
    }

    .player {
        display: flex;
        align-items: center;
        gap: 10px; 
    }

    .name {
        font-weight: bold;
    }

    .number {
        background-color: #4CAF50; 
        border-radius: 50%; 
        padding: 5px 10px;
        font-weight: bold;
    }
</style>



<div class="header-card">
    {#each Object.entries(spieler_kartenanzahl) as [name, anzahl]}
        <div class="player">
            <div class="name">{name}</div>
            <div class="number">{anzahl}</div>
        </div>
    {/each}
</div>
