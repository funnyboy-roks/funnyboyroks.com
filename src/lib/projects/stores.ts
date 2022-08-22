import { writable } from 'svelte/store';

export const selectedTags = writable(new Set<string>());

export const removeTag = (tag: string) => {
    selectedTags.update((t) => { t.delete(tag); return t });
}



export const selectedLanguages = writable(new Set<string>());

export const removeLang = (lang: string) => {
    selectedLanguages.update((t) => { t.delete(lang); return t });
}