<script 0lang="ts">
	import { browser, dev } from '$app/env';

	// we don't need any JS on this page, though we'll load
	// it in dev so that we get hot module replacement...
	export const hydrate = dev;

	// ...but if the client-side router is already loaded
	// (i.e. we came here from elsewhere in the app), use it
	export const router = browser;

	// since there's no dynamic data here, we can prerender
	// it so that it gets served as a static asset in prod
	export const prerender = true;
</script>

<svelte:head>
	<title>Home | funnyboy_roks</title>
</svelte:head>


<div class="content">
	<h1>Hello!</h1>
	<p>I am Hayden Pott, though many people know me as funnyboy_roks.
		I am currently studying Computer Science at Louisiana Tech University.</p>	

</div>

<style>

	.content {
		margin: 0 10rem;
	}

	h1 {
		width: 100%;
	}

</style>
