<script lang="ts">

    const sketches = [
        {
            path: './p5/Cardoid',
            name: 'Cardoid',
        },
    ]

</script>

<div>
    <h1>My Various <a href="https://p5js.org">p5js</a> Projects</h1>
    <ul>
        {#each sketches as sketch, i (i)}
        <li><a href={sketch.path}>{sketch.name}</a></li>
        {/each}
    </ul>
    
</div>

<style>
</style>
