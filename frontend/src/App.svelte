<script>
    import { Router, Route } from 'svelte-routing';
    import Home from './Home.svelte';
    import Game from './Game.svelte';
</script>

<main>
    <Router>
        <Route path="/" component={Home} />
        <Route path="/game/:name" let:params>
            <Game {params} />
        </Route>
    </Router>
</main>
