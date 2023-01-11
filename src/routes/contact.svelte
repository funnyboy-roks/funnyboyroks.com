<script lang="ts">

    import { Circle } from 'svelte-loading-spinners';
    
    let formData = {
        name: '',
        contact: '',
        content: '',
    };

    let formState = 'unsubmitted';
    
    const submit = async () => {
        if(!formData.name || !formData.contact || !formData.content) {
            alert('Missing form fields!');
            return;
        }
        formState = 'submitted';
        const res = await fetch('https://api.funnyboyroks.com/site/contact', {
            method: 'POST',
            body: JSON.stringify(formData),
            headers: {
                'content-type': 'application/json',
            },
        });
        console.log('res');
        
        formState = res.ok ? 'success' : 'error';
    }
</script>

<svelte:head>
	<title>Contact | funnyboy_roks</title>
</svelte:head>

<div class="content">
    <h1>Contact Me</h1>
    <p>The best way to contact me is to use the form below, but I am also reachable on Discord by joining my <a href="/discord">Discord Server</a> or by email at <a href="mailto:funnyboyroks@gmail.com">funnyboyroks@gmail.com</a></p>
    
    <div id="form">
        {#if formState === 'unsubmitted' || formState === 'error'}
            {#if formState === 'error'}
                <h1 class="error">Error submitting form! Try again in a few minutes!</h1>
            {/if}
            <form on:submit|preventDefault={submit}>
                <input type="text" bind:value={formData.name} id="name" placeholder="Name">
                <input type="text" bind:value={formData.contact} id="contact" placeholder="Contact">
                <textarea id="content" bind:value={formData.content} placeholder="Content" />

                <button type="submit">Submit</button>
            </form>
        {:else if formState === 'submitted'}
            <center><Circle color="#5271ff" /></center>
        {:else if formState === 'success'}
            <h1 class="success">Message Sent!</h1>
            <p>I will try to respond as soon as possible!</p>
        {/if}
    </div>


</div>

<style>
    #form {
        text-align: center;
    }

    form {
        display: flex;
        flex-direction: column;
        margin: 0 15rem;
        text-align: center;
        font-size: 1.2rem;
    }
    
    form input, form textarea {
        font-size: 1.5rem;
        background: #111;
        color: #fff;
        border: none;
        outline: none;
        border-radius: 5px;
        font-family: monospace;
        padding: .5rem;
        margin: .5rem 0;
    }

    form textarea {
        height: 5rem;
    }

    form button {
        background: #111;
        color: #fff;
        border: none;
        outline: none;
        border-radius: 5px;
        margin-top: 1.2rem;
        padding: .5rem;
    }

    form button:hover {
        background: #000c;
        cursor: pointer;
    }

    @media only screen and (max-width: 480px) {
        form {
            width: 100%;
            margin: 0;
        }
    }
</style>