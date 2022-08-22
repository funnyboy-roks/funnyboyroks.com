<script lang="ts">
	import type { Project } from '$lib/types';

	import CSSLogo from './images/css_logo.png';
	import HTMLLogo from './images/html_logo.svg';
	import JavaLogo from './images/java_logo.png';
	import JSLogo from './images/js_logo.png';
	import ProcessingLogo from './images/processing_logo.png';
	import PythonLogo from './images/python_logo.png';
	import TSLogo from './images/ts_logo.jpg';

	const logosMap = new Map<string, string>(
		Object.entries({
			css: CSSLogo,
			html: HTMLLogo,
			java: JavaLogo,
			javascript: JSLogo,
			processing: ProcessingLogo,
			python: PythonLogo,
			typescript: TSLogo
		})
	);

	export let project: Project;
</script>

<div class="project-card">
	<h1>{project.title}</h1>
	{#if project.source}
		<a href={project.source} id="source">View Source</a>
	{/if}
	<div id="langs">
		{#each project.languages as lang, i (i)}
			<img src={logosMap.get(lang.toLowerCase())} title={lang} alt={lang} class="logo" />
		{/each}
	</div>
	<div class="tags">
		{#if project.tags}
			{#each project.tags as tag, i (i)}
				<div class="tag">{tag}</div>
			{/each}
		{/if}
	</div>
	<p>{@html project.description}</p>
	<div id="links">
		{#if project.buttons}
			{#each project.buttons as { name, link }, i (i)}
				<a href={link} class="link">{name}</a>
			{/each}
		{/if}
	</div>
</div>

<style>
	.tags {
		display: flex;
		justify-content: center;
		width: 100%;
	}

	.tag {
		padding: 0.2rem 1rem;
		margin: 0.2rem;
		background: var(--accent-color);
		color: white;
		font-family: monospace;
		font-size: 0.8rem;
		border-radius: 1.8rem;
	}

	.project-card {
		background: #151515;
		border-radius: 0.75rem;
		width: 35%;
		margin: 2rem;
		padding: 2rem;
		text-align: center;
	}

	h1 {
		font-size: 2rem;
		margin: 0;
	}

	img.logo {
		height: 1.5rem;
		width: auto;
		margin: 0 0.2rem;
	}

	#links {
		display: flex;
		justify-content: space-evenly;
	}

	#source {
		font-size: 0.75rem;
		vertical-align: top;
	}

	@media only screen and (max-width: 480px) {
        .project-card {
            width: 100%;
            overflow: hidden;
        }
	}
</style>
