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
        background-color: #eae7dc; /* Ein weicher beiger Hintergrund */
        box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s;
    }

    .card:hover {
        transform: scale(1.05);
    }

    .card.suit-herz, .card.suit-karo {
        color: #e85a4f; /* Ein tieferes Rot */
    }

    .card.suit-kreuz, .card.suit-pik {
        color: #6b705c; /* Ein weiches Grau/Schwarz */
    }

    .suit-symbol {
        font-size: 20px;
        user-select: none;
    }

    .suit-symbol.top-left {
        position: absolute;
        top: 10px;
        left: 10px;
    }

    .suit-symbol.bottom-right {
        position: absolute;
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

    /* Ein leichter Gradient im Hintergrund für eine bessere Tiefe */
    .card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: -1;
        border-radius: 8px;
        background: linear-gradient(45deg, #d8c3a5 0%, #e2d4b5 100%);
    }
</style>

<div class="card suit-{farbe.toLowerCase()}" title="{farbe} {wert}">
    <div class="suit-symbol top-left">{farbeSymbol()}</div>
    <div class="card-value">{wert}</div>
    <div class="suit-symbol bottom-right">{farbeSymbol()}</div>
</div>
