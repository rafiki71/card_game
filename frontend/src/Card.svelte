<script>
    export let farbe = '';
    export let wert = '';

    function farbeSymbol() {
        switch(farbe) {
            case 'Herz': return '♥';
            case 'Kreuz': return '♣';
            case 'Karo': return '♦';
            case 'Pik': return '♠';
            default: return '';
        }
    }
</script>

<style>
    .card {
        width: 80px;
        height: 120px;
        border-radius: 8px;
        padding: 10px;
        font-family: Arial, sans-serif;
        text-align: center;
        position: relative;
        background: transparent; /* Transparenter Hintergrund */
        transition: transform 0.2s;
        
        /* Neon-Blau-Stil, aber subtiler */
        border: 2px solid rgba(0, 255, 255, 0.5);
        box-shadow: 
            0 0 5px rgba(0, 255, 255, 0.5),
            0 0 10px rgba(0, 255, 255, 0.5);
    }

    /* Neon-Effekt auf Text und Symbole */
    .card .suit-symbol, .card .card-value {
        text-shadow: 
            0 0 5px rgba(0, 255, 255, 0.5),
            0 0 10px rgba(0, 255, 255, 0.5),
            0 0 15px #00ffff;
        color: rgba(0, 255, 255, 0.5);
    }

    .card:hover {
        transform: scale(1.05);
    }

    .suit-symbol {
        font-size: 20px;
        user-select: none;
    }

    .suit-symbol.top-left, .suit-symbol.bottom-right {
        position: absolute;
    }

    .suit-symbol.top-left {
        top: 10px;
        left: 10px;
    }

    .suit-symbol.bottom-right {
        bottom: 10px;
        right: 10px;
    }

    .card-value {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        font-size: 24px;
        font-weight: bold;
        user-select: none;
    }
</style>

<div class="card suit-{farbe.toLowerCase()}" title="{farbe} {wert}">
    <div class="suit-symbol top-left">{farbeSymbol()}</div>
    <div class="card-value">{wert}</div>
    <div class="suit-symbol bottom-right">{farbeSymbol()}</div>
</div>
