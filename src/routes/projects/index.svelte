<script lang="ts">
    import type { Project } from '$lib/types';
    import { removeLang, removeTag, selectedLanguages, selectedTags } from '$lib/projects/stores';
    import { derived, writable } from 'svelte/store';
    import { includesAll } from '$lib/util';

    import ProjectCard from '$lib/projects/ProjectCard.svelte';
    
    let availableTags: string[];
    let availableLangs: string[];
    let projects = writable([] as Project[]);
    let search = writable('');

    const load = async () => {
        const res = await fetch('https://api.funnyboyroks.com/site/projects');
        $projects = await res.json();
        availableTags = [...new Set($projects.flatMap(p => p.tags).filter(n => n))].sort() as string[];
        availableLangs = [...new Set($projects.flatMap(p => p.languages).filter(n => n))].sort() as string[];
    };

    const addTag = (tag: string) => selectedTags.update(t => t.add(tag));
    const addLang = (lang: string) => selectedLanguages.update(t => t.add(lang));
    const adaptSearch = (s: string) => s.toLowerCase().trim().replace(/[\s-_]+/gi, '-');

    const searchMatch = (p: Project): boolean => {
        const s = adaptSearch($search);
        return adaptSearch(p.title).includes(s) || adaptSearch(p.description).includes(s);
    }
    
    const matchedProjects = derived([projects, selectedTags, selectedLanguages, search], ([projects, tags, langs, search]) => {
        return projects.filter(p =>
            (!tags.size || p.tags && includesAll(p.tags, tags))
            && (!langs.size || includesAll(p.languages, langs))
            && (!search || searchMatch(p))
            );
    }, []);

</script>

<svelte:head>
	<title>Projects | funnyboy_roks</title>
</svelte:head>

<div class="content">
    <h1>My Projects</h1>
    {#await load()}
        Loading...
    {:then}
        <div id="filter">
            <h3>Filter</h3>
            <input type="text" name="search" id="search" bind:value={$search} placeholder="Search">
            <div id="selections">
                <div id="tag-select">
                    <legend>Tag</legend>
                    {#each availableTags as tag, i (i)}
                        <div>
                            <input
                                type="checkbox"
                                on:input={(e) => e.target?.checked ? addTag(tag) : removeTag(tag)}
                                id="tag_{tag}"
                            >
                            <label for="tag_{tag}">{tag}</label>
                        </div>
                    {/each}
                </div>
                <div id="lang-select">
                    <legend>Language</legend>
                    {#each availableLangs as lang, i (i)}
                        <div>
                            <input
                                type="checkbox"
                                on:input={(e) => e.target?.checked ? addLang(lang) : removeLang(lang)}
                                id="lang_{lang}"
                            >
                            <label for="lang_{lang}">{lang}</label>
                        </div>
                    {/each}
                </div>
            </div>
        </div>

        <div id="projects">
            {#each $matchedProjects as project, n (n)}
                <ProjectCard {project} />
            {:else}
                <h3 class="error">No projects match your selection.</h3>
            {/each}
        </div>


    {:catch}
        <h1 class="error">Unable to load projects! Try again in later.</h1>
    {/await}
</div>

<style>

    #tag-select, #lang-select {
        display: flex;
        flex-direction: column;
    }

    #filter h3 { 
        padding: 0;
        margin: 0;
        font-size: 2rem;
        text-align: center;
    }

    #filter {
        position: fixed;
        padding: 1rem;
        left: 0;
        top: 50vh;
        transform: translateY(-50%);
        background: #ffffff05;
        border-radius: 0 1rem 1rem 0;
        border: 2px solid var(--accent-color);
        border-left: none;
    }

    #filter #search {
        background: #0003;
        outline: none;
        border: none;
        color: white;
        padding: .3rem;
        border-radius: .3rem;
    }

    legend {
        font-weight: bold;
    }
    
    #selections {
        display: flex;
    }

    #projects {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    @media only screen and (max-width: 480px) {

        #filter {
            /* width: 100%; */
            position: unset;
            top: unset;
            left: unset;
            transform: none;
            border: 2px solid var(--accent-color);
            border-radius: 1rem;
        }

    }

</style>
